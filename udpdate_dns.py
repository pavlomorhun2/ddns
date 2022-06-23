from repo.default_repos import DefaultRepo
from resolvers import ProviderReposResolver

try:
    # initial repos
    default_repo = DefaultRepo()
    remote_repo = ProviderReposResolver.get_repo('godaddy')
    # obtain public IP
    ip = default_repo.get_public_ip()
    # obtain IP of DNS
    result = remote_repo.get_record('cloud')
    old_ip = result['data']

    if old_ip != ip:
        remote_repo.update_record('cloud', ip)

except Exception as e:
    print(str(e))
