import requests
import urllib
import json
from typing import List, Dict
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os
import sys
import logging
import urllib3
import ssl
import subprocess
from filelock import FileLock, Timeout
import random
import time
import psutil
import tkinter as tk
from tkinter import simpledialog




def shutdown_script():
    try:
    
        os._exit(0)
    except Exception as e:
        logging.error(f"Error in shutting down script FUNCTION: {e}")
        time.sleep(1000)
        print(f"Error in shutting down script: {e}")


def delete_file(file_path):
    """Delete a file at the specified path."""
    try:
        os.remove(file_path)
    except Exception as e:
        pass
       

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, password, attachment_path):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Check if the attachment path is not empty
    if attachment_path:
        try:
            # Attach the file
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
                msg.attach(part)
                
            # Optionally delete the file after attaching it
            
        except Exception as e:
            print(f"Could not attach the file: {e}")
            return

    try:
        # Create a secure SSL context and connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)  # Login to the email account
            server.sendmail(sender_email, receiver_email, msg.as_string())
            # logging.info("Email Sent Successfully")
            delete_file(attachment_path)
    except Exception as e:
        print(f"Email Crash Error: {e}")
        shutdown_script()
        

def make_captcha_request(anchor,varChr,varVh,varBg,email,revemail,password):
    anchorr = str(anchor)
    anchorr = anchorr.strip()
    keysite = anchorr.split('k=')[1].split("&")[0]
    var_co = anchorr.split("co=")[1].split("&")[0]
    var_v = anchorr.split("v=")[1].split("&")[0]
    
    r1=''
    
    try:

        r1 = requests.get(anchorr).text
    except:
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r1 = requests.get(anchorr,verify=False).text
        except:
            try:
                headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                r1 = requests.get(anchorr,headers=headers,verify=False).text
                
            except Exception as e:
                #log error
                # logging.error(f"Error in making captcha request: {e}")
                
                shutdown_script()
                    
                    
                
                
            
            
            
            

    token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]

    var_chr = str(varChr)
    var_vh = str(varVh)
    var_bg = str(varBg)
    var_chr = str(urllib.parse.quote(var_chr))
    

    payload = {
        "v":var_v,
        "reason":"q",
        "c":token1,
        "k":keysite,
        "co":var_co,
        "hl":"en",
        "size":"invisible",
        "chr":var_chr,
        "vh":var_vh,
        "bg":var_bg
    }
    try:
        r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload)
    except:
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload,verify=False)
        except:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
                r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload,headers=headers,verify=False)
            except Exception as e:
                #log error
                # logging.error(f"Error in making captcha request: {e}")
                
                shutdown_script()
        
        
        
    try:
        token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
    except:
        token2 = 'null'

    if token2 == "null":
        
        

        return 'Failed'
        
        
    else:
       
       
        returnanchor=anchorr
        returnrelod=f"https://www.google.com/recaptcha/api2/reload?k={keysite}"
        returnpayload=f"v={var_v}&reason=q&c=<token>&k={keysite}&co={var_co}&hl=en&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}"
            
        return returnanchor,returnrelod,returnpayload
    
    
def generateresponse(anchorurl, reloadurl, payload,email,receveemail,password):
    s = requests.Session( )
    try:
    
        r1 = s.get(anchorurl).text
    except:
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r1 = s.get(anchorurl,verify=False).text
        except:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
                r1 = s.get(anchorurl,headers=headers,verify=False).text
            except Exception as e:
                #log error
                
                # logging.error(f"Error in generating response token: {e}")
                
                shutdown_script()
                
    token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]
    payload = payload.replace("<token>", str(token1))
    
    try:
        
        r2 = s.post(reloadurl, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})
    except:
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r2 = s.post(reloadurl, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"},verify=False)
        except:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
                r2 = s.post(reloadurl, data=payload, headers=headers,verify=False)
            except Exception as e:
                #log error
                # logging.error(f"Error in generating response token: {e}")
                
                shutdown_script()
    
    
    
    
    try:
        token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
        return token2
    except:
        
        shutdown_script()
        
        
def clean_payment_data(payment_data):
    # Fields to keep
    fields_to_keep = {
        'receiptNum': 'Receipt #',
        'paymentDateTime': 'Payment Date',
        'fullNameJewish': 'Donor Jewish Name',
        'createdDate': 'Created Date & Time',
        'amount': 'Amount',
        'paymentType': 'Payment Type',
        'approval': 'Approval',
        'refNum': 'Ref #',
        'paymentStatus': 'Status',
        'scheduleNum': 'Schedule #',
        'scheduleInfo': 'Schedule Info',
        'note': 'NOTE',
        'sourceTypeId': 'Source',
        'accountNum': 'Account #',
        'fullName': 'Donor English Name',
        'address': 'Address',
        'cityStateZip': 'City State Zip',
        'defaultPhone': 'Phone Number',
        'emailAddresses': 'Email',
        'pledgePayment': 'Amount applied',
        'currencyAmount': 'Currency Amount',
        'gatewayBatchNum': 'Gateway Batch #'
    }

    # Clean the data
    cleaned_data = []
    for payment in payment_data:
        cleaned_payment = {new_key: payment[old_key] for old_key, new_key in fields_to_keep.items() if old_key in payment}
        cleaned_data.append(cleaned_payment)

    return cleaned_data


    
def login_function(email,password,response_token,sendemail,receveemail,sendpassword):
# API URL
    url = "https://webapi.donary.com/v2/authentication/login"

    # Payload for login, replace with actual email, password, and generated reCAPTCHA token
    payload = {
        "email":email ,
        "password": password,
        "recapcha": response_token  
    }

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Make the POST request
    
    try:
    
        response3 = requests.post(url, json=payload, headers=headers)
    except:
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response3 = requests.post(url, json=payload, headers=headers,verify=False)
        except:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
                response3 = requests.post(url, json=payload, headers=headers,verify=False)
            except Exception as e:
                #log error
                logging.error(f"Error in login function: {e}")
                
                shutdown_script()

    # Check the response status and content
    if response3.status_code == 200:
        
        return response3  # This will show the server's response4
    
   
    else:
        
        return 'Failed'
        # Print the error message from the server
        

def get_items(login_response,eventuid):

    url = "https://webapi.donary.com/v1/paymenttransaction/GetPaymentTrans"
    today_date = datetime.now().strftime('%Y-%m-%d')

    payload = {
        "eventGuId": str(eventuid),
        "fromDate": today_date,
        "toDate": today_date,
    }

    # Define the headers, including the Bearer token
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {login_response.json()['accessToken']} "
    }
    

    # Send the POST request to fetch the transactions
    try:
    
        response = requests.post(url, headers=headers, json=payload)
    except:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response= requests.post(url, headers=headers, json=payload,verify=False)
        

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON data
        transactions = response.json()
        
        # Process the transactions data as needed
        return transactions  # Pretty print the JSON data
    
    elif response.status_code == 204:
        return "Noc"
    else:
        
        return 'Failed'
        
        
        
