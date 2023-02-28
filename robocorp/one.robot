*** Settings ***
Documentation    Template robot main suite

Library    Selenium2Library    


*** Variables ***
${URL}       https://robotsparebinindustries.com/

*** Keywords ***
Open the intranet website
    Open Browser    ${URL} 

Log In
    Input Text    username    maria
    Input Password    password    thoushallnotpass
    # "Click Button Log in" or use "Submit Form"
    Submit Form
    Wait Until Page Contains Element    id:sales-form

Fill Sales Form
    # Use the name of each field as the locator
    Input Text    firstname    John
    Input Text    lastname    Smith    
    Input Text    salesresult    123
    Select From List By Value    salestarget   10000
    Click Button    Submit

*** Test Cases *** 
Open the website
    Open the intranet website 
    Log In
    
    Fill Sales Form