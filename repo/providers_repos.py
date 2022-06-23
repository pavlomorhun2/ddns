import json

from requests import get, put


class ProviderRepoInterface:
    def get_record(self, record_name: str):
        raise NotImplementedError

    def update_record(self, record_name: str, ip: str):
        raise NotImplementedError


class GoDaddyRepo(ProviderRepoInterface):
    def __init__(self):
        self.api_key = 'e5NMoriCci2m_Vcpb6JDfugLuqpqrYteH9H'
        self.api_secret = 'HGPjCPN4dkqKbXKJspBgkF'
        self.api_path = 'https://api.godaddy.com'
        self.domain = 'pavlomorhun.com'

    def get_headers(self):
        return {
            'Authorization': f'sso-key {self.api_key}:{self.api_secret}',
        }

    def get_record(self, record_name: str):
        result = get(
            f'{self.api_path}/v1/domains/{self.domain}/records/A/{record_name}',
            headers=self.get_headers(),
        )

        if result.status_code >= 400:
            raise Exception(result.text)

        return json.loads(result.text)[0]

    def update_record(self, record_name: str, ip: str):
        result = put(
            f'{self.api_path}/v1/domains/{self.domain}/records/A/{record_name}',
            json=[{
                    "data": ip,
                    "name": "cloud",
                    "ttl": 600,
                    "type": "A"
                }],
            headers=self.get_headers(),
        )

        if result.status_code >= 400:
            raise Exception(result.text)

        return json.loads(result.text)
