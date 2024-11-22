from functions import *
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pytz
import logging





log_file_path = os.path.join(os.getcwd(), 'app_log.txt')
logging.basicConfig(filename=log_file_path,
                    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')












    



def main():
    passed_time=calculate_time_difference()
    if passed_time>3:
        get_data()



    
    
    scheduler = BlockingScheduler()

# Define the timezone for Eastern Standard Time (UTC-4)
    eastern = pytz.timezone('America/New_York')
    

# Schedule the job to run every day at 11:55 PM
    # scheduler.add_job(get_data,trigger='cron', hour=23, minute=55, timezone=eastern,replace_existing=True)
    # scheduler.add_job(restart_script, trigger='cron', hour=4, minute=20, timezone=eastern,replace_existing=True)
    
    scheduler.add_job(get_data,trigger='interval', minutes=1, replace_existing=True)
    scheduler.add_job(restart_script, trigger='interval', minutes=5, replace_existing=True,args=[scheduler])
    
    
    scheduler.start()
    
if __name__ == '__main__':
    main()
    
