# # import time
# # from selenium.webdriver.support.ui import Select
# #
# # class AddCustomer:
# #     lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
# #     lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
# #     btnAddnew_Xpath = "//a[@class='btn btn-back-top bg-teal']"
# #     txtEmail_Xpath ="//input[@id='Email']"
# #     txtPassword_Xpath = "//input[@id='Password']"
# #     txtFirstName_Xpath = "//input[@id='FirstName']"
# #     txtLastName_Xpath = "//input[@id='LastName']"
# #     rdMaleGender_id = "//input[@id='Gender_Male']"
# #     rdFeMaleGender_id = "//input[@id='Gender_Female']"
# #     txtCompanyName_Xpath = "//input[@id='Company']"
# #     chkboxtax_Xpath = "//input[@id='IsTaxExempt']"
# #     Newsletter_Xpath = "//span[@class='select2 select2-container select2-container--default select2-container--below select2-container--focus']//span[@role='combobox']"
# #     txtcustomerRoles_Xpath = "(//div[@class='select2-blue'][1])[2]"
# #     lstitemAdministrators_Xpath = "//li[@title='Administrators']"
# #     lsttitForum_Xpath = "//li[@title='Forum Moderators']"
# #     lstitemRegistered_Xpath = "//li[@title='Registered']"
# #     lstitemAGuests_Xpath ="//li[@title='Guests']"
# #     lstitemVendors_Xpath ="//li[@title='Vendors']"
# #     drpmgrOfVendor_Xpath = "//select[@id='VendorId']"
# #     Active_Xpath = "//input[@id='Active']"
# #     Customchpw_Xpath = "//input[@id='MustChangePassword']"
# #     txtAdminContent_Xpath = "//textarea[@id='AdminComment']"
# #     btnSave_Xpath  = "//button[@name='save']"
# #
# #     def __init__(self, driver):
# #         self.driver = driver
# #
# #     def clickOnCustomersMenu(self):
# #         self.driver.find_element_by_Xpath(self.lnkCustomers_menu_xpath).click()
# #
# #     def clickOnCustomersMenuItem(self):
# #         self.driver.find_element_by_Xpath(self.lnkCustomers_menuitem_xpath).click()
# #
# #     def clickOnAddnew(self):
# #         self.driver.find_element_by_Xpath(self.btnAddnew_Xpath).click()
# #
# #     def setEmail(self,email):
# #         self.driver.find_element_by_Xpath(self.txtEmail_Xpath).send_keys(email)
# #
# #     def setPassword(self,password):
# #         self.driver.find_element_by_Xpath(self.txtPassword_Xpath).send_keys(password)
# #
# #     def setCustomerRoles(self, role):
# #         self.driver.find_element_by_Xpath(self.txtcustomerRoles_Xpath).click()
# #         time.sleep(5)
# #         if role == 'Registered' :
# #             self.listitem = self.driver.find_element_by_Xpath(self.lstitemRegistered_Xpath)
# #
# #         elif role == 'Administrators' :
# #             self.listitem = self.driver.find_element_by_Xpath(self.lstitemAdministrators_Xpath)
# #
# #         elif role == 'Guests' :
# #             time.sleep(5)
# #             self.driver.find_element_by_Xpath("(//span[@role='presentation'])[1]").click()
# #             self.listitem = self.driver.find_element_by_Xpath(self.lstitemAGuests_Xpath)
# #         elif role == 'Registered':
# #             self.listitem = self.driver.find_element_by_Xpath(self.lstitemRegistered_Xpath)
# #         elif role == 'Vendors':
# #             self.listitem = self.driver.find_element_by_Xpath(self.lstitemVendors_Xpath)
# #         else:
# #             self.listitem = self.driver.find_element_by_Xpath(self.lstitemAGuests_Xpath)
# #         time.sleep(6)
# #         #self.listitem.click()
# #         self.driver.execute_script("arguments[0].click();", self.listitem)
# #
# #     def setManagerOfVendor(self,value):
# #         drp=Select(self.driver.find_element_by_Xpath(self.drpmgrOfVendor_Xpath))
# #         drp.select_by_visible_text(value)
# #
# #     def setGender(self,gender):
# #         if gender=='Male':
# #             self.driver.find_element_by_id(self.rdMaleGender_id).click()
# #         elif gender=='Female':
# #             self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
# #         else:
# #             self.driver.find_element_by_id(self.rdMaleGender_id).click()
# #
# #     def setFirstName(self, fname):
# #         self.driver.find_element_by_Xpath(self.txtFirstName_Xpath).send_keys(fname)
# #
# #     def setLastName(self, lname):
# #         self.driver.find_element_by_Xpath(self.txtLastName_Xpath).send_keys(lname)
# #
# #     def setCompanyName(self, comname):
# #         self.driver.find_element_by_Xpath(self.txtCompanyName_Xpath).send_keys(comname)
# #
# #     def setAdminContent(self, content):
# #         self.driver.find_element_by_Xpath(self.txtAdminContent_Xpath).send_keys(content)
# #
# #     def clicOnSave(self):
# #         self.driver.find_element_by_Xpath(self.btnSave_Xpath).click()
#
# #Chatgpt
#
# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class AddCustomer:
#     lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
#     lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
#     btnAddnew_xpath = "//a[normalize-space()='Add new']"
#     txtEmail_xpath = "//input[@id='Email']"
#     txtPassword_xpath = "//input[@id='Password']"
#     txtFirstName_xpath = "//input[@id='FirstName']"
#     txtLastName_xpath = "//input[@id='LastName']"
#     rdMaleGender_xpath = "//input[@id='Gender_Male']"
#     rdFeMaleGender_xpath = "//input[@id='Gender_Female']"
#     txtCompanyName_xpath = "//input[@id='Company']"
#     chkboxtax_xpath = "//input[@id='IsTaxExempt']"
#     Newsletter_xpath = "//span[@class='select2 select2-container select2-container--default select2-container--below select2-container--focus']//span[@role='combobox']"
#     txtcustomerRoles_xpath = "(//div[@class='select2-blue'][1])[2]"
#     lstitemAdministrators_xpath = "//li[@title='Administrators']"
#     lsttitForum_xpath = "//li[@title='Forum Moderators']"
#     lstitemRegistered_xpath = "//li[@title='Registered']"
#     lstitemGuests_xpath = "//li[@title='Guests']"
#     lstitemVendors_xpath = "//li[@title='Vendors']"
#     drpmgrOfVendor_xpath = "//select[@id='VendorId']"
#     Active_xpath = "//input[@id='Active']"
#     Customchpw_xpath = "//input[@id='MustChangePassword']"
#     txtAdminContent_xpath = "//textarea[@id='AdminComment']"
#     btnSave_xpath = "//button[@name='save']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def clickOnCustomersMenu(self):
#         self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
#
#     def clickOnCustomersMenuItem(self):
#         self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
#
#     def clickOnAddnew(self):
#         try:
#             # Wait until button is clickable
#             add_btn = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, self.btnAddnew_xpath))
#             )
#             add_btn.click()
#         except:
#             # Fallback to JS click if normal click fails
#             add_btn = self.driver.find_element(By.XPATH, self.btnAddnew_xpath)
#             self.driver.execute_script("arguments[0].click();", add_btn)
#
#     def setEmail(self, email):
#         email_field = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, self.txtEmail_xpath))
#         )
#         email_field.send_keys(email)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)
#
#     def setCustomerRoles(self, role):
#         self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
#         time.sleep(2)
#
#         # if role == 'Registered':
#         #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
#         # elif role == 'Administrators':
#         #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
#         # elif role == 'Guests':
#         #     time.sleep(1)
#         #     self.driver.find_element(By.XPATH, "(//span[@role='presentation'])[1]").click()
#         #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
#         # elif role == 'Vendors':
#         #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
#         # else:
#         #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
#         #
#         # time.sleep(1)
#         # self.driver.execute_script("arguments[0].click();", self.listitem)
#
#     def setCustomerRoles(self, role):
#         # Click to open the customer roles dropdown
#         self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
#
#         # Wait for the dropdown options to be visible
#         role_xpath = f"//li[contains(text(), '{role}')]"
#         role_element = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, role_xpath))
#         )
#
#         # Before selecting 'Guests', remove 'Registered' if already selected
#         if role == "Guests":
#             try:
#                 registered = self.driver.find_element(By.XPATH,"//span[@title='delete' and preceding-sibling::span[text()='Registered']]")
#                 registered.click()
#             except:
#                 pass
#
#         # Click the role
#         self.driver.execute_script("arguments[0].click();", role_element)
#
#     def setManagerOfVendor(self, value):
#         drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
#         drp.select_by_visible_text(value)
#
#     # def setGender(self, gender):
#     #     if gender == 'Male':
#     #         self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
#     #     elif gender == 'Female':
#     #         self.driver.find_element(By.XPATH, self.rdFeMaleGender_xpath).click()
#     #     else:
#     #         self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
#     def setGender(self, gender):
#         if gender == 'Male':
#             gender_xpath = self.rdMaleGender_xpath
#         elif gender == 'Female':
#             gender_xpath = self.rdFeMaleGender_xpath
#         else:
#             gender_xpath = self.rdMaleGender_xpath
#
#         gender_element = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, gender_xpath))
#         )
#         try:
#             gender_element.click()
#         except:
#             self.driver.execute_script("arguments[0].click();", gender_element)
#
#     def setFirstName(self, fname):
#         self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)
#
#     def setLastName(self, lname):
#         self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)
#
#     def setCompanyName(self, comname):
#         self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)
#
#     def setAdminContent(self, content):
#         self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)
#
#     def clickOnSave(self):
#         save_btn = self.driver.find_element(By.XPATH, self.btnSave_xpath)
#         self.driver.execute_script("arguments[0].click();", save_btn)
#
#         self.ac.clickOnSave()
#         time.sleep(2)
#
#         # ✅ Validation should be here, not in Page Object
#         msg = self.driver.find_element(By.TAG_NAME, "body").text
#         print("Page message:", msg)
#
#         assert "The new customer has been added successfully." in msg, \
#             f"Customer creation failed! Got message: {msg}"
#
# # import pytest
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
#
# # 🔹 import your Page Object
# # import time
# # from selenium.webdriver.support.ui import Select
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # class Test_003_AddCustomer:
# #     baseURL = "https://admin-demo.nopcommerce.com/login"
# #     username = "admin@yourstore.com"
# #     password = "admin"
# #
# #     def test_addCustomer(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.get(self.baseURL)
# #         self.driver.maximize_window()
# #
# #         # ---------- LOGIN ----------
# #         self.driver.find_element(By.ID, "Email").clear()
# #         self.driver.find_element(By.ID, "Email").send_keys(self.username)
# #         self.driver.find_element(By.ID, "Password").clear()
# #         self.driver.find_element(By.ID, "Password").send_keys(self.password)
# #         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
# #
# #         # ---------- NAVIGATE ----------
# #         addcust = AddCustomer(self.driver)
# #         addcust.clickOnCustomersMenu()
# #         addcust.clickOnCustomersMenuItem()
# #         addcust.clickOnAddnew()
# #
# #         # ---------- FILL FORM ----------
# #         email = "test_" + str(int(time.time())) + "@gmail.com"
# #         addcust.setEmail(email)
# #         addcust.setPassword("Test@123")
# #         addcust.setFirstName("John")
# #         addcust.setLastName("Doe")
# #         addcust.setGender("Male")
# #         addcust.setCompanyName("MyCompany")
# #         addcust.setCustomerRoles("Guests")
# #         addcust.setManagerOfVendor("Vendor 1")
# #         addcust.setAdminContent("This is a test customer")
# #
# #         # ---------- SAVE ----------
# #         addcust.clickOnSave()
# #
# #         # ---------- VERIFY ----------
# #         msg = WebDriverWait(self.driver, 10).until(
# #             EC.visibility_of_element_located((By.TAG_NAME, "body"))
# #         ).text
# #         assert "The new customer has been added successfully." in msg
# #
# #         self.driver.close()
# # import pytest
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # # 🔹 import your Page Object
# # from pageObjects.AddCustomer import AddCustomer   # make sure path is correct
# #
# # class Test_003_AddCustomer:
# #     baseURL = "https://admin-demo.nopcommerce.com/login"
# #     username = "admin@yourstore.com"
# #     password = "admin"
# #
# #     def test_addCustomer(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.get(self.baseURL)
# #         self.driver.maximize_window()
# #
# #         # ---------- LOGIN ----------
# #         self.driver.find_element(By.ID, "Email").clear()
# #         self.driver.find_element(By.ID, "Email").send_keys(self.username)
# #         self.driver.find_element(By.ID, "Password").clear()
# #         self.driver.find_element(By.ID, "Password").send_keys(self.password)
# #         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
# #
# #         # ---------- NAVIGATE ----------
# #         addcust = AddCustomer(self.driver)
# #         addcust.clickOnCustomersMenu()
# #         addcust.clickOnCustomersMenuItem()
# #         addcust.clickOnAddnew()
# #
# #         # ---------- FILL FORM ----------
# #         email = "test_" + str(int(time.time())) + "@gmail.com"
# #         addcust.setEmail(email)
# #         addcust.setPassword("Test@123")
# #         addcust.setFirstName("John")
# #         addcust.setLastName("Doe")
# #         addcust.setGender("Male")
# #         addcust.setCompanyName("MyCompany")
# #         addcust.setCustomerRoles("Guests")
# #         addcust.setManagerOfVendor("Vendor 1")
# #         addcust.setAdminContent("This is a test customer")
# #
# #         # ---------- SAVE ----------
# #         addcust.clickOnSave()
# #
# #         # ---------- VERIFY ----------
# #         msg = WebDriverWait(self.driver, 10).until(
# #             EC.visibility_of_element_located((By.TAG_NAME, "body"))
# #         ).text
# #         assert "The new customer has been added successfully." in msg
# #
# #         self.driver.close()

import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkboxtax_xpath = "//input[@id='IsTaxExempt']"
    Newsletter_xpath = "//span[@class='select2 select2-container select2-container--default select2-container--below select2-container--focus']//span[@role='combobox']"
    txtcustomerRoles_xpath = "(//div[@class='select2-blue'][1])[2]"
    lstitemAdministrators_xpath = "//li[@title='Administrators']"
    lsttitForum_xpath = "//li[@title='Forum Moderators']"
    lstitemRegistered_xpath = "//li[@title='Registered']"
    lstitemGuests_xpath = "//li[@title='Guests']"
    lstitemVendors_xpath = "//li[@title='Vendors']"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    Active_xpath = "//input[@id='Active']"
    Customchpw_xpath = "//input[@id='MustChangePassword']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        try:
            add_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.btnAddnew_xpath))
            )
            add_btn.click()
        except:
            add_btn = self.driver.find_element(By.XPATH, self.btnAddnew_xpath)
            self.driver.execute_script("arguments[0].click();", add_btn)

    def setEmail(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txtEmail_xpath))
        )
        email_field.send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(2)

        role_xpath = f"//li[contains(text(), '{role}')]"
        role_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, role_xpath))
        )

        if role == "Guests":
            try:
                registered = self.driver.find_element(
                    By.XPATH,
                    "//span[@title='delete' and preceding-sibling::span[text()='Registered']]"
                )
                registered.click()
            except:
                pass

        self.driver.execute_script("arguments[0].click();", role_element)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            gender_xpath = self.rdMaleGender_xpath
        elif gender == 'Female':
            gender_xpath = self.rdFeMaleGender_xpath
        else:
            gender_xpath = self.rdMaleGender_xpath

        gender_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, gender_xpath))
        )
        try:
            gender_element.click()
        except:
            self.driver.execute_script("arguments[0].click();", gender_element)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        save_btn = self.driver.find_element(By.XPATH, self.btnSave_xpath)
        self.driver.execute_script("arguments[0].click();", save_btn)
