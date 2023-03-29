from conftest import *
from base_helpers import *
from Locators.TempWorkersLocators import *
from test_Login import loginwithSteps


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker Screen")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerScreen(driver):
    loginwithSteps(driver)
    with allure.step('Then User clicks "Temporary Worker" button on "Homepage" screen'):
        find_byXpath(TemproryworkersMainLink_xpath, driver).click()

    with allure.step('Then Scroll "Down" into view "Add New Temporary Worker" Section'):
        scroll_into_element(AddNewWorker_xpath, driver)

    with allure.step('Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen'):
        find_byXpath(AddNewWorker_xpath, driver).click()

    with allure.step('Then Verify user is on "Add Temporary Worker" screen'):
        check_IFRedirectedON_ValidUrl(Storage.temproryWorkerUrl, driver)


def VisitTemporary_WorkerPageWithSteps(driver):
    test_TemporaryWorkerScreen(driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Verify All mandatory fields for Temporary Worker Screen")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerMandatoryFields(driver):
    VisitTemporary_WorkerPageWithSteps(driver)
    with allure.step('And Verify All mandatory fields for "Temporary Worker" screen'):
        # Personal Details
        verify_element_is_present(PersonalDetails_xpath, driver)
        verify_element_is_present(AddWorkerHeading_xpath, driver)
        verify_element_is_present(FirstName_xpath, driver)
        verify_element_is_present(LastName_xpath, driver)
        verify_element_is_present(Select_Nationality_xpath, driver)
        verify_element_is_present(PhoneNumberInput_xpath, driver)
        verify_element_is_present(PhoneNumber_CountryFlagIcon_xpath, driver)
        verify_element_is_present(address_xpath, driver)
        verify_element_is_present(email_xapth, driver)
        # Employee Status
        verify_element_is_present(EmployeeStatusHeading_xpath, driver)
        verify_element_is_present(EmployeeTypeInput_xpath, driver)
        verify_element_is_present(ContractTypeInleen_xpath, driver)
        verify_element_is_present(ContractTypeVeritec_xpath, driver)
        verify_element_is_present(WorkStatus_xpath, driver)
        verify_element_is_present(startDate_xpath, driver)
        # Client And Project
        verify_element_is_present(ClientAndProjectHeading_xpath, driver)
        verify_element_is_present(AssignClient_xpath, driver)
        verify_element_is_present(AssignProject_xpath, driver)
        # Residence
        verify_element_is_present(ResidenceHeading_xpath, driver)
        verify_element_is_present(HouseYesCheckBox_xpath, driver)
        verify_element_is_present(HouseNoCheckBox_xpath, driver)
        verify_element_is_present(HouseNameInputSelect_xpath, driver)
        verify_element_is_present(HouseBedInputSelect_xpath, driver)
        # Transport
        verify_element_is_present(TransportHeading_xpath, driver)
        verify_element_is_present(TransportYes_xapth, driver)
        verify_element_is_present(TransportNO_xapth, driver)
        verify_element_is_present(OwnCarYes_xapth, driver)
        verify_element_is_present(OwnCarNO_xapth, driver)
        verify_element_is_present(TypeTransportBike_xpath, driver)
        verify_element_is_present(TypeTransportCar_xapth, driver)
        # Others
        verify_element_is_present(OthersHeading_xpath, driver)
        verify_element_is_present(VCA_YES_xpath, driver)
        verify_element_is_present(VCA_NO_xpath, driver)
        verify_element_is_present(VCA_DocumentFile_xpath, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.skip(reason="Not Implemented Yet")
def test_TemporaryWorkerAdd(driver):
    loginwithSteps(driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker with asterisks data")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.skip(reason="Not Implemented Yet")
def test_TemporaryWorkerAddAsterisksData(driver):
    loginwithSteps(driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Delete Temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.skip(reason="Not Implemented Yet")
def test_TemporaryWorkerDelete(driver):
    loginwithSteps(driver)
