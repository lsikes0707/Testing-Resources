from selenium import webdriver
from selenium.webdriver.common.by import By

def test_wikipedia_homepage_title():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")
    assert "Wikipedia" in driver.title
    driver.quit()
