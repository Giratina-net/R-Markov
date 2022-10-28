import schedule
from time import sleep
import ferrg
ferrg.run()
def task():
    ferrg.run()
schedule.every(30).minutes.do(task)
while True:
    schedule.run_pending()
    sleep(1)