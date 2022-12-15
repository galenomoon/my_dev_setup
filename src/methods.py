import os
from dotenv import load_dotenv
from termcolor import colored
from templates.templates import Templates
import requests

def create_and_editing(filename, content):
  file = open(filename, '+w')
  file.write(content)
  file.close()

def create_default_files():
  create_and_editing('.env', 'REACT_APP_API_URL=http://localhost:3000')
  create_and_editing('.gitignore', '.env\n/node_modules')
  tailwind_setup()
  os.chdir('config')
  create_and_editing('api_client.js', Templates.api_client())
  
def install_libs():
  libs = ['axios', 'react-icons', 'react-hot-toast']
  for lib in libs:
    print (f"Installing ", colored(f"{lib}", 'green'))
    os.system(f"npm install {lib}")
  
def tailwind_setup():
  os.system('npm install -D tailwindcss postcss autoprefixer')
  os.system('npx tailwindcss init -p')
  create_and_editing('tailwind.config.js', Templates.tailwind_config())
  
  os.chdir('src')
  os.remove('index.css')
  create_and_editing('index.css', Templates.index_css())
  os.chdir('./')
  
def create_react_app(react_app_name, creation_mode = '1'):
  os.system('npx create-react-app '+ react_app_name)
  os.chdir(react_app_name)
  if creation_mode == '1':
    generate_default_template()
  if creation_mode == '2':
    generate_custom_template()
  create_default_files()
  
def generate_default_template():
  folders = ['components', 'pages', 'config', 'assets', 'routes', 'utils']
  for folder in folders:
    os.mkdir('src/' + folder)

def generate_custom_template():
  print('Work in progress 🚧')
  return

def after_creation(after_creation_mode):
  if after_creation_mode == '1' or after_creation_mode == '3':
    os.system('npm start')
  if after_creation_mode == '2' or after_creation_mode == '3':
    os.system('code .')

def remove_default_files():
  os.chdir('../')
  print('-' * 12)
  os.system('pwd')
  print('-' * 12)
  os.remove('App.js')
  create_and_editing('App.js', Templates.app_js())
  
  os.remove('index.js')
  create_and_editing('index.js', Templates.index_js())
  
  os.remove('App.css')
  os.remove('App.test.js')
  os.remove('logo.svg')
  os.remove('reportWebVitals.js')
  os.remove('setupTests.js')
  
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