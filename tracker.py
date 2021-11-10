import os
import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Uncomment to auto install driver 
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome('F:/Programs/WebDrivers/Chrome/chromedriver.exe')
token = '<Your Telegram Bot token here>'
chat_id = '<Your Telegram Bot chat ID here>'
api_url = 'https://api.telegram.org/bot'+token+'/sendMessage'+'?chat_id='+chat_id+'&text='

driver.get('https://web.whatsapp.com')
time.sleep(10) 

'''
1. Scan Your QR code
2. Open person's chat that you want to track
3. Once Done press Enter
'''

input('Ready to Start Track')

ONLINE_STATUS_LABEL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'
status = 'off'

def alert_telegram(log):
    requests.get(api_url + log )

def check_status():
    try:
        driver.find_element_by_xpath(ONLINE_STATUS_LABEL)
        print('Online')
        return True
    except:
        print('Offline')
        return False
  
def calculate_time(t):
    if t < 60:
        return(str(t)+' s')
    else:
        return(str(t // 60)+' m')
    
while(True):
    if check_status() and status == 'off':
        alert_telegram('==========================')
        alert_telegram('Came Online')
        time_1 = time.time()
        status = 'on'
    if not check_status() and status == 'on':
        time_2 = time.time()
        time_interval = time_2 - time_1
        alert_telegram('Session Time : '+ calculate_time(int(time_interval)))
        alert_telegram('Went Offline')
        alert_telegram('==========================')
        status = 'off'
        


    
    


