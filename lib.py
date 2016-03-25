from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class Logger:
    '''
    Class for creating a Logging module.
    This module is used for logging debug information across modules.
    '''    
    def __init__(self):
        logging.basicConfig(filename='example.log', 
                           filemode='w', level=logging.DEBUG)
        logger = logging.getLogger(__name__)
 
   
class Driver:
    '''
	Class for handling the Drive connection, connecting to the url
	and cleanup of connection
    '''

    def __init__(self, browser):
       self.logger_handle = Logger()
       logging.info("inside the driver") 
       try:
           if browser == "Firefox":
               self.driver = webdriver.Firefox()
           elif browser == "Chrome":
               self.driver = webdriver.Chrome()
       except Exception as e:
           logger.info(e)

    def connect(self,url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

def login_gmail():
    browser_connect = Driver("Firefox")
    browser_connect.connect("http://gmail.com")
    element = WebDriverWait(browser_connect, 10).until(
        EC.presence_of_element_located((By.ID, "Email"))
    )
    element.send_keys("tanigai.dj@gmail.com")
    browser_connect.implicitly_wait(5)
    browser_connect.close()   


if __name__ == "__main__":
   print "Hello"
   login_gmail()
