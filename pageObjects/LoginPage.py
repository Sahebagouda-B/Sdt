# class LoginPage:
#    textbox_username_id="Email"
#    textbox_password_id="Password"
#    button_login_xpath="//button[normalize-space()='Log in']"
#    link_logout_linktext="Logout"
#
#    def __init__(self,driver):
#       self.driver=driver
#
#    def setUserName(self,username):
#        self.driver.find_element_by_id(self.textbox_username_id).clear()
#        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
#
#    def setPassword(self,password):
#        self.driver.find_element_by_id(self.textbox_password_id).clear()
#        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
#
#    def clickLogin(self):
#        self.driver.find_element_by_xpath(self.button_login_xpath).click()
#
#    def clickLogout(self):
#        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_username_id))
        )
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_password_id))
        )
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        )
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and text()='Logout']"))
        )
        logout_btn.click()