def filter_transactions_by_payment_type(transactions, payment_types):
    """
    Filters a list of transactions based on the payment types.

    :param transactions: List of transaction dictionaries.
    :param payment_types: A list of payment types to filter by (e.g., ['Cash', 'Pledger']).
    :return: List of transactions that match the specified payment types.
    """
    filtered_transactions = [
        transaction for transaction in transactions 
        if transaction.get('paymentType') in payment_types
    ]
    
    return filtered_transactions

def make_excell(data):
    if len(data) == 0:
        data={"ERROR":"PLEASE CHECK SCRIPT"}
        
    
    t_date = datetime.now().strftime('%Y-%m-%d')
    file_path = f"ScrapData_for_Date_{t_date}_{random.randint(100, 999)}.xlsx"  # Modify the filename format
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    return file_path  

def restart_script(scheduler):
    

    try:
        scheduler.remove_all_jobs()
        subprocess.Popen([sys.executable] + sys.argv)
    except Exception as e:
        logging.error(f"!!!!!!!Failed to restart script !!!!!!!: {e}")
        time.sleep(1000)
    finally:
        sys.exit()
        
    
    
  
CONFIG_FILE = 'scrapconfig.json'

def get_user_inputs():
    root = tk.Tk()
    root.withdraw()
    email =  simpledialog.askstring("Input", "Enter your SendingEmail:")
    
   
    
    password =  simpledialog.askstring("Input", "Enter your Sending Email Password:")
    receveemail = simpledialog.askstring("Input", "Enter your Receving Email:")
    accountemail = simpledialog.askstring("Input", "Enter your Donary Account Email:")
    accountlogin =   simpledialog.askstring("Input", "Enter your Donary Account Password:")
   
    eventuid= simpledialog.askstring("Input", "Enter your Donary Account EventUID:")
    
    # Save inputs to a config file
    with open(CONFIG_FILE, 'w') as f:
        json.dump({
            'email': email,
            'password': password,
            'receveemail': receveemail,
            'accountemail': accountemail,
            'accountlogin': accountlogin,
            'eventuid': eventuid,
            'lastsent': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }, f)
    root.destroy()
      

def update_last_sent():
    # Update the last sent timestamp in the config file
    data = load_user_inputs()
    if data:
        data['lastsent'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f)
    else:
        print("No user inputs found!")
        
def calculate_time_difference():
    # Calculate the time difference between the last sent timestamp and the current time
    data = load_user_inputs()
    if data:
        last_sent = datetime.strptime(data['lastsent'], '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()
        time_difference = current_time - last_sent
        return time_difference.total_seconds() / 60  # Return the time difference in minutes
    else:
        return None
  

def load_user_inputs():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            data = f.read().strip()  # Read and strip any extra whitespace
            if data:  # Check if the file has data
                return json.loads(data)  # Parse and return the JSON data
            else:
                return None  # Return None if the file is empty
    else:
        return None
    

def get_data():
    
    user_inputs=load_user_inputs() 
    if user_inputs is None:
   
    
        get_user_inputs()
        user_inputs=load_user_inputs() 
        
        email = user_inputs['email']
        
        password = user_inputs['password']
        receveemail = user_inputs['receveemail']
        accountemail = user_inputs['accountemail']
        accountlogin = user_inputs['accountlogin']
        eventuid = user_inputs['eventuid']
        
    else:
        
        email = user_inputs['email']
        
        
        password = user_inputs['password']
        receveemail = user_inputs['receveemail']
        accountemail = user_inputs['accountemail']
        accountlogin = user_inputs['accountlogin']
        eventuid = user_inputs['eventuid']
        
    
    try:
        logging.info("Get data` function is starting...")
        
        
        
        
        
        requrement1='https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Le5HB8qAAAAACVrDjBtWwnN3Ry5W1zCoV8EZoCj&co=aHR0cHM6Ly9wLmRvbmFyeS5jb206NDQz&hl=en&v=EGbODne6buzpTnWrrBprcfAY&size=invisible&cb=mqhzibkq69xi'
        
        req2='6009931042'
        
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
            
        
        logging.info("Middle")
    

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
            
            logging.info("Finished Sending Data")
            update_last_sent()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        shutdown_script()

    
    
    