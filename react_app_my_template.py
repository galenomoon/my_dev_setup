import os

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
    generate_custom_template()
  
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
  
def git_init(reponame):
  os.system('git init')
  os.system('git add .')
  os.system('git commit -m "Initial commit"')
  os.system('git branch -M master')
  os.system('git remote add origin git@github.com:galenomoon/'+ reponame +'.git')
  os.system('git push -u origin master')

react_app_name = input('Enter the name of the react app: ')
creation_mode = input('Enter the creation mode: \n1) Default\n2) Custom\n[1/2]: ')
after_creation_mode = input('After creation: \n1) Start app\n2) Open code\n3) Both\n4) None\n[1/2/3/4]: ')
connect_git = input('Connect to git? [y/n]: ')

# ======================

create_react_app(react_app_name + '-react', creation_mode)
remove_default_files()

if connect_git == 'y':
  reponame = input('Enter the name of the repository: ')
  git_init(reponame)

after_creation(after_creation_mode)