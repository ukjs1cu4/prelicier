import re
import os
import schedule 
import subprocess
import time

def reza():
 output = subprocess.check_output("netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r | awk '$1>10'", shell=True)
 ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output )
 for i in ip:
  os.system('route add {} reject'.format(i))
  bantext = "ip : {} Banned".format(i)
  requests.get("https://api.telegram.org/bot1362187823:AAGgF6XgIJOW9pm9kqboV0l5q6QfHeJ8sw8/sendMessage?chat_id=650249840&text={}".format(bantext))
schedule.every(1).minutes.do(reza)
while True:
   schedule.run_pending()
   time.sleep(1)
