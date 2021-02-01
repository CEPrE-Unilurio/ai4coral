from pathlib import Path
import os

BASE_DIR = os.getcwd()
home = str(Path.home())
OD_DIR = f'{BASE_DIR}/microservices/object_detection'
FE_DIR = f'{BASE_DIR}/microservices/frame_engine'
export = f'export PYTHONPATH={FE_DIR}:{OD_DIR}:$PYTHONPATH'
already_exported = False

with open(f'{home}/.bashrc', 'w+') as bashrc:
  with open(f'{home}/.bashrc.back') as f:
    for line in f:
      if line == export:
        print(f'changing {line} to {export}')
        bashrc.write(export)
        already_exported = True
      else:
        bashrc.write(line)  
    if not already_exported:
      print(f'adding {export}')
      bashrc.write(export)