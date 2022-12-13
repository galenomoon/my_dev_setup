from methods import create_and_editing
from initializer import initialize
from termcolor import colored

initialize()
print('To connect to git, you need:')
print('1) to have git installed on your computer. To install git, go to https://git-scm.com/downloads')
print('2) to have a github account. To create a github account, go to https://github.com/')
print('3) to have a github token. To create a github token, go to https://github.com/settings/tokens')
print('-' * 50)
token = input('Enter your github token: ')
print(colored("GitHub token saved!", 'green'))
create_and_editing('.env', f"GITHUB_TOKEN={token}")