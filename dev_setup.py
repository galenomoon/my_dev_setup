#/usr/bin/python3
import os
import sys
from initializer import application_helper

if sys.argv[1] == "--react":
  os.system("python3 react_dev_setup.py")
elif sys.argv[1] == "--git-config":
  os.system("python3 git_config.py")
elif sys.argv[1] == "--install-requirements":
  os.system("pip3 install -r requirements.txt")
elif sys.argv[1] == "--help":
  application_helper()
else:
  print("Invalid argument! Try again. Use --help to see the options.")