# from sys import flags
#
# from selenium.webdriver.common.by import By
# class SearchCustomer :
#     txtEmail_id ="SearchEmail"
#     txtFirstName_id ="SearchFirstName"
#     txtLastName_id ="SearchLastName"
#     btnSearch_id ="search-customers"
#
#     tblSearchResults_xpath="//table[@id='customers-grid']"
#     table_Xpath ="//table[@id='customers-grid']"
#     tableRows_Xpath =""
#     tableColumns_Xpath ="//table[@id='customers-grid']//tbody/tr"
#     tableColumns_Xpath ="//table[@id='customers-grid']//tbody/tr/td"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setEmail(self, email):
#         self.driver.find_element(By.ID,self.txtEmail_id).clear()
#         self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)
#
#     def setFirstName(self, fname):
#         self.driver.find_element(By.ID, self.txtEmail_id).clear()
#         self.driver.find_element(By.ID, self.txtEmail_id).send_keys(fname)
#
#     def setLastName(self, lname):
#         self.driver.find_element(By.ID, self.txtEmail_id).clear()
#         self.driver.find_element(By.ID, self.txtEmail_id).send_keys(lname)
#
#     def clickSearch(self):
#         self.driver.find_element(By.ID, self.btnSearch_id).click()
#
#     def getNoOfRows(self):
#         return len(self.driver.find_element(By.XPATH,self.tableRows_Xpath))
#
#     def getNoOfColumns(self):
#         return len(self.driver.find_element(By.XPATH,self.tableColumns_Xpath))
#
#     def SearchCustomerByEmail(self,email):
#         flag=False
#         for r in range(1,self.getNoOfRows()+1):
#             table=self.driver.find_element(By.XPATH,self.table_Xpath)
#             emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
#             if emailid == email:
#                 flag = True
#                 break
#         return flag
#
#     def SearchCustomerByName(self,Name):
#         flag=False
#         for r in range(1,self.getNoOfRows()+1):
#             table=self.driver.find_element(By.XPATH,self.table_Xpath)
#             name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
#             if name == Name:
#                 flag = True
#                 break
#         return flag
from selenium.webdriver.common.by import By

class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    table_Xpath = "//table[@id='customers-grid']"
    tableRows_Xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_Xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_Xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_Xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            emailid = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[2]"
            ).text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):  # 👈 lowercase s
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            name_value = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[3]"
            ).text
            if name_value.strip() == name.strip():
                flag = True
                break
        return flag
