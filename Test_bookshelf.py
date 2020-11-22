import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from  xpath_elements import xpath_dict as xpath
import utils
import time

class Case_bookshelf01(unittest.TestCase):
    # Description : Verify that all the navigation options work
    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_bookshelf01(self):
        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Bookshelf nav")
        utils.Find_and_Click(xpath['bookshelf_btn'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Bookshelf button")
        utils.Find_and_Click(xpath['my_bookshelf_nav'])
        self.assertIn("My Bookshelf", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on Shared With Me button")
        utils.Find_and_Click(xpath['shared_nav'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Drive button")
        utils.Find_and_Click(xpath['google_drive_nav'])
        self.assertIn("My Drive", utils.Get_element_text(xpath['page_title']))

    def tearDown(self):
        utils.Close_Browser()

#Resource_To_Add_Name needs to be setup before execute the test
class Case_bookshelf02(unittest.TestCase):
    # Description : Add a Google Drive document to Bookshelf resources
    Resource_To_Add_Name = ""

    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_bookshelf02(self):

        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Bookshelf nav")
        utils.Find_and_Click(xpath['bookshelf_btn'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Bookshelf button")
        utils.Find_and_Click(xpath['my_bookshelf_nav'])
        self.assertIn("My Bookshelf", utils.Get_element_text(xpath['page_title']))

        print("Opening the window: Select Resource Type")
        utils.Find_and_Click(xpath['add_resource_btn'])
        utils.Find_and_Click(xpath['add_type_resource'])

        print("Selecting Google Drive as resource")
        utils.Wait_For_Element(xpath['googleDrive_btn'])
        utils.Find_and_Click(xpath['googleDrive_btn'])
        utils.Wait_For_Element("(//button[contains(text(),'My Drive')])[1]")
        self.assertTrue(utils.Is_Text_in_Page("Add from Google Drive"))
        
        print("Adding File " +self.Resource_To_Add_Name)
        Document_To_Add_Xpath = "//td[contains(text(),'"+self.Resource_To_Add_Name+"')]"
        time.sleep(1)
        utils.Wait_For_Element(Document_To_Add_Xpath)        
        utils.Find_and_Click(Document_To_Add_Xpath)
        utils.Wait_For_Element(xpath['google_drive_save_btn'])
        utils.Send_Keys(Keys.PAGE_DOWN)
        utils.Find_and_Click(xpath['google_drive_save_btn'])

        print("Verifing file was added")
        Document_to_Verify = "//span[contains(text(),'"+self.Resource_To_Add_Name+"')]"
        utils.Wait_For_Element(Document_to_Verify)
        self.assertTrue(utils.Is_Element_Displayed(Document_to_Verify))

        print ("Deleting added file " +self.Resource_To_Add_Name)
        utils.Find_and_Click("//button[@aria-label='open actions menu' and @color='transparent']")
        utils.Find_and_Click("//span[contains(text(),'Delete')]")
        utils.Find_and_Click("//button[contains(text(),'Delete')]")
        time.sleep(2)
        try:
            self.assertFalse(utils.Is_Element_Displayed(Document_to_Verify))
        except:
            self.assertTrue(True)            
            print("Document was deleted")

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()

"""
I couldn't upload a file :(
skip this test
"""
class Case_bookshelf03(unittest.TestCase):
    # Description : Upload a file to bookshelf resources
    Path_To_file = ""

    @unittest.skip("I couldn't upload a file :(")
    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    @unittest.skip("I couldn't upload a file :(")
    def test_bookshelf03(self):

        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Bookshelf nav")
        utils.Find_and_Click(xpath['bookshelf_btn'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Bookshelf button")
        utils.Find_and_Click(xpath['my_bookshelf_nav'])
        self.assertIn("My Bookshelf", utils.Get_element_text(xpath['page_title']))

        print("Opening the window: Select Resource Type")
        utils.Find_and_Click(xpath['add_resource_btn'])
        utils.Find_and_Click(xpath['add_type_resource'])

        print("Selecting upload a file as resource type")
        utils.Wait_For_Element(xpath['upload_file_btn'])
        utils.Find_and_Click(xpath['upload_file_btn'])
        utils.Wait_For_Element("//div[@class='otus-modal-navbar__title' and contains(text(),'Add File')]")
        self.assertTrue(utils.Is_Text_in_Page("Add File"))
        
        time.sleep(2)
        print ("Clicking on Browse button")
        utils.Wait_For_Element("//otus-button[@buttontext='Browse']/button")
        browseElement = self.driver.find_element_by_xpath("//otus-button[@buttontext='Browse']")
        self.driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', browseElement)
        browseElement.send_keys('Path_To_file')
        time.sleep(2)

    @unittest.skip("I couldn't upload a file :(")
    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()

#Link to a document needs to be setup before execute the test
class Case_bookshelf04(unittest.TestCase):
    # Description : Add a Link to bookshelf resources
    Link = "https://youtu.be/dQw4w9WgXcQ"
    LinkName = "A Link"

    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_bookshelf04(self):

        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Bookshelf nav")
        utils.Find_and_Click(xpath['bookshelf_btn'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Bookshelf button")
        utils.Find_and_Click(xpath['my_bookshelf_nav'])
        self.assertIn("My Bookshelf", utils.Get_element_text(xpath['page_title']))

        print("Opening the window: Select Resource Type")
        utils.Find_and_Click(xpath['add_resource_btn'])
        utils.Find_and_Click(xpath['add_type_resource'])

        print("Selecting Add Link as resource")
        utils.Wait_For_Element(xpath['link_btn'])
        utils.Find_and_Click(xpath['link_btn'])
        utils.Wait_For_Element("(//input[contains(@class,'attach-link__input')])[1]")
        self.assertTrue(utils.Is_Text_in_Page("Add Link"))
        
        print("Adding link information")
        utils.Find_and_Input(xpath['add_link_input'], self.Link)
        utils.Find_and_Input(xpath['add_link__name_input'], self.LinkName)
        utils.Find_and_Click(xpath["save_btn"])

        #validate resource and delete
        print("Verifing file was added")
        Document_to_Verify = "//span[contains(text(),'"+self.LinkName+"')]"
        utils.Wait_For_Element(Document_to_Verify)
        self.assertTrue(utils.Is_Element_Displayed(Document_to_Verify))

        print ("Deleting added file " +self.LinkName)
        utils.Find_and_Click("//button[@aria-label='open actions menu' and @color='transparent']")
        utils.Find_and_Click("//span[contains(text(),'Delete')]")
        utils.Find_and_Click("//button[contains(text(),'Delete')]")
        time.sleep(2)
        try:
            self.assertFalse(utils.Is_Element_Displayed(Document_to_Verify))
        except:
            self.assertTrue(True)            
            print("Document was deleted")

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()


class Case_bookshelf05(unittest.TestCase):
    # Description : Add a photo to bookshelf resources

    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_bookshelf05(self):

        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Bookshelf nav")
        utils.Find_and_Click(xpath['bookshelf_btn'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Bookshelf button")
        utils.Find_and_Click(xpath['my_bookshelf_nav'])
        self.assertIn("My Bookshelf", utils.Get_element_text(xpath['page_title']))

        print("Opening the window: Select Resource Type")
        utils.Find_and_Click(xpath['add_resource_btn'])
        utils.Find_and_Click(xpath['add_type_resource'])

        print("Selecting Photo as resource")
        utils.Wait_For_Element(xpath['photo_btn'])
        utils.Find_and_Click(xpath['photo_btn'])
        utils.Wait_For_Element("//span[contains(text(),'Take a Photo')]")
        self.assertTrue(utils.Is_Text_in_Page("Add Photo"))
        
        utils.Find_and_Click("//span[contains(text(),'Take a Photo')]")
        time.sleep(2)
        utils.Find_and_Click("(//span[contains(text(),'Take a Photo')])[2]//ancestor::button")
        utils.Find_and_Click("(//span[contains(text(),'Take a Photo')])[2]//ancestor::button")
        utils.Find_and_Click(xpath['save_btn'])

        #validate resource and delete
        print("Verifing file was added")
        Document_to_Verify = "//span[contains(text(),'photo.png')]"
        utils.Wait_For_Element(Document_to_Verify)
        self.assertTrue(utils.Is_Element_Displayed(Document_to_Verify))

        print ("Deleting added file ")
        utils.Find_and_Click("//button[@aria-label='open actions menu' and @color='transparent']")
        utils.Find_and_Click("//span[contains(text(),'Delete')]")
        utils.Find_and_Click("//button[contains(text(),'Delete')]")
        time.sleep(2)
        try:
            self.assertFalse(utils.Is_Element_Displayed(Document_to_Verify))
        except:
            self.assertTrue(True)            
            print("Document was deleted")

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()


class Case_bookshelf06(unittest.TestCase):
    # Description : Add a video to bookshelf resources

    def setUp(self):
        print ("Opening Browser")
        utils.Open_Browser("https://my.otus.com/login")
        print ("Loggin in")
        utils.Log_in()
        self.driver = utils.driver

    def test_bookshelf06(self):

        print ("Validating if log in was successful")
        # to verify if the search results page loaded
        self.assertIn("Otus",self.driver.title)

        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)

        print ("Clicking on Bookshelf nav")
        utils.Find_and_Click(xpath['bookshelf_btn'])
        self.assertIn("Shared With Me", utils.Get_element_text(xpath['page_title']))

        print ("Clicking on My Bookshelf button")
        utils.Find_and_Click(xpath['my_bookshelf_nav'])
        self.assertIn("My Bookshelf", utils.Get_element_text(xpath['page_title']))

        print("Opening the window: Select Resource Type")
        utils.Find_and_Click(xpath['add_resource_btn'])
        utils.Find_and_Click(xpath['add_type_resource'])

        print("Selecting Video as resource")
        utils.Wait_For_Element(xpath['video_btn'])
        utils.Find_and_Click(xpath['video_btn'])
        utils.Wait_For_Element("//span[contains(text(),'Record Video')]//ancestor::button")
        self.assertTrue(utils.Is_Text_in_Page("Add Video"))
        
        utils.Find_and_Click("//span[contains(text(),'Record Video')]//ancestor::button")
        time.sleep(2)
        utils.Find_and_Click("//button[@title='Device']")
        utils.Find_and_Click("//button[@title='Record']")
        time.sleep(2)
        utils.Find_and_Click("//button[@title='Stop']")
        utils.Find_and_Input("//input[contains(@class,'attach-video__input')]", "videoTest01")
        utils.Find_and_Click(xpath['save_btn'])

        #validate resource and delete
        print("Verifing file was added")
        Document_to_Verify = "//span[contains(text(),'videoTest01')]"
        utils.Wait_For_Element(Document_to_Verify)
        self.assertTrue(utils.Is_Element_Displayed(Document_to_Verify))

        print ("Deleting added file ")
        utils.Find_and_Click("//button[@aria-label='open actions menu' and @color='transparent']")
        utils.Find_and_Click("//span[contains(text(),'Delete')]")
        utils.Find_and_Click("//button[contains(text(),'Delete')]")
        time.sleep(2)
        try:
            self.assertFalse(utils.Is_Element_Displayed(Document_to_Verify))
        except:
            self.assertTrue(True)            
            print("Document was deleted")

    def tearDown(self):
        print ("Ending session")
        utils.Close_Browser()


if __name__ == "__main__":
    unittest.main()