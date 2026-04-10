from playwright.sync_api import sync_playwright, expect



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Реализовано как ввод с эмуляцией клавиатуры, т.к. в рамках уроков рассматривался данный способ. В строке с комментарием указан более оптимальный способ, но из прошлых уроков, поэтому решил использовать новый.
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.type(char)
    #email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()
    for char in 'username':
        page.keyboard.type(char)
    #username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()
    for char in 'password':
        page.keyboard.type(char)
    #password_input.fill("password")

    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(5000)

