from selenium import webdriver
import unittest


class newVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_startList_retrieveLater(self):
        #Sohail heard about a cool online app.
        #He decided to check its homepage...
        self.browser.get('http://127.0.0.1:8000')

        #He noticed a page title and header contained a to-do list
        self.assertIn('To-Do', self.browser.title)
        eader_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is prompted for a to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #He types "Buy more Jordans" into a test box
        inputbox.send_keys('Buy more Jordans')
        #He hits enter and the page updates
        #"1: Buy more Jordans"

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy more Jordans' for row in rows)
        )

        #There is an additional test box reqesting another item to add to the list
        self.fail('Finish the test!')
        #He enters "Ask Danielle how the activity is going"(Sohail is very helpful XD)

        #The page updates and shows bot items on his list

        #He wonders if the list is saved, luckily he sees a text box that has a link to his generated list
        #He happily saves the list and turns on the TV

if __name__ == '__main__':
    unittest.main()
