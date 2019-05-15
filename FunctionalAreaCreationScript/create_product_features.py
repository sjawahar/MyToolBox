import argparse
import requests
import csv
import json

parser = argparse.ArgumentParser(description='Creates Functional Area tasks for a given JIRA project, based on a CSV file')
parser.add_argument('jira_username', help='Your Jira username')
parser.add_argument('jira_password', help='Your Jira password')
parser.add_argument('project', help='your peoject ID')
parser.add_argument('csv_file_path', help='Path to CSV file that contains which features to create')

args = parser.parse_args()
jira_auth = (args.jira_username, args.jira_password)
request = requests.get(
    'https://jira.devfactory.com/rest/api/2/search'
    '?maxResults=3000&jql=issuetype="Functional Area" '
    'AND project="{project}"'.format(project=args.project), auth=jira_auth)
feature_requests = request.json()['issues']
print 'Existing features: ', map(lambda f: f['key'] + ' ' + f['fields']['summary'], feature_requests)

with open(args.csv_file_path, 'r') as csvfile:
    with open(args.csv_file_path + '.out', 'wb') as outcsvfile:
        reader = csv.reader(csvfile)
        has_header = csv.Sniffer().has_header(file.read(csvfile))
        csvfile.seek(0)  # Rewind.
        if has_header:
            next(reader,None)
        writer = csv.writer(outcsvfile)
        for row in reader:
            feature_name = row[0]
            target_e2e = int(row[1])
            key = None
            existing_feature = next(iter(filter(lambda f: f['fields']['summary'] == feature_name, feature_requests)), None)
            if existing_feature is not None:
                print 'Feature', feature_name, 'already exists, skipping...'
                key = existing_feature['key']
            else:
                print 'Creating feature', feature_name, ' with target:', target_e2e
                dumps = {
                    'fields': {
                        'project': {
                            'key': args.project
                        },
                        'summary': feature_name,
                        'description': 'Generated automatically by E2E generator',
                        'issuetype': {'name': 'Functional Area'},
                        'customfield_22803': target_e2e
                    }
                }
                r = requests.post('https://jira.devfactory.com/rest/api/2/issue/', auth=jira_auth, json=dumps)
                if r.status_code != 200 and r.status_code != 201:
                    print 'Error trying to create issue, ', r.status_code, ': ', r.text
                else:
                    print 'Done'
                    key = 'https://jira.devfactory.com/browse/'+json.loads(r.text)['key']
            writer.writerow([feature_name, key if key is not None else 'Error'])
