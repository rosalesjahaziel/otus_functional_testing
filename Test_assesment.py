import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from  xpath_elements import xpath_dict as xpath
import utils

class Case_Assesment01(unittest.TestCase):
    # Description : Verify assessment list loaded

    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_precondition(self):
        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

       # page_title = utils.Get_element_text(xpath['page_title'])
        print ("Clicking on Assessment button")

        utils.Find_and_Click(xpath['assesment_btn'])
        self.assertIn("Assessments", utils.Get_element_text(xpath['page_title']))

        print ("Is assesment available")        
        self.assertTrue(utils.Is_Element_Displayed(xpath['status_lbl']))

    def tearDown(self):
        utils.Close_Browser()

if __name__ == "__main__":
    unittest.main()