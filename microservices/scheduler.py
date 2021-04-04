# Copyright 2021  CEPrE-Unilurio 

r""" Used to control CronTab to setup the time to launch and stop sertvices
"""
import os
from crontab import CronTab
from od.settings import common as od_config

python = f'{od_config.AI4CORAL_DIR}/venv/bin/python'
jobs = ['start_api', 'stop_api', 'start_frame_engine', 'stop_frame_engine']
MS_DIR = f'{od_config.AI4CORAL_DIR}/microservices'
cron = CronTab(user=True)

start_hour_on = od_config.START_TIME[0]
start_min_on = od_config.START_TIME[1]
stop_hour_on = od_config.STOP_TIME[0]
stop_min_on = od_config.STOP_TIME[1]

for job in cron:
  if job.comment in jobs:
      cron.remove(job)
      cron.write()

start_api = cron.new(command=f'{python} {MS_DIR}/service_ctl.py start --service ai4coral_api ', 
                      comment='start_api')

start_api.minute.on(start_min_on)
start_api.hour.on(start_hour_on)
print(start_api.is_valid())

stop_api = cron.new(command=f'{python} {MS_DIR}/service_ctl.py stop --service ai4coral_api', 
                      comment='stop_api')

stop_api.minute.on(stop_min_on)
stop_api.hour.on(stop_hour_on)
print(stop_api.is_valid())

start_fe = cron.new(command=f'{python} {MS_DIR}/service_ctl.py start --service frame_engine ', 
                      comment='start_frame_engine')

start_fe.minute.on(start_min_on)
start_fe.hour.on(start_hour_on)
print(start_fe.is_valid())

stop_fe = cron.new(command=f'{python} {MS_DIR}/service_ctl.py stop --service frame_engine', 
                    comment='stop_frame_engine')

stop_fe.minute.on(stop_min_on)
stop_fe.hour.on(stop_hour_on)
print(stop_fe.is_valid())

for job in cron:
  print(job)

cron.write()