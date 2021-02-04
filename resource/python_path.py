from pathlib import Path
import os

BASE_DIR = os.getcwd()
home = str(Path.home())
MS_DIR = f'{BASE_DIR}/microservices'
export = f'export PYTHONPATH={MS_DIR}:$PYTHONPATH'
already_exported = False

with open(f'{home}/.bashrc', 'w+') as bashrc:
  with open(f'{home}/.bashrc.back') as f:
    for line in f:
      if line == export:
        print(f'nothing to be done')
        bashrc.write(line)
        already_exported = True
      else:
        bashrc.write(line)  
    if not already_exported:
      print(f'adding {export}')
      bashrc.write(export)