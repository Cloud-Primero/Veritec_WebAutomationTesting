TemproryworkersMainLink_xpath = '//a[text()="Temporary Workers"]/parent::li'
AddNewWorker_xpath = '//a[text()="Add New Temporary Worker"]'
AddWorkerHeading_xpath = '//h5[text()="Add new Temporary Worker"]'

# form locators

# personal Details locators
PersonalDetails_xpath = '//h2[text()=" Personal Details "]'
FirstName_xpath = '//input[@placeholder="Enter First Name"]'
LastName_xpath = '//input[@placeholder="Enter Last Name"]'
Select_Nationality_xpath = '//input[@id="register_nationality"]'
CountryName_xpath = '//div[@class="ant-select-item-option-content" and text()="Chilean"]'
PhoneNumber_CountryFlagIcon_xpath = '//div[@class="flag nl"]/div[@class="arrow"]'
PhoneNumberCountry_searchInput = '//ul[@class="country-list "]/li//input[@class="search-box"]'  # find Country
PhoneNumberInput_xpath = '//input[@placeholder="Enter Phone Number"]'
address_xpath = '//textarea[@placeholder="Enter Address"]'
email_xapth = '//input[@placeholder="Enter Email Address"]'

# Employee Status
EmployeeStatusHeading_xpath = '//h2[text()=" Employee Status "]'
EmployeeTypeInput_xpath = '//input[@id="register_employee_type"]'
ContractTypeInleen_xpath = '//span[text()="Inleen/Dorleen"]'
ContractTypeVeritec_xpath = '//span[text()="Veritec"]'
WorkStatus_xpath = '//input[@id="register_worker_status"]'
startDate_xpath = '//input[@id="register_start_date"]'

# Client And Project
ClientAndProjectHeading_xpath = '//h2[text()=" Client & Project "]'
AssignClient_xpath = '//input[@id="register_client_id"]'
AssignProject_xpath = '//input[@id="register_project_id"]'

# Residence
ResidenceHeading_xpath = '//h2[text()=" Residence "]'
HouseYesCheckBox_xpath = '//h2[text()=" Residence "]/parent::div//input[@class="ant-radio-input" and @value="true"]'
HouseNoCheckBox_xpath = '//h2[text()=" Residence "]/parent::div//input[@class="ant-radio-input" and @value="false"]'
HouseNameInputSelect_xpath = '//input[@id="register_residence_id"]'
HouseBedInputSelect_xpath = '//input[@id="register_bed_number"]'

# Transport
TransportHeading_xpath = '//h2[text()=" Transport "]'
TransportYes_xapth = '//label[@title="Transport"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                     '@value="true"]'
TransportNO_xapth = '//label[@title="Transport"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                    '@value="false"]'
OwnCarYes_xapth = '//label[@title="Own Car"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                  '@value="true"]'
OwnCarNO_xapth = '//label[@title="Own Car"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                 '@value="false"]'
TypeTransportBike_xpath = '//label[text()="Type of Transport"]/parent::div/following-sibling::div//span[text(' \
                          ')="Bike"]/parent::label//input[@type="radio"]'
TypeTransportCar_xapth = '//label[text()="Type of Transport"]/parent::div/following-sibling::div//span[text(' \
                         ')="Car"]/parent::label//input[@type="radio"]'

# Others
OthersHeading_xpath = '//h2[text()=" Others "]'
VCA_YES_xpath = '//div[@id="register_is_vca"]//input[@value="true"]'
VCA_NO_xpath = '//div[@id="register_is_vca"]//input[@value="false"]'
VCA_DocumentFile_xpath = '//label[@title="VCA Document"]/parent::div/parent::div//input[@type="file"]/parent::span'

