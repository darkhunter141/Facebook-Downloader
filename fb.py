# -*- coding: utf-8 -*-
import sys
import os
import re,time
import requests as r
import wget
os.system('clear')
def bannar():
  print ('''\033[95m
    ____                      __                __
   / __ \____ _      ______  / /___  ____ _____/ /
  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / 
 / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  
/_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/   ''')
  print ('''\033[94m
    __  ___           __           
   /  |/  /___ ______/ /____  _____
  / /|_/ / __ `/ ___/ __/ _ \/ ___/
 / /  / / /_/ (__  ) /_/  __/ /    
/_/  /_/\__,_/____/\__/\___/_/    \033[93m Version : 1.0     
                                    
''')
  print ('\033[94m-'*50)
  print ('')
  print (' \033[96m Author   : \033[95m Dark Hunter 141')
  print ('')
  print (' \033[96m Tool     : \033[95m Facebook Downloader')
  print ('')
  print (' \033[96m Facebook : \033[95m https://www.facebook.com/darkhunter141/')
  print ('')
  print (' \033[96m Github   : \033[95m https://www.github.com/darkhunter141/')
  print ('')
  print (' \033[96m Coded By : \033[95m Dark Wolf , DarkXploit')
  print ('')
  print ('\033[94m-'*50)
  print ('')
  print ('             \033[0;37;41m Facebook Video Downloader \033[0m ' )
  print ('')
  print ('')
bannar()

filedir = os.path.join('file.mp4')
ERASE_LINE = '\x1b[2K'
hibabe=input("\033[92m [!] Paste Your FB Video Url : \033[93m ")

print ('')
print ('')
print( '\033[0;37;44m Options Menu  : \033[0m ' )
print ('')
print ('')
print ('\033[91m [\033[0m1\033[91m] \033[92m Download Video In SD Format\033[90m')
print ("")
print ('\033[91m [\033[0m✓\033[91m] \033[92m Download Video In HD Format\033[90m')
print ("")
print ("")
choice=input(str('\033[92m [!] Type Any Number : \033[93m '))
print ("")
print ("")
print ("\033[96m [✓] Downloading Video Please Wait..Its Depends On Your Network Speed.To Stop This Process CTRL + Z")
print ("\033[91m")
if choice=='1':
  try:
    LINK = hibabe
    html = r.get(LINK)
    sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
  except r.ConnectionError as e:
  
    print("OOPS!! Connection Error.")
    
  except r.Timeout as e:
    print("OOPS!! Timeout Error")
  except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")  
  except (KeyboardInterrupt,SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
  except TypeError:
    print("Video May Private or Hd version not avilable")  
  else:
    sd_url = sdvideo_url.replace('sd_src:"', '')
    print("\n")
    print("\033[92m [+]Normal Quality:\033[93m " + sd_url)
    print("[+] Video Started Downloading")
    wget.download(sd_url, filedir)
    sys.stdout.write(ERASE_LINE)
    print("\n")
    print("Video downloaded")
    os.system('termux-setup-storage')
    os.system('mv file.mp4 /sdcard')
    print ('File Save As file.mp4 in Your Sdcard.')
    print ('Cheack Your Sdcard')
    print ('Good Bye ')
if choice=='2':
  try:
    print ("\033[91m")
    LINK = hibabe

    html = r.get(LINK)
    hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
  except r.ConnectionError as e:
  
    print("OOPS!! Connection Error.")
  except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")  
  except (KeyboardInterrupt,SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
  except TypeError:
    print("Video May Private or Hd version not avilable")    
  except r.Timeout as e:
    print("OOPS!! Timeout Error")
  else:
    hd_url = hdvideo_url.replace('hd_src:"', '')
    print("\n")
    print("\033[92m [+]Normal Quality:\033[93m " + hd_url)
    print("[+] Video Started Downloading")
    wget.download(hd_url, filedir)
    sys.stdout.write(ERASE_LINE)
    print("\n")
    print("Video downloaded")
    os.system('termux-setup-storage')
    os.system('mv file.mp4 /sdcard')
    print ('File Save As file.mp4 in Your Sdcard.')
    print ('Cheack Your Sdcard')
    print ('Good Bye ')
else:
  print ('\033[91mGood Bye')
  print ('Tnks For Using This Tool')
 
  
