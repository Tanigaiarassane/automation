from selenium import webdriver
from common.setup_lib import connect_browser
from selenium.webdriver.common.action_chains import ActionChains
import time
URL_JQUERY_UI = "http://jqueryui.com/button/"
URL_AUTOMATION_PRACTICE = "http://automationpractice.com"
URL_TOOLS_QA = "http://toolsqa.com/automation-practice-form/"

def frame_demo():
    #print connect_browser().browser
    #browser = webdriver.Firefox()
    browser= connect_browser().browser
    browser.get(URL_JQUERY_UI)

    button_element = browser.find_element_by_xpath(".//*[@id='sidebar']/aside[2]/ul/li[3]/a")
    frame=browser.find_element_by_tag_name('iframe')
    browser.switch_to_frame(frame)
    button_default = browser.find_element_by_xpath("html/body/div/button")
    button_default.click()
    print (button_default.text)
    time.sleep(5)
    #browser.quit()
    #time.sleep(3)

def actions_menu():
    browser = connect_browser().browser
    browser.get("https://qatechnicals.wordpress.com/jmeter-learning-in-30-days/")
    element_1 = browser.find_element_by_xpath(".//*[@id='menu-item-754']/a")
    element_2 = browser.find_element_by_xpath(".//*[@id='menu-item-836']/a")
    menu = ActionChains(browser).move_to_element(element_1).move_to_element(element_2).click().perform()

    time.sleep(5)
    browser.quit()

def search_by_xpath():
    browser = connect_browser().browser
    xtag_val = ".//*[@id='sidebar']/aside[1]/ul/li[1]/a"
    find_by_xtag = {'xtag':{'url':'http://jqueryui.com/','value':xtag_val}}
    browser.get(find_by_xtag['xtag']['url'])
    element = browser.find_element_by_xpath(find_by_xtag['xtag']['value'])
    element.click()
    time.sleep(5)
    browser.quit()
    #browser.find_element_by_tag_name()

def search_by_class_name():
    CLASS_NAME="login"
    browser = connect_browser().browser
    browser.get(URL_AUTOMATION_PRACTICE)
    element = browser.find_element_by_class_name(CLASS_NAME)
    element.click()
    time.sleep(5)
    print browser.title
    browser.quit()

def search_by_id():
    ID = "search_query_top"
    browser = connect_browser().browser
    browser.get(URL_AUTOMATION_PRACTICE)
    element = browser.find_element_by_id(ID)
    element.click()
    print browser.title
    time.sleep(5)


def search_by_link_text():
    '''
    browser.find_element_by_partial_link_text()

    :return:
    '''
    browser = connect_browser().browser
    browser.get(URL)
    print URL
    element = browser.find_element_by_link_text("Draggable")
    element.click()
    print browser.title
    time.sleep(5)
    browser.quit()


def search_by_css_selector():
    browser = connect_browser().browser
    element = browser.find_element_by_css_selector()
    element.click()
    time.sleep(5)
    pass

if __name__ == "__main__":
    #frame_demo()
    #search_by_xpath()
    #search_by_link_text()
    #search_by_id()
    #search_by_class_name()
    actions_menu()
