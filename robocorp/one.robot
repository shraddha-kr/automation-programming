*** Settings ***
Documentation    Template robot main suite

Library    Selenium2Library    
Library    RequestsLibrary
Library    OperatingSystem
Library    ExcelLibrary
Library    ./excelhandling.py
Library    String
*** Variables ***
${URL}       https://robotsparebinindustries.com/
${URI}       https://robotsparebinindustries.com/SalesData.xlsx 
${EXCELFILE}     ${EXECDIR}/robocorp/SalesData.xlsx
@{one}    [[Shraddha]    [Kharangate]    [12345]]    [[Rishabh]    [Kharangate]    [67891]]    [[Rohan]    [Kharangate]    [112342]]
@{two}    one    two    three
*** Keywords ***
Open the intranet website
    Open Browser    ${URL} 


Log In
    Input Text    username    maria
    Input Password    password    thoushallnotpass
    # "Click Button Log in" or use "Submit Form"
    Submit Form
    # For the next case to complete ensure the required page gets loaded, using form id of the resultant page
    Wait Until Page Contains Element    id:sales-form

Fill Sales Form
    # Use the name of each field as the locator & use List By Value for select dropdown
    Input Text    firstname    John
    Input Text    lastname    Smith    
    Input Text    salesresult    123
    Select From List By Value    salestarget   10000
    Click Button    Submit

Download the Excel file
    # Use a session with a GET request 
    Create Session    test    https://robotsparebinindustries.com/
    ${response}=    Get Request	    test    https://robotsparebinindustries.com/SalesData.xlsx 
    Run Keyword And Continue On Failure     Should Be Equal As Numbers  ${response.status_code}    200
    Create Binary File    ${EXECDIR}/robocorp/SalesData.xlsx   ${response.content}

Fill Sales Form using the data from the Excel file
    # Open Excel     ${EXECDIR}/robocorp/SalesData3.xls     
    # ${sales_reps}    Get Sheet Values	data
    # Log To Console     ${sales_reps}    
    Use excel handling

Use excel handling
    ${excel_val}=    excelhandling.Open And Read Excel File  data  ${EXCELFILE}
    Fill and submit the form for one person    ${excel_val}

Fill and submit the form for one person
    [Arguments]    ${sales_rep}
    FOR     ${in}    ${one_rep}    IN ENUMERATE    @{sales_rep}                                                  
        Input Text    firstname    ${one_rep}[0]       
        Input Text    lastname    ${one_rep}[1]
        Input Text    salesresult  ${one_rep}[2]  
        Select From List By Value    salestarget    ${one_rep}[3]
        Click Button    Submit        
    END


*** Test Cases ***  
Open the website
    Open the intranet website 
    Log In
    Download the Excel file
    Fill Sales Form using the data from the Excel file
    
