import requests
import sys
import os

file_name = sys.argv[1]
scan_type = ''

if file_name == 'gitleaks-results.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'semgrep-results.json':
    scan_type = 'Semgrep JSON Report'
elif file_name == 'snyk-results.json':
    scan_type = 'Snyk Scan'    
elif file_name == 'trivy-results.json':
    scan_type = 'Trivy Scan'
elif file_name == 'zap-results.xml':
    scan_type = 'ZAP Scan'

# Get the token from the environment variable
token = os.environ.get('DEFECTDOJO_TOKEN')
if not token:
    print('Error: DEFECTDOJO_TOKEN environment variable is not set.')
    sys.exit(1)

headers = {
    'Authorization': f'Token {token}'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 21
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')