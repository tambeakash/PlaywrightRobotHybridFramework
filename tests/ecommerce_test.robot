*** Settings ***
Library    ../keywords/ecommerce_keywords.py
Resource   ../resources/data.robot

*** Variables ***
${URL}    https://www.saucedemo.com

*** Test Cases ***
Complete E2E Purchase Flow
    ${users}=    Read Users From CSV    tests/data/users.csv
    FOR    ${user}    IN    @{users}
        Open Application    ${URL}
        Login To Application    ${user}[username]    ${user}[password]
        Add Item And Checkout
        Close Application
    END