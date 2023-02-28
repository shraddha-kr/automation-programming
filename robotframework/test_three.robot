*** Settings ***
Library    Selenium2Library

*** Variables ***
${HOMEPAGE}    http://www.google.com
${BROWSER}    Chrome

*** Keywords ***
open the browser
Open Browser ${HOMEPAGE}${BROWSER}

search topic
[Arguments] ${topic}
Input Text name=q${topic}
Press key name=q\\13

*** Test Cases ***
Open Browser
