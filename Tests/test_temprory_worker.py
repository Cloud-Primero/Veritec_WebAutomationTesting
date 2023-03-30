from conftest import *
from base_helpers import *
from Locators.TempWorkersLocators import *
from test_Login import loginwithSteps

TW = Storage.temporaryWorkerData


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
        verify_element_is_present(email_xpath, driver)
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
        verify_element_is_present(AddRemarkButton_xpath, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerAdd(driver):
    VisitTemporary_WorkerPageWithSteps(driver)
    with allure.step('Then User fills "All" form data on "Temporary Worker" screen'):
        with allure.step('Enter Personal Data'):
            find_byXpath(FirstName_xpath, driver).send_keys(TW.FirstName)
            find_byXpath(LastName_xpath, driver).send_keys(TW.LastName)
            find_byXpath(Select_Nationality_xpath, driver).click()
            sleep(1)
            find_byXpath(Select_Nationality_xpath, driver).send_keys(TW.Nationality)
            find_byXpathAndWait(CountryName_xpath(TW.Nationality), driver).click()
            find_byXpath(PhoneNumber_CountryFlagIcon_xpath, driver).click()
            find_byXpath(PhoneNumberCountry_searchInput, driver).send_keys(TW.PhoneCountry)
            find_byXpath(PhoneNumberCountryNameClick(TW.PhoneCountry), driver).click()
            find_byXpath(PhoneNumberInput_xpath, driver).click()
            find_byXpath(PhoneNumberInput_xpath, driver).send_keys(TW.PhoneNumber)
            find_byXpath(address_xpath, driver).send_keys(TW.Address)
            find_byXpath(email_xpath, driver).send_keys(TW.Email)
            scroll_into_element(email_xpath, driver)

        with allure.step('Enter Employee Status'):
            find_byXpath(EmployeeTypeInput_xpath, driver).click()
            find_byXpathAndWait(EmployeeTypeInput_xpath, driver).send_keys(TW.EmployeeType)
            find_byXpath(EmployeeTypeSelect_xpath(TW.EmployeeType), driver).click()
            if find_byXpath(ContractTypeInleen_xpath, driver).is_selected():
                pass
            else:
                find_byXpath(ContractTypeInleen_xpath, driver).click()
            scroll_into_element(EmployeeStatusHeading_xpath, driver)
            find_byXpath(startDate_xpath, driver).click()
            find_byXpath(startDate_xpath, driver).send_keys(TW.StartDate)
            press_Enter(driver)

        with allure.step('Enter Client & Project Information'):
            scroll_into_element(ClientAndProjectHeading_xpath, driver)
            click_on_element_js(AssignClient_xpath, driver)
            find_Elements_byXpathAndWait(AssignClientsList_xpath, driver)[1].click()
            find_byXpath(AssignProject_xpath, driver).click()
            find_Elements_byXpathAndWait(AssignProjectsList_xpath, driver)[1].click()

        with allure.step('Enter Residence Information'):
            scroll_into_element(ResidenceHeading_xpath, driver)
            click_on_element_js(HouseYesCheckBox_xpath, driver)
            click_on_element_js(HouseNameInputSelect_xpath, driver)
            find_Elements_byXpathAndWait(HouseNameList_xpath, driver)[1].click()
            find_byXpath(HouseBedInputSelect_xpath, driver).click()
            find_Elements_byXpathAndWait(HouseBedList_xpath, driver)[1].click()

        with allure.step('Enter Transport Information'):
            scroll_into_element(TransportHeading_xpath, driver)
            click_on_element_js(TransportYes_xapth, driver)
            click_on_element_js(TypeTransportBike_xpath, driver)
            find_byXpath(NameBikeInput_xpath, driver).click()
            find_Elements_byXpathAndWait(BikeNameList_xpath, driver)[0].click()

        with allure.step('Enter Other Information and Upload File'):
            find_byXpath(VCA_YES_xpath, driver).click()
            find_byXpath(VCAStatusInput, driver).click()
            find_Elements_byXpath(VCAStatusList, driver)[0].click()
            find_byXpath(VCA_ValidUntil, driver).click()
            find_byXpath(VCA_ValidUntil, driver).send_keys(TW.StartDate)
            press_Enter(driver)
            find_byXpath(VCA_Insurance, driver).click()
            find_Elements_byXpath(VCA_InsuranceList_xpath, driver)[1].click()
            print(TW.filepath)
            find_byXpath(VCA_DocumentFile_xpath, driver).send_keys(TW.filepath)

        with allure.step('Handle Remarks Popup and Add Remarks'):
            find_byXpath(AddRemarkButton_xpath, driver).click()
            verify_element_is_present(RemarkIframe_xpath, driver)
            find_byXpath(remarksDate_xpath, driver).click()
            find_byXpath(remarksDate_xpath, driver).send_keys(TW.StartDate)
            press_Enter(driver)
            find_byXpath(statusInput_xpath, driver).click()
            find_Elements_byXpath(status_dropDownList_xpath, driver)[0].click()
            find_byXpath(remarksTextareaInput_xpath, driver).send_keys(TW.remarks)
            find_byXpath(addRemarksBtn_xpath, driver).click()

        with allure.step('Click Add Temporary Button to save information'):
            find_byXpath(AddTemporaryButton_xpath, driver).click()
        with allure.step('Verify from Success popup-message'):
            verify_visibility_of_element_located(TemporaryDataSave_SuccessMessage_xpath, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker with asterisks data")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.skip(reason="Not Implemented Yet")
def test_TemporaryWorkerAddAsterisksData(driver):
    VisitTemporary_WorkerPageWithSteps(driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Delete Temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.skip(reason="Not Implemented Yet")
def test_TemporaryWorkerDelete(driver):
    VisitTemporary_WorkerPageWithSteps(driver)
