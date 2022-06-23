from repo.providers_repos import ProviderRepoInterface, GoDaddyRepo


class ProviderReposResolver:
    GODADDY = 'godaddy'

    repos_map = {
        GODADDY: GoDaddyRepo,
    }

    @staticmethod
    def get_repo(provider_name: str) -> ProviderRepoInterface:
        repo = ProviderReposResolver.repos_map.get(provider_name)

        if not repo:
            raise Exception(f'Provider {provider_name} does not have repo')

        return repo()
