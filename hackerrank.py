from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
url = 'https://www.hackerrank.com/domains/data-structures?filtersBstatusDBD=unsolved&filtersBdifficultyDBD=medium&badge_type=problem-solving'
browser.get(url)

browser.find_element_by_xpath('//input[@value="medium"]').click()