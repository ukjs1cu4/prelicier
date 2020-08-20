import requests
import re
import os
import schedule 
import subprocess
import time

#kirm dhnt reza :D
def reza():
 output = subprocess.check_output("netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r | awk '$1>50'", shell=True)
 if re.findall( r'[0-9]+(?:\.[0-9]+){3}', output ):
  ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output )
  for i in ip:
   os.system('route add {} reject'.format(i))
   bantext = "ip : {} Banned".format(i)
   requests.get("https://api.telegram.org/bot1090278340:AAG_76X95gTm-Iry2VBOxIpXhYHa3XriNMs/sendMessage?chat_id=650249840&text={}".format(bantext))
 else:
  reza = "khar"
schedule.every(30).seconds.do(reza)
while True:
   schedule.run_pending()
   time.sleep(1)
