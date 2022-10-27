*** Settings ***
Library  SeleniumLibrary
Library    SeleinumLibrary
*** Variables ***
${browser}  chrome
${url}  https://www.facebook.com/

*** Test Cases ***
Login
    Open browser    ${url}  ${browser}
    Login testing


*** Keywords ***
Login testing
    input text  name:email  muthuthangam1604@gmail.com
    input text  name:pass   muthums@cse
    click element    name:login