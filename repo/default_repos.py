from requests import get


class DefaultRepo:
    def get_public_ip(self):
        return get('https://api.ipify.org').content.decode('utf8')
