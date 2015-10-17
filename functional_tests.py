from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app
        # She goes to check out its homepage

        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item right away

        # She types "Buy peacock feathers" into a text box
        # Her hobby is tying fly lures

        # When she hits enter, the page updates, and now the page
        # lists her to-do item

        # There is still a text box to enter another item
        # She enters "Use feather to make a fly"

        # The page updates again and shows both items

        # She wonders if the site will remember her list
        # She notices there is a unique URL - with some text explaining
        # what the URL is used For

        # She visits the URL - her to-do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
