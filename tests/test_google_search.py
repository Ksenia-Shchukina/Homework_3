from selene import browser, have


class TestGoogleSearch:
    def test_google_search_valid_input(self, browser_for_test):
        browser.element('[name="q"]').type('qa guru').press_enter()
        browser.element('[class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"]').should(have.text('QA.GURU'))

    def test_google_search_invalid_input(self, browser_for_test):
        browser.element('[name="q"]').type('blablabla muhaha 123456qwertydddddddddddddddddddddddddd').press_enter()
        browser.element('[style="padding-top:.33em"]').should(have.text('не найдены.'))
