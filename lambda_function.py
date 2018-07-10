import requests


def lambda_handler(event, context):
    print('deployed using Ansible')
    r = requests.get('http://www.navcode.info')
    print(f'URL : {r.url}')
    print(f'Status Code : {r.status_code}')
    print(f'Response Length : {len(r.content)}')
    return True
