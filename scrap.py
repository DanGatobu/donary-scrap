from functions import *
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pytz
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_inputs=load_user_inputs() 





if user_inputs is None:
    
    get_user_inputs()
    user_inputs=load_user_inputs() 
    logging.info("Starting....",user_inputs)
    email = user_inputs['email']
    
    password = user_inputs['password']
    receveemail = user_inputs['receveemail']
    accountemail = user_inputs['accountemail']
    accountlogin = user_inputs['accountlogin']
    eventuid = user_inputs['eventuid']
    
else:
    
    email = user_inputs['email']
    logging.info("Starting...",user_inputs)
    
    password = user_inputs['password']
    receveemail = user_inputs['receveemail']
    accountemail = user_inputs['accountemail']
    accountlogin = user_inputs['accountlogin']
    eventuid = user_inputs['eventuid']



def get_data():
    
    
    
    requrement1='https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Le5HB8qAAAAACVrDjBtWwnN3Ry5W1zCoV8EZoCj&co=aHR0cHM6Ly9wLmRvbmFyeS5jb206NDQz&hl=en&v=EGbODne6buzpTnWrrBprcfAY&size=invisible&cb=mqhzibkq69xi'
    
    req2=' 6009931042'
    
    req3='!XFqgWl8KAAQeBu1XbQEHewF3r1uHI2K6ioroh_8HdshF71OdCl_0vnUsr-qyUE10ZEWjb1fCAv0LouH4kuXjiiXDFrqSLfTtFreWo6uV426VFvd5MCviCasLbH2YDKGpv6jmLk7NF_wJIku84MwyGF2Cdxg4TBATPN50ZYOudlADShMS9CuXpKZ-VC45Ggs_JeDRga0qHGpmqyJAHzwl9BLSeCqieRgtMnSS7oDzJ5vN8jKBjKEHkAWKF-W7sZVQ5NlFATCkv61-poyB_6QqCmqBYGFF2NTikI6HNiR9A-JTwc3InKXygJFr5_vrddsFXrGRAX0no1SWeHUt7uT1juwraHeueD2dDKBkH22_D8coA12A-CfvtdOh1aEjIdWD7L9t3DksdYW5hjN6VoahPGdJctCc4mYQNUxuuCsX4ddzGONH-opywCM3Z_SKs866t7leSfRor9_nnc4tZqGUX118Ij5bIAb4evGrRbi8p1o0-YWNWdUPYU1rDCSXZPZB28i1ENZ11xTGnARUy77eogCECHFreyXShCjHp87rqwRwj0vDcvk6aRs9Xd1EouLwL1iegUh1-xjXIyjUu2zjwreTc7KpssIg0nEeoxMt1WhmKqo3AsC2iOy3ScvSv7Kwb5lKJaTzEcjcpcoHLWykk90J-C-Z1sEGaCFZ-VFZoSNLceWEKKVubS_iWPeHQGXkXHduMSc1osY4bLx6MoDc_4H8C6X8IxEUcYvRAqkAIoiTDsoYBBgFxOWFQ-E4bbfHz2_wnhBntUx3OWqxp4wWYSq6UTt79nNXHQ-r8WmWUd6_pxtV3fhnF3BrHJ8xJwn_46v6giTAzZyhWSm1_Cwbc2PO4G4l0LEk-g5z7Y333BlIXJ7v1O1wxRsJpFVVGBvKTt48rkMgvrsoiklkJoHRDunpYjuIVpQl-8eTbpK4eunQ6i-hTy5dkPDRCXHiQTnrNWOuEjNhIxfLK86jc1XdETdm5ZxLkAMQ7QcvF-V2FY_4AwLQhKeNWT0r80YYcX3qgMGF4UvW4EMWLGxjh5PIvuWUW40In9r-i48-vgmQe8xEY4kn8yhNhe9eWjYDf2U1Ibzqf2FCRta1gR0-zQhQa40yXW_xTrRR6kMJnb_5SSbZ8BGWr1O00RRNkoYOv5cBdNIZLq_586UsCMRCHt_Bfi8wy-lcBCskMnXsl-XGclOYJ7RN0NIKVsXQycvd6WuWSjKk7ET31XZtkSDL-3VRwx1qP8k4be23oY_NgG4kcd8XcnlvXbf5g0EnJJWxKFqQGc3eM9HpDKZrQzSodziPWXYVB96aLcPx7neaQ_XRlNKa8klHjJnqt1dAtfvMFzqEcAvW0i-PX0bzaoxvILlkMYLNPIucK5McUrxCI_OdpPHN6FJjDqfzjLhofVFYe9pdeSVKDJpz6uEoGSzcawFUXTVvN2_fWRFQ8Jr-0uOBMSgc8Rr2G1LJxbtz-EFzDv6xEbvQgaIWvQvwU9dR-QsJZe4A8kc7ciQ96chifCgaJ5tOdtbELddABgC9mVGwRGVQ_aXxvwm84F2PjkcyDI-LQMFqFxz36qaO28CQ-KhigujZE9w77_sBBKrbjtMKX-MADNYpYUQyHUI7eXAWIOtpOrFlSnaGwPOtJRO6ohhJbK2cUPevOva9QrVvnYPOOYkloXKlIZNhhCikHJRP_8k6361N0E3NCe_XewdhO1_XMydkAIL6BKNO1s_JzUrdo0fYlgZvgRoCuqTBilP-bwNXFh80IvsC9DH6AJwKt4fx3Qc3V0u8coxE8z9biHbD6KKCBP8pUfoZd9EnMEL1U-OB48lK1TENzy_u6_KsAKfOlD8oebo8NMiurlfhiRtkUHVrPT5qPxRC-iACQAU1THIwr7PNwTwXI3rmnxEk9riXYefT0nzaJ5X9v-hI0upcQ_t7TE6_laNh3Rto0B3ESRa5haT1QQol7NgquPH3h2LwGdPF4ncmNV04tZYb6R9WxHWJ7cA-xN1r1hZ9pFMbk9gIiQ*'
    
    if make_captcha_request(requrement1,'',req2,req3,email,receveemail,password)=='Failed':
        send_email(
        sender_email= email,
    receiver_email= receveemail,
    subject="Error Generating Captcha Data",
    body="Can't generate capcha response token update captcha make_captcha_request function",
    smtp_server="smtp.gmail.com",  
    smtp_port=587,  
    password=password,  
    attachment_path='')
        shutdown_script()
    else:
    
    
        anchorresult,reloadurlresult,payloadresult=make_captcha_request(requrement1,'',req2,req3,email,receveemail,password)
        
    

    respnsetoken=generateresponse(anchorresult,reloadurlresult,payloadresult,email,receveemail,password)
    
    if respnsetoken=='Failed':
        send_email(
        sender_email= email,
    receiver_email= receveemail,
    subject="Error Generating Captcha Response Token",
    body="Can't generate captcha response token update captcha bypass function",
    smtp_server="smtp.gmail.com",  
    smtp_port=587,  
    password=password,  
    attachment_path='')
        shutdown_script()
        
    
    
   

    login_response=login_function(str(accountemail),str(accountlogin),respnsetoken,email,receveemail,password)
    if login_response=='Failed':
        send_email(
        sender_email= email,
    receiver_email= receveemail,
    subject="Error In Daily File Script",
    body="Can't login",
    smtp_server="smtp.gmail.com",  # For Gmail
    smtp_port=587,  # For Gmail
    password=password,  # Use an app password if necessary
    attachment_path='')
        shutdown_script()

    
    transactions_results=get_items(login_response,eventuid)
    if transactions_results=='Failed':
        send_email(
    sender_email= email,
    receiver_email= receveemail,
    subject="Daily File Error" ,
    body="Could not get data check the get items function And restart the script",
    smtp_server="smtp.gmail.com",  # For Gmail
    smtp_port=587,  # For Gmail
    password=password,  # Use an app password if necessary
    attachment_path=''  # Replace with the path to your file
)
        shutdown_script()

    
    elif transactions_results=='Noc':
        send_email(
    sender_email= email,
    receiver_email= receveemail,
    subject="Daily File" ,
    body="No data Found Today",
    smtp_server="smtp.gmail.com",  # For Gmail
    smtp_port=587,  # For Gmail
    password=password,  # Use an app password if necessary
    attachment_path=''  # Replace with the path to your file
)
        
    else:
        
    
    
        Filtered_data=filter_transactions_by_payment_type(transactions_results['paymentTransGridModel'],['OJC','Pledger','Matbia','Credit Card'])
        Filtered_data=clean_payment_data(Filtered_data)
        filepath=make_excell(Filtered_data)
        
        
        
        
        
        send_email(
        sender_email= email,
        receiver_email= receveemail,
        subject="Daily File",
        body="A copy of the requested file",
        smtp_server="smtp.gmail.com",  # For Gmail
        smtp_port=587,  # For Gmail
        password=password,  
        attachment_path=filepath  
        
    )
        
        logging.info("Email Sent",datetime.now())
        update_last_sent()


def main():
    passed_time=calculate_time_difference()
    if passed_time>1440:
        get_data()
    
    scheduler = BlockingScheduler()

# Define the timezone for Eastern Standard Time (UTC-4)
    eastern = pytz.timezone('America/New_York')
    

# Schedule the job to run every day at 11:55 PM
    scheduler.add_job(get_data,trigger='cron', hour=23, minute=55, timezone=eastern,replace_existing=True)
    scheduler.add_job(restart_script, trigger='cron', hour=4, minute=20, timezone=eastern,replace_existing=True)
    
    
    scheduler.start()
    
if __name__ == '__main__':
    main()
    
