import os
from selene import browser, have, be


def test_check_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().should(be.blank).type('Shamo')
    browser.element('#lastName').click().should(be.blank).type('Shamilov')
    browser.element('#userEmail').click().should(be.blank).type('shamilov50@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').click().should(be.blank).type('8005553535')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1997"]').click()
    browser.element('[class*=day--07]').click()
    browser.element('#subjectsInput').click().should(be.blank).type('Eng').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('[type=file]').send_keys(os.path.abspath('pic/banana.jpg'))
    browser.element('#currentAddress').click().should(be.blank).type('Moscow st')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()

    browser.element('[id="example-modal-sizes-title-lg"]').should(
        have.exact_text('Thanks for submitting the form')
    )
    browser.all('tbody tr td:last-child').should(
        have.exact_texts(
            'Shamo Shamilov',
            'shamilov50@mail.ru',
            'Male',
            '8005553535',
            '07 August,1997',
            'English',
            'Sports, Reading, Music',
            'banana.jpg',
            'Moscow st',
            'Haryana Panipat',
        )
    )
