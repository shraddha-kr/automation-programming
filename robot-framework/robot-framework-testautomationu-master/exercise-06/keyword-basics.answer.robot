*** Settings ***
Library  OperatingSystem
Library  SeleniumLibrary

*** Test Cases ***
Check invoice manager page
    Comment    We've learned how to create a custom keyword!
    Navigate To Home Page
    My Keyword
    Page Should Contain     Invoice Manager

*** Keywords ***
My Keyword
    Comment         This is a keyword that shraddha created
Navigate To Home Page
    Open Browser    http://34.225.240.91		chrome
