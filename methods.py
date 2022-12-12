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
  