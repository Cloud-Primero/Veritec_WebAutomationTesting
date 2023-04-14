from Locators.TempWorkersLocators import csvFileEXPORTNAME, nextPage, mainShowHideButton, mainExportButton, \
    mainFilterButton
from Tests.test_temprory_worker import downloadAndVerifyCSVExportedFile
from conftest import *
from base_helpers import *
from Locators.UsersLocators import *
from test_Login import loginwithSteps


@allure.feature("Users Feature")
@allure.story("Verify Users Screen Navigation")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_UsersScreenNavigation(driver):
    loginwithSteps(driver)
    UsersUrl = 'active-user'
    with allure.step('Then User clicks "Users" button on "Homepage" screen'):
        find_byXpath(UsersMainLink_xpath, driver).click()
    with allure.step('And User Should see "active-user" in the url'):
        assert UsersUrl in driver.current_url


def VisitUsersPageWithLogin(driver):
    test_UsersScreenNavigation(driver)


@allure.feature("Users Feature")
@allure.story("Check If Export Button actually downloads the file and its in csv format")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.smoke
@pytest.mark.order(3)
def test_UsersCheckExportButtonDownloadsCSVFile(driver):
    VisitUsersPageWithLogin(driver)
    fileName = downloadAndVerifyCSVExportedFile(driver)
    os.remove(fileName)


@allure.feature("Users Feature")
@allure.story("Verify If Exported CSV Users file has the exact data matches with table")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_UsersVerifyIfExportedCSVFileDataMatchesWithWebTableData(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And Check if CSV file downloaded correctly'):
        fileName = Storage.downloadsPath + find_byXpath(csvFileEXPORTNAME, driver).get_attribute("download") + '.csv'
        downloadAndVerifyCSVExportedFile(driver)

    with allure.step("Verify If Exported CSV file has the exact data matches with table"):
        scroll_to_bottom_of_page(driver)
        sleep(4)
        df = pd.read_csv(fileName)
        df = df.fillna('')

        counter = 0
        page = 1

        for i, row in df.iterrows():
            if counter == 10:
                print(f'Page : {page + 1}')
                page += 1
                counter = 0
                find_byXpath(nextPage, driver).click()

            csv_list = row.tolist()
            ID = csv_list[0]
            first_name = csv_list[1]
            last_name = csv_list[2]
            email = csv_list[3]
            role = csv_list[4]
            phone_number = csv_list[5]
            created_by = csv_list[6]
            approve_by = csv_list[7]
            status = csv_list[8]

            listOfData = [ID, first_name, last_name, email, role, phone_number, created_by, approve_by, status]

            # noinspection PyTypeChecker
            verifyDatainTableByRow(driver, rowData=listOfData, rowIndex=counter)
            counter += 1


@allure.feature("Users Feature")
@allure.story("Navigate to check if Users for approval page is present")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_UsersNavigateToUsersForApprovalPage(driver):
    VisitUsersPageWithLogin(driver)
    UsersForApprovalTabUrl = 'approve-user'
    with allure.step('Then User clicks "Users for Approval" button on screen'):
        find_byXpath(UsersForApprovalTab_xpath, driver).click()

    with allure.step('And User Should see "approve-user" in the url'):
        assert UsersForApprovalTabUrl in driver.current_url


@allure.feature("Users Feature")
@allure.story("Check All Necessary Buttons Clickable")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(4)
def test_UserCheckNecessaryButtonsClickAble(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And Check if All Necessary Buttons are Clickable'):
        verify_elementIsClickAble(mainShowHideButton, driver)
        verify_elementIsClickAble(mainExportButton, driver)
        verify_elementIsClickAble(mainFilterButton, driver)


@allure.feature("Users Feature")
@allure.story("Check All Necessary Buttons are Visible")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(4)
def test_UserCheckNecessaryButtonsVisible(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And Check if All Necessary Buttons are Clickable'):
        verify_visibility_of_element_located(mainShowHideButton, driver)
        verify_visibility_of_element_located(mainExportButton, driver)
        verify_visibility_of_element_located(mainFilterButton, driver)
