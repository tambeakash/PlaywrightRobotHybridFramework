*** Settings ***
Library    ../keywords/ecommerce_keywords.py

*** Variables ***
${URL}    https://www.saucedemo.com

*** Test Cases ***
Complete E2E Purchase Flow
    Open Application    ${URL}
    Login To Application    standard_user    secret_sauce
    Add Item And Checkout
    Close Application