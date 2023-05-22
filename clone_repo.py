from git import Repo

# List of repositories to clone
repositories = [
    'https://github.com/user/repo1.git',
    'https://github.com/user/repo2.git',
    'https://github.com/user/repo3.git'
]

# Destination folder where the repositories will be cloned
destination_folder = '/path/to/destination/folder'

# Clone the repositories
for repo_url in repositories:
    try:
        repo_name = repo_url.split('/')[-1].split('.')[0]
        repo_destination = f"{destination_folder}/{repo_name}"
        Repo.clone_from(repo_url, repo_destination)
        print(f"Successfully cloned repository: {repo_url}")
    except Exception as e:
        print(f"Error cloning repository: {repo_url}")
        print(e)
