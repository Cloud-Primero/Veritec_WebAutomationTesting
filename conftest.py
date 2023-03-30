# import pytest
# from pytest import fixture
# from conftest import *
from base_helpers import *
import os
from base_helpers import get_randomEmail


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="CHROME"
    )
    parser.addoption(
        "--headless", action="store"
    )


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class TemoraryWorkerDataClass:
    FirstName = 'Terminator'
    LastName = 'Genesis'
    Nationality = 'Pakistani'
    PhoneCountry = 'Pakistan'
    PhoneNumber = '3058440924'
    Address = 'Chandigarh road mia wali khairpur karachi Sindh'
    Email = get_randomEmail()
    EmployeeType = 'Temporary Worker'
    StartDate = '30-APR-2023'
    filepath = os.getcwd() + '/TestData/terminator.jpeg'
    remarks = 'Quality Assurance, is a critical process in software development that ensures the final product'


class Storage:
    baseUrl = 'http://52.70.226.96:85'
    temporaryWorkerData = TemoraryWorkerDataClass()
    temproryWorkerUrl = 'http://52.70.226.96:85/temporary-worker/add'
    userData1 = {'Email': 'hassan.abbas@cloudprimero.com',
                 'Password': 'PowerPoint@123'}
    userData2 = {'Email': 'ahassan.abbas@cloudprimero.com',
                 'Password': 'aPowerPoint@123'}
    requestId = None
    skipAll = False
    skipAllDummy = False
    failedTestCases = []


# it runs before everything else


@pytest.fixture(scope='function')
def driver(request):
    print(request.config.option.browser)
    BROWSER = request.config.option.browser
    driver = None

    if request.config.option.headless == "1":
        headless = "--headless"
    else:
        headless = "headfull"

    if BROWSER == "CHROME":
        chrome_options = Chrome_options()
        chrome_options.add_argument(headless)
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)

    elif BROWSER == "FIREFOX":
        firefox_options = Firefox_options()
        firefox_options.add_argument(headless)
        firefox_options.add_argument('--log-level=3')
        firefox_options.add_argument("start-maximized")
        firefox_options.set_preference(
            'permissions.default.desktop-notification', 1)
        # driver = webdriver.Firefox(service=Firefox_service(
        #     GeckoDriverManager().install()), options=firefox_options)
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=firefox_options)

    elif BROWSER == "OPERA":
        pass
        # driver = webdriver.Chrome(service=Service(
        #     ChromeDriverManager().install()))

    else:
        pytest.skip(allow_module_level=True,
                    reason="Please provide a browser name to initiate tests")

    driver.implicitly_wait(7)
    driver.maximize_window()
    yield driver
    # sleep(180)
    driver.close()
    driver.quit()

# pytest Tests --alluredir=reports --screenshot=on --browser CHROME  -v -s --headless 0
# parallel test execution with 2 retry on failure
# Pytest Tests  --alluredir=reports --screenshot=on --browser CHROME  --headless 0 -n 10 --reruns 2
# pytest xdist
