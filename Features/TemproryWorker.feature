Feature: Temporary Worker Feature

    @TemporaryWorkerScreen @Regression @Sanity
    Scenario: Add new temporary worker Screen
        Given Go to the Base url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then Verify user is on "Add Temporary Worker" screen

    @TemporaryWorkerMandatoryFields @Regression @Sanity
    Scenario: Add new temporary worker Mandatory Fields Screen
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then Verify user is on "Add Temporary Worker" screen
        Then User clicks "Add Temporary Worker Form Button" button on "Temporary Worker" screen
        And Verify mandatory fields for "Temporary Worker" screen


    @TemporaryWorkerAdd @Regression @Sanity
    Scenario: Add new temporary worker
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then User fills "All" form data on "Temporary Worker" screen
        Then User clicks "Temporary Worker Back Button" button on "Temporary Worker" screen
        And Verify record is present on the top of table

    @TemporaryWorkerAddAsterisksData @Regression @Sanity
    Scenario: Add new temporary worker with asterisks data
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then User fills "Asterisks" form data on "Temporary Worker" screen
        Then User clicks "Temporary Worker Back Button" button on "Temporary Worker" screen
        And Verify "Temporary Worker Asterisks" data is present on "Temporary Worker Edit" screen

    @TemporaryWorkerDelete @Regression @Sanity
    Scenario: Delete Temporary worker
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then User fills "Asterisks" form data on "Temporary Worker" screen
        Then User clicks "Temporary Worker Back Button" button on "Temporary Worker" screen
        And User is able to delete "Temporary Worker Asterisks" data