from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events
import datetime

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')
register_events(scheduler)

# @register_job(scheduler, "interval", seconds=3)
# def my_job():
#     print('测试调度3秒一次,{}'.format(datetime.datetime.now()))

# scheduler.start()