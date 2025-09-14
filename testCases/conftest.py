import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     # driver.quit()



#---- Different Browser code--------
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Launching Chrome Browser **********")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox Browser **********")
    elif browser == "ie":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        print("Launching IE Browser **********")
    else:
        raise ValueError(f"Browser '{browser}' is not supported!")

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests: chrome, firefox, or ie")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

###############Pytest HTML Reports #############
# Hook for adding/modifying environment info
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Add custom environment info
    metadata['Project Name'] = 'nop commerce'
    metadata['Module Name'] = 'Customers'
    metadata['Tester'] = 'Sainath'

    # Remove unwanted keys
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)