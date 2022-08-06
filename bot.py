from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class InstaFollower:
    def __init__(self):
        self.chrome_driver_path = "/Users/axel/Documents/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        
    def login(self, email, password):
        # Go to Instagram Login Page
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        
        # Provide email
        email_field = self.driver.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
        email_field.send_keys(email)
        
        # Provide password and submit
        password_field = self.driver.find_element_by_xpath("//input[@aria-label='Password']")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        
        # Dismiss pop-ups
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(2)
    
    def find_followers(self, account):
        # Go to target account page
        self.driver.get(f"https://www.instagram.com/{account}/")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text()=' followers']")))
        
        # Click on followers
        self.driver.find_element_by_xpath("//div[text()=' followers']").click()
        sleep(2)
        
        # Scroll down
        followers_popup = self.driver.find_element_by_class_name("_aano")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            sleep(2)
          
    def follow(self):
        follow_buttons = self.driver.find_elements_by_xpath("//ul/div/li/div/div/button")
        for button in follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath("//button[text()='Cancel']").click()