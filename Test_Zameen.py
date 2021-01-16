# from os import pathsep
import unittest as ut
import logging as lg
import openpyxl
# import utilities_ddt as utility
# import config as config
import time

# import selenium

import re




class test_OladocZameenAssesment(ut.TestCase):
    
    


    @classmethod
    def setUpClass(self):
        super(test_OladocZameenAssesment, self).setUpClass()
        
        lg.basicConfig(filename="C://Users/Asim Kabir/Desktop/dev/SeleniumWebDriver Practice/master/oladoc/logs/metaTitles_logs.txt", format='%(asctime)s: %(levelname)s:---> %(message)s', datefmt='%m/%d/%y %I:%M:%S:%p', level=lg.DEBUG)
        # lg.debug("Class setup is done")
        # lg.info("it is info")
        # lg.warning("it is warning")
        # lg.error("it is error")
        # lg.critical("It is critical")

        
        




        
    def test_Zameen(self):
        # self.driver = webdriver.Chrome('./webDrivers/chromedriver')
        # url = "https://www.airbnb.com/"
        # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
        # self.driver.get(url)
        # self.driver.maximize_window()
        # self.element = self.driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Location 
        # self.element.send_keys("Rome, Italy")
        # # self.element = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div")
        # # self.element.send_keys("Rome, Italy")
        # time.sleep(3)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]").click() 
        # time.sleep(3)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div").click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]/div/div/div").click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div").click()
        # time.sleep(1)
        # self.ele_guest = self.driver.find_element_by_xpath("//*[@id='stepper-adults']/button[2]")
        # self.ele_guest.click()
        # time.sleep(1)

        # self.ele_guest.click()
        # time.sleep(1)
        # self.ele_guest = self.driver.find_element_by_xpath("//*[@id='stepper-children']/button[2]")
        # self.ele_guest.click()
        # time.sleep(2)
        # self.ele_Search = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[4]/button").click()
        # time.sleep(5)
        # self.ele_location = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]/div/button[1]/div")
        # self.location_Text = self.ele_location.text
        # print(self.location_Text)
        # time.sleep(3)
        # self.ele_Date = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]/div/button[2]/div")
        # self.date_Text = self.ele_Date.text
        # print(self.date_Text)
        # time.sleep(3)
        # self.ele_Guests = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]/div/button[3]/div[1]")
        # self.guests_Text = self.ele_Guests.text
        # print(self.guests_Text)
        # time.sleep(3)

        ###########################################################################################################################################################################
        # self.driver = webdriver.Chrome('./webDrivers/chromedriver')
        # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
        # self.driver.maximize_window()
        # self.driver.get(url1)
        

        # self.ele_DetailContainer = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]").click() #clicking on Detailed Container
        # time.sleep(2)    

        ####################################################################################################################################################################    

        # self.ele_DetailContainer_Location = self.driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Detailed Container location
        # self.ele_DetailContainer_Location_Text = self.ele_DetailContainer_Location.get_attribute("value")
        # print(self.ele_DetailContainer_Location_Text)
        # # time.sleep(2)        

        # self.ele_DetailContainer_Date_Checkin = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]/div/div[2]") # Detailed Container location
        # self.ele_DetailContainer_Date_Checkin_Text = self.ele_DetailContainer_Date_Checkin.text
        # print(self.ele_DetailContainer_Date_Checkin_Text)
        # # time.sleep(2)        


        # self.ele_DetailContainer_Date_Checkout = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[3]/div[1]/div/div[2]") # Detailed Container location
        # self.ele_DetailContainer_Date_Checkout_Text = self.ele_DetailContainer_Date_Checkout.text
        # print(self.ele_DetailContainer_Date_Checkout_Text)
        # time.sleep(2)        

        # self.ele_DetailContainer_Guest = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div/div[2]") # Detailed Container location
        # self.ele_DetailContainer_Guest_Text = self.ele_DetailContainer_Guest.text
        # print(self.ele_DetailContainer_Guest_Text)
        time.sleep(1)        

    # def test_VerifyLocation (self):
    #     self.driver = webdriver.Chrome('./webDrivers/chromedriver')
    #     url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    #     self.driver.maximize_window()
    #     self.driver.get(url1)

    #     self.ele_DetailContainer = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]").click() #clicking on Detailed Container
    #     time.sleep(2)        

        
    #     self.ele_DetailContainer_Location = self.driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Detailed Container location
    #     self.ele_DetailContainer_Location_Text = self.ele_DetailContainer_Location.get_attribute("value")
    #     print(self.ele_DetailContainer_Location_Text)
    #     self.assertEqual(self.ele_DetailContainer_Location_Test, "Rome, Italy", "Failed: --> Location is not matching")
    #     lg.error("Failed: --> Location is not matching")
    #     time.sleep(2)        

    # def test_VerifyCheckInDate (self):            
    #     self.driver = webdriver.Chrome('./webDrivers/chromedriver')
    #     url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    #     self.driver.maximize_window()
    #     self.driver.get(url1)
        
    #     self.ele_DetailContainer = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]").click() #clicking on Detailed Container
    #     time.sleep(2)        


    #     self.ele_DetailContainer_Date_Checkin = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]/div/div[2]") # Detailed Container location
    #     self.ele_DetailContainer_Date_Checkin_Text = self.ele_DetailContainer_Date_Checkin.text
    #     print(self.ele_DetailContainer_Date_Checkin_Text)
    #     self.assertEqual(self.ele_DetailContainer_Date_Checkin_Text, "Jan 16", "Failed: --> CheckIn is not matching")
    #     lg.error("Failed: --> CheckIn is not matching")
    #     time.sleep(2)

    # def test_VerifyCheckOutDate (self):
    #     self.driver = webdriver.Chrome('./webDrivers/chromedriver')
    #     url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    #     self.driver.maximize_window()
    #     self.driver.get(url1)
        
    #     self.ele_DetailContainer = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]").click() #clicking on Detailed Container
    #     time.sleep(2)        



    #     self.ele_DetailContainer_Date_Checkout = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[3]/div[1]/div/div[2]") # Detailed Container location
    #     self.ele_DetailContainer_Date_Checkout_Text = self.ele_DetailContainer_Date_Checkout.text
    #     print(self.ele_DetailContainer_Date_Checkout_Text)
    #     self.assertEqual(self.ele_DetailContainer_Date_Checkout_Text, "Jan 23", "Failed: --> CheckOut is not matching")
    #     lg.error("Failed: --> CheckOut is not matching")
    #     time.sleep(2)        


        
    # def test_VerifyGuests (self):
    #     self.driver = webdriver.Chrome('./webDrivers/chromedriver')
    #     url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    #     self.driver.get(url1)
    #     self.driver.maximize_window()

    #     self.ele_DetailContainer = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]").click() #clicking on Detailed Container
    #     time.sleep(2)        



    #     self.ele_DetailContainer_Guest = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div/div[2]") # Detailed Container location
    #     self.ele_DetailContainer_Guest_Text = self.ele_DetailContainer_Guest.text
    #     print(self.ele_DetailContainer_Guest_Text)
    #     self.assertEqual(self.ele_DetailContainer_Guest_Text, "3 guests", "Failed: --> Guests is not matching")
    #     lg.error("Failed: --> Guests is not matching")
    #     time.sleep(10)
            

    # def test_VerifyNumberOfGuestsAvailable (self):
    #     self.driver = webdriver.Chrome('./webDrivers/chromedriver')
    #     url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    #     self.driver.get(url1)
    #     self.driver.maximize_window()

    #     # time.sleep(2)

    #     self.elem_NumberOfGuests = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/main/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[9]/div/div/div/div/div[1]/div[2]/div[3]")
    #     self.text = self.elem_NumberOfGuests.text
    #     print(self.text)

    #     # self.text = "8 guests . 3 bedrooms . 4 beds . 1 bath"
    #     self.t = self.text
    #     self.parts = self.t.split(" . ")
    #     print(" ---->   ",self.parts[0])
    #     # print(" ---->   ",self.parts[1])
    #     # print(" ---->   ",self.parts[2])
    #     # print(" ---->   ",self.parts[3])

    #     # self.guestParts = self.parts[0]
    #     # self.gbedroomParts = self.parts[1]
    #     # self.bedParts = self.parts[2]
    #     # self.bathParts = self.parts[3]


    #     # print("\n\n -------========0000000-------------------\n\n") 
        
    #     # self.splitGuestNum = self.guestParts.split(" ")
    #     # print(self.splitGuestNum[0])

    #     # if int(self.splitGuestNum[0]) > 3 :
    #     #     print("Guests are OKAAAYYYYYYYYYYYY")
    #     # else:
    #     #     print("FFFFFAAAAAAAIIIIILLLLLLEEEEEEEDDDDDDDDD")
        

    def Atest_ExtraFilters(self):

        self.driver = self.webdriver.Chrome('./webDrivers/chromedriver')
        url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
        self.driver.get(url1)
        self.driver.maximize_window()

        self.ele_MoreFilters = self.driver.find_element_by_xpath("//*[@id='menuItemButton-dynamicMoreFilters']/button")
        self.ele_MoreFilters.click()
        time.sleep(1)

        self.ele_Bedrooms = self.driver.find_element_by_xpath("/html/body/div[11]/section/div/div/div[2]/div[1]/div/div[2]/div/div[2]/button[2]")
        
        self.ele_Bedrooms.click()
        time.sleep(0.5)
        self.ele_Bedrooms.click()
        time.sleep(0.5)
        self.ele_Bedrooms.click()
        time.sleep(0.5)
        self.ele_Bedrooms.click()
        time.sleep(0.5)
        self.ele_Bedrooms.click()
        time.sleep(2)

        self.ele_Pool = self.driver.find_element_by_xpath("//*[@id='filterItem-facilities-checkbox-amenities-7']")

        # Scrooling to pool item 
        # self.driver.execute_script("arrguments[0].ScrollIntoView();", self.ele_Pool )
        self.ele_Pool.location_once_scrolled_into_view
        # Scrooling to pool item END

        self.ele_PoolValue = self.ele_Pool.get_attribute("value")
        print(self.ele_PoolValue)
        self.ele_Pool.click()
        time.sleep(2)

        self.ele_ShowStays = self.driver.find_element_by_xpath("/html/body/div[11]/section/div/div/footer/button")

        self.ele_ShowStays.click()
        time.sleep(2)




    #     self.text = "8 guests . 3 bedrooms . 4 beds . 1 bath"
    #     self.t = self.text
    #     self.parts = self.t.split(" . ")
    #     print(" ---->   ",self.parts[0])
    #     # print(" ---->   ",self.parts[1])
    #     # print(" ---->   ",self.parts[2])
    #     # print(" ---->   ",self.parts[3])

    #     # self.guestParts = self.parts[0]
    #     # self.gbedroomParts = self.parts[1]
    #     # self.bedParts = self.parts[2]
    #     # self.bathParts = self.parts[3]


    #     # print("\n\n -------========0000000-------------------\n\n") 
        
    #     # self.splitGuestNum = self.guestParts.split(" ")
    #     # print(self.splitGuestNum[0])

    #     # if int(self.splitGuestNum[0]) > 3 :
    #     #     print("Guests are OKAAAYYYYYYYYYYYY")
    #     # else:
    #     #     print("FFFFFAAAAAAAIIIIILLLLLLEEEEEEEDDDDDDDDD")

        # self.ele_OpenDetailOfProperty = self.driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
        # self.ele_OpenDetailOfProperty.click()

        self.ele_link = self.driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
        time.sleep(1)
        
        print(self.ele_link.get_attribute("href"))
        print(self.driver.current_url)
        time.sleep(150)


    
  
    def test_win(self):

        self.driver = self.webdriver.Chrome('./webDrivers/chromedriver')
        url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=filter_change&map_toggle=true&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&min_bedrooms=5&amenities%5B%5D=7"
        self.driver.get(url1)
        self.driver.maximize_window()
        
        # self.ele_OpenDetailOfProperty = self.driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
        # self.ele_OpenDetailOfProperty.click()
        
        self.window_before = self.driver.window_handles[0]

        self.ele_link = self.driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
        time.sleep(3)
        self.ele_link.click()
        self.window_after = self.driver.window_handles[1]
        time.sleep(3)
        
        self.driver.switch_to_window(self.window_after)
        time.sleep(3)
        # print(self.ele_link.get_attribute("href"))
        print(self.driver.current_url)
        time.sleep(2)

        self.ele_AllAminites = self.driver.find_element_by_xpath("//*[@id='site-content']/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div[3]/a")
        self.ele_AllAminites.click()
        time.sleep(3)

        self.ele_PoolUnderFacilities = self.driver.find_element_by_xpath("/html/body/div[11]/section/div/div/div[3]/div/div/section/div[2]/div[3]/div[4]/div")
        self.ele_PoolUnderFacilitiesText = self.ele_PoolUnderFacilities.text
        print(" --->   ",self.ele_PoolUnderFacilitiesText)
        time.sleep(10)







    
    # def test_HomePageMetaTitles(self):
    #     title = "Hello"
    #     self.assertEqual("Hello", title, "FAILED:: Page Title is wrong")
        
        
    # def test_SpecialityListingMetaTitles(self):
    #     title = "Hello"
    #     self.assertEqual("Hello", title, "FAILED:: Title is wrong")
        
    # def test_TreatmentListingMetaTitles(self):
    #     title = "Hello"
    #     self.assertEqual("Hellpo", title, "FAILED:: Title is wrong")
        
    # def test_ConditionListingMetaTitles(self):
    #     title = "Hello"
    #     self.assertEqual("Hello", title, "FAILED:: As Title is wrong")
        
    # def  test_BookableDoctorProfileMetaTitles(self):
    #     title = "Hello"
    #     self.assertEqual("Hello", title, "FAILED:: Title is wrong")
        
    # def  test_NonBookableDoctorProfileMetaTitles(self):
    #     title = "Hello"
    #     self.assertEqual("Hello", title, "FAILED:: Title is wrong")
        
if __name__== "__main__":
    ut.main()


