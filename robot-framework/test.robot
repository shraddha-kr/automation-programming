*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           Selenium2Library


*** Test Cases ***
Valid Login
    Open Browser     https://google.fr    chrome
