from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'username'
passwordStr = 'password'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()


password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'password')))
password.send_keys(passwordStr)
 
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()