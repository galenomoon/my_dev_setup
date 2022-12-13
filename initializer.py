from termcolor import colored

def initialize():
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

def application_helper():
  print('''
  Usage: python3 dev_setup.py [OPTION]

  Options:
    --react                      Create a react app
    --git-config                 Configure git
    --install-requirements       Install requirements
    --help                       Show this help
  ''')