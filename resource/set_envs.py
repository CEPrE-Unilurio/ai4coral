from pathlib import Path
from od.settings import common as od_config
import os

BASE_DIR = od_config.AI4CORAL_DIR
home = str(Path.home())
MS_DIR = f'{BASE_DIR}/microservices'
envs = {}

envs['PYTHONPATH'] = f'export PYTHONPATH={MS_DIR}:$PYTHONPATH\n'
envs['AI4CORAL_BASE'] = f'export AI4CORAL_BASE={od_config.AI4CORAL_DIR}\n' 

def export():
  try:
    os.system(f'cp {home}/.bashrc {home}/.bashrc.old')
    with open(f'{home}/.bashrc.old', 'r') as f:
      data = f.readlines()
    with open(f'{home}/.bashrc', 'w+') as bashrc:
      for line in data:
        for env in envs.keys():
          if line.__contains__(env):
            bashrc.write(envs[env])
            del envs[env]
            break
        else:
          bashrc.write(line)
      for env in envs.keys():
        bashrc.write(envs[env])
  except Exception as e:
    print('can not export')
    print(e)
    os.system(f'cp {home}/.bashrc.old {home}/.bashrc')

if __name__ == '__main__':
  export()