import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from  xpath_elements import xpath_dict as xpath
import utils

# the parameter class_to_validate needs to be set up before executing
class Case_Classboard01(unittest.TestCase):
    # Description : Review a class board summary
    class_to_validate = "QA Tech Challenge"
    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_Classboard01(self):
        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Classes nav")
        utils.Find_and_Click(xpath['classes_btn'])
        self.assertIn("Classes", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on class : " + self.class_to_validate)
        utils.Find_and_Click("//span[contains(text(),'"+self.class_to_validate+"')]/parent::div")
        self.assertTrue(utils.Is_Text_in_Page("Class Board"))

        print ("Clicking class summary")
        utils.Find_and_Click("//div[@class='ot-post-summary__post-header']")
        self.assertTrue(utils.Is_Element_Displayed("//div[@class='ot-page-header-title']"))

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()

if __name__ == "__main__":
    unittest.main()