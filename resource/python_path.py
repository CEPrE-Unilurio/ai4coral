from pathlib import Path
import os

BASE_DIR = os.getcwd()
home = str(Path.home())
MS_DIR = f'{BASE_DIR}/microservices'
env = f'export PYTHONPATH={MS_DIR}:$PYTHONPATH\n'

def export():
  already_exported = False
  try:
    os.system(f'cp {home}/.bashrc {home}/.bashrc.old')
    with open(f'{home}/.bashrc.old', 'r') as f:
      data = f.readlines()
    with open(f'{home}/.bashrc', 'w+') as bashrc:
      for line in data:
        if line == env:
          print(f'nothing to be done')
          bashrc.write(line)
          already_exported = True
        else:
          bashrc.write(line)  
      if not already_exported:
        print(f'adding {env}')
        bashrc.write(env)
  except Exception as e:
    print('can not export')
    print(e)
    os.system(f'cp {home}/.bashrc.old {home}/.bashrc')

if __name__ == '__main__':
  export()