from selenium import webdriver
chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')
assert 'Django' in browser.title