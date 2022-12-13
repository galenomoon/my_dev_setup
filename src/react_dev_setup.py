#!usr/bin/python3

import os
from termcolor import colored
from initializer import initialize
from methods import create_react_app, remove_default_files, git_connection, after_creation

class ReactDevSetup:

  def __init__(self):
    self.__run()

  def __run(self):
    initialize()

    print('Enter the name of the', colored('react app: ', 'green'), end='')
    react_app_name = input()

    # print('-' * 25)

    # creation_mode = input('Enter the creation mode: \n1) Default\n2) Custom\n[1/2]: ')

    print('-' * 25)

    after_creation_mode = input('After creation: \n1) Start app\n2) Open code\n3) Both\n4) None\n[1/2/3/4]: ')

    print('-' * 25)
    create_git = input('Create a repo to git? It will create a repo with the same name as the react app. \n[y/n]: ')
    if create_git == 'y': 
      is_public = input('Do you want to make your repository public? \n[y/n]: ')

    print(colored("Please wait... I'm generating your app...", 'green'))

    print('-' * 25)

    create_react_app(react_app_name + '-react')
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