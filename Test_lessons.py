import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from  xpath_elements import xpath_dict as xpath
import utils

# the parameter Lesson_to_validate needs to be set up before executing
class Case_Lessons01(unittest.TestCase):
    # Description : Review a class board summary
    Lesson_to_validate = "QA Technical Challenge"
    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_Lessons01(self):
        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Lesson nav")
        utils.Find_and_Click(xpath['lessons_btn'])
        utils.Wait_For_Element("//td[contains(text(),'"+self.Lesson_to_validate+"')]")
        self.assertIn("Lessons", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on Lesson : " + self.Lesson_to_validate)
        utils.Find_and_Click("//td[contains(text(),'"+self.Lesson_to_validate+"')]")
        self.assertTrue(utils.Is_Element_Displayed("//div[contains(text(),'"+self.Lesson_to_validate+"')]"))

        print ("Clicking Save&Exit")
        utils.Find_and_Click("//span[contains(text(),'Save & Exit')]//parent::button")
        self.assertIn("Lessons", utils.Get_element_text(xpath['page_title']))

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()

if __name__ == "__main__":
    unittest.main()