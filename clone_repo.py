from git import Repo

# List of repositories to clone
repositories = [
    {
        'url': 'https://github.com/user/repo1.git',
        'destination': 'codecommit://<your-aws-region>/<repository-name>'
    },
    {
        'url': 'https://github.com/user/repo2.git',
        'destination': 'codecommit://<your-aws-region>/<repository-name>'
    },
    {
        'url': 'https://github.com/user/repo3.git',
        'destination': 'codecommit://<your-aws-region>/<repository-name>'
    }
]

# Clone the repositories
for repo in repositories:
    try:
        Repo.clone_from(repo['url'], repo['destination'])
        print(f"Successfully cloned repository: {repo['url']}")
    except Exception as e:
        print(f"Error cloning repository: {repo['url']}")
        print(e)
