from selenium import webdriver
class browser_setup:
    def __init__(self):
        self.browser = webdriver.Firefox()

val = browser_setup()


def connect_browser():
    return val
