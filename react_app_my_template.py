import os
from dotenv import load_dotenv
from termcolor import colored
import requests

def create_and_editing(filename, content):
  file = open(filename, '+w')
  file.write(content)
  file.close()

def create_env_file():
  create_and_editing('.env', 'REACT_APP_API_URL=http://localhost:3000')

def create_react_app(react_app_name, creation_mode):
  os.system('npx create-react-app '+ react_app_name)
  os.chdir(react_app_name)
  create_env_file()
  if creation_mode == '1':
    generate_default_template()
  if creation_mode == '2':
    generate_default_template()
    # generate_custom_template()
  
def generate_default_template():
  folders = ['components', 'pages', 'config', 'assets', 'routes', 'utils']
  for folder in folders:
    os.mkdir('src/' + folder)

def generate_custom_template(folders):
  # custom folders
  return

def after_creation(after_creation_mode):
  if after_creation_mode == '1' or after_creation_mode == '3':
    os.system('npm start')
  if after_creation_mode == '2' or after_creation_mode == '3':
    os.system('code .')

def remove_default_files():
  os.remove('src/setupTests.js')
  os.remove('src/App.test.js')
  os.remove('src/logo.svg')

def create_repo(reponame, is_public=True):
  load_dotenv()
  print('-' * 12)
  print(colored("Creating repository on your github account", 'green'))
  url = 'https://api.github.com/user/repos'
  token = os.environ['GITHUB_TOKEN']
  headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json'}
  requests.post(url, json={'name': reponame, 'public' : is_public}, headers=headers)
  
def git_connection(reponame, is_public=True):
  create_repo(reponame, is_public)  
  print('-' * 12)
  print(colored("Repository Created!", 'green'))
  username = os.popen('git config user.name').read().replace("\n", "")
  os.system('git init')
  os.system('git add .')
  os.system('git commit -m "Initial commit"')
  os.system('git branch -M master')
  os.system(f"git remote add origin git@github.com:{username}/{reponame}.git")
  os.system('git push -u origin master')
  

print(colored("Welcome to your app...", 'green'))
print(colored('''
██████╗ ███████ ██╗   ██╗  ███████ ███████ ████████ ██╗   ██ ██████╗ 
██╔══██ ██╔════ ██║   ██║  ██╔════ ██╔════ ╚══██╔══ ██║   ██ ██╔══██╗
██║  ██ █████╗  ██║   ██║  ███████ █████╗     ██║   ██║   ██ ██████╔╝
██║  ██ ██╔══╝  ╚██╗ ██╔╝  ╚════██ ██╔══╝     ██║   ██║   ██ ██╔═══╝ 
██████╔ ███████╗ ╚████╔╝   ███████ ███████╗   ██║   ╚██████╔ ██║     
╚═════╝ ╚══════╝  ╚═══╝    ╚══════ ╚══════╝   ╚═╝    ╚═════╝╚═╝     
''', 'cyan'))
print(colored("Your react app generator!", 'green'))

print('-' * 50)

print('Enter the name of the', colored('react app: ', 'green'), end='')
react_app_name = input()

print('-' * 25)

creation_mode = input('Enter the creation mode: \n1) Default\n2) Custom\n[1/2]: ')

print('-' * 25)

after_creation_mode = input('After creation: \n1) Start app\n2) Open code\n3) Both\n4) None\n[1/2/3/4]: ')

print('-' * 25)

create_git = input('Create a repo to git? It will create a repo with the same name as the react app. \n[y/n]: ')
if create_git == 'y': 
  is_public = input('Do you want to make your repository public? \n[y/n]: ')

print(colored("Please wait... I'm generating your app...", 'green'))

print('-' * 25)

create_react_app(react_app_name + '-react', creation_mode)
remove_default_files()

if create_git == 'y':
  is_public = True if is_public == 'y' else False
  git_connection(react_app_name + '-react', is_public)
  print('-' * 25) 
  username = os.popen('git config user.name').read().replace("\n", "")
  print("Your repository is ready to use!")
  print("Access your repository on:", colored(f"https://github.com/{username}/{react_app_name}-react", 'green'))

print(colored("ALL DONE!", 'green'))
after_creation(after_creation_mode)