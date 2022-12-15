import argparse
import os
from git_config import GitConfig
from react_dev_setup import ReactDevSetup

class DevSetupCLI:
  CLI_VERSION = '0.1.3'
  
  def __init__(self):
    self.__run()
  
  def __run(self):
    self.parser = argparse.ArgumentParser(
      prog='dev_setup',
      description='Dev Setup CLI',
      epilog='Developed by: @galenomoon - https://github.com/galenomoon',
      usage='%(prog)s [options] [command] [command options]')
    self.parser.version = self.CLI_VERSION
    self.parser.add_argument('-v', '--version', action='version')
    self.parser.add_argument('-r', '--react', action='store_true', help='Setup React')
    self.parser.add_argument('-g', '--git-config', action='store_true', help='Setup Git Config')
    self.parser.add_argument('-i', '--install-requirements', action='store_true', help='Install Requirements')
    self.args = self.parser.parse_args()
  
    if self.args.react:
      ReactDevSetup()
    
    if self.args.git_config:
      GitConfig()
    
    if self.args.install_requirements:
      os.system("pip3 install -r src/requirements.txt")
    
    if not self.args.react and not self.args.git_config and not self.args.install_requirements:
      self.parser.print_help()