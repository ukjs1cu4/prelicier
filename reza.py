import requests
import re
import os
import schedule 
import subprocess
import time

def reza():
 output = subprocess.check_output("netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r | awk '$1>100'", shell=True)
 if re.findall( r'[0-9]+(?:\.[0-9]+){3}', output ):
  ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output )
  for i in ip:
   os.system('route add {} reject'.format(i))
   bantext = "ip : {} Banned".format(i)
   requests.get("https://api.telegram.org/bot1307189716:AAFACx24JGHM8runYguxFyOQr3LggDjW17E/sendMessage?chat_id=650249840&text={}".format(bantext))
 else:
  reza = "khar"
schedule.every(30).seconds.do(reza)
while True:
   schedule.run_pending()
   time.sleep(1)
