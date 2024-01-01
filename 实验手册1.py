from github import Github

token = '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'

t = Github(token)
user = t.get_user()

followers = user.get_following()

for follower in followers:
    repos = follower.get_repos()
    for repo in repos:
        with open('repos.txt', 'a') as file:
            file.write(f"{follower.login} : {repo.name}\n")