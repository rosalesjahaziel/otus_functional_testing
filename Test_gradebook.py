import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from  xpath_elements import xpath_dict as xpath
import utils

class Case_Gradebook01(unittest.TestCase):
    # Description : Verify that gradebook table is visible by Points and Standards
    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_Gradebook01(self):
        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Gradebook nav")
        utils.Find_and_Click(xpath['gradebook_btn'])
        utils.Wait_For_Element("//button[contains(text(),'Points')]")
        self.assertIn("Gradebook", utils.Get_element_text(xpath['page_title']))


        print ("Validating table elements")
        utils.Wait_For_Element("//span[contains(text(),'Class')]/parent::div")
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Class')]/parent::div"))
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Grade')]/parent::div"))
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Total')]/parent::div"))
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Subject')]/parent::div"))
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Teacher')]/parent::div"))

        print ("Changing to 'Standards' filter")
        utils.Find_and_Click("//button[contains(text(),'Standards')]")
        utils.Wait_For_Element("//span[contains(text(),'Standard')]/parent::div")
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Standard')]/parent::div"))
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Last Attempt')]/parent::div"))
        self.assertTrue(utils.Is_Element_Displayed("//span[contains(text(),'Performance')]/parent::div"))

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()

if __name__ == "__main__":
    unittest.main()