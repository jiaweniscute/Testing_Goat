from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    print("in class")
    def setUp(self):
        chromedriver = '/usr/local/bin/chromedriver'
        self.browser = webdriver.Chrome(chromedriver)
        print("after setup")
    def tearDown(self):
        self.browser.quit()
        print("after tear down")

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        print('end of test')


        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        print('end of test')

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')