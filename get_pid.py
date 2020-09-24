from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta
import csv

def get_pid(referred_by='self', business=''):
  if referred_by=='self':
    business = input("Enter Business Name: ")
  url = f'https://www.google.com/search?q={business}'
  pid_found = False

  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get(url)
  time.sleep(1)

  aaa = driver.find_elements_by_tag_name( "a" )

  for a in aaa:
    pid = a.get_attribute("data-pid")
    if pid!=None:
      print ("\nThe Business PID Is:",pid)
      pid_found=True
      break

  if pid_found == False:
    print ("No Business Or Multiple Businesses Found - Try Adding A Location To Be More Specific")
  

  driver.quit()
  return pid
