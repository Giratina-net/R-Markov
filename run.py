import schedule
from time import sleep
import ferrg
import get
ferrg.run()
def task():
    ferrg.run()
def task2():
    get.run()
schedule.every(30).minutes.do(task)
schedule.every(1).day.do(task2)
while True:
    schedule.run_pending()
    sleep(1)