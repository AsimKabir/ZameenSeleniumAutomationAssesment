import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _pytest.mark import expression
import unittest 




def applyFiltersOnHomePage():
    driver = webdriver.Chrome('./webDrivers/chromedriver')
    url = "https://www.airbnb.com/"
    # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Now entering location Rome, Italy on Home page
    ele_EnterLocation = driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Rome, Italy Location element 
    ele_EnterLocation.send_keys("Rome, Italy")
        # element = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div")
        # element.send_keys("Rome, Italy")
    # time.sleep(1)
    # Now Clicking on the In date on home page
    ele_EnterDateField = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]") # CheckIn field element
    ele_EnterDateField.click()
    time.sleep(1)
    # Now entering Check In date on home page
    ele_EnterCheckInDate = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div") # CheckIn date element
    ele_EnterCheckInDate.click()
    time.sleep(1)
    # Now entering CheckOut date on home page
    ele_EnterCheckOutDate = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]/div/div/div") # Check out date element
    ele_EnterCheckOutDate.click()
    time.sleep(1)
    # Now clicking on the guest field of home page
    ele_GuestField = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div") # Guest Field Element
    ele_GuestField.click()
    time.sleep(1)

    # Now adding adults as guests on home page
    ele_AdultGuest = driver.find_element_by_xpath("//*[@id='stepper-adults']/button[2]") # Adult guests alement on home page
    ele_AdultGuest.click()
    # time.sleep(1)
    ele_AdultGuest.click()
    time.sleep(1)
    # Now entering child Guest on home page
    ele_ChildGuest = driver.find_element_by_xpath("//*[@id='stepper-children']/button[2]") # Child guest element on home page
    ele_ChildGuest.click()
    # time.sleep(2)

    # Now clicking on the element Search Button
    ele_SearchField = driver.find_element_by_xpath("//button[@class='_1mzhry13' and @type='button']") # Button search element on home page
    ele_SearchField.click()
    time.sleep(1)
    return driver


def verifyIsNumberofGuestsAccomodate():
    # driver = webdriver.Chrome('./webDrivers/chromedriver')
    # driver.get("https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=filter_change&gps_lat=32.252380099999996&gps_lng=75.1662008")
    # driver.maximize_window()
    # driver.implicitly_wait(10)   
   
    driver = applyFiltersOnHomePage()
    time.sleep(10)
    ele_guests = driver.find_elements_by_xpath("//div[@class='_kqh46o' and @style='margin-top: 9px;']")
    print("Length of total cards is :: --->> " , len(ele_guests))

    guests = []
    i=0
    for x in ele_guests:
        t = x.text
        parts = t.split("guests")
        temp = parts[0]
        guests.append(temp)
        i = i + 1

    for y in guests:
        assert int(y) >= 3 , "Property Does Not Accomudate the Number of Guests"
        print(y)

   

def VerifyAppliedFiltersAreCorrect():

    driver = applyFiltersOnHomePage()
    time.sleep(10)
    # driver = webdriver.Chrome('./webDrivers/chromedriver')
    # driver.get("https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=filter_change&gps_lat=32.252380099999996&gps_lng=75.1662008")
    # driver.maximize_window()
    # driver.implicitly_wait(10)   
    # print("PASSEEDD ASIM")

    location = "Rome, Italy"
    checkin = "Jan 16"
    checkout = "Jan 23"
    guests = 3

    

    ################################### Getting Filters from Container by Opening code Starts #######################################################################################################################################    

    # Clicking on the top Header filter to open and get filters details
    ele_DetailContainer = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]") #clicking on filter of Detailed Container element
    ele_DetailContainer.click()
    time.sleep(2)    

        
    # Now getting Location by Opening Container
    ele_DetailContainer_Location = driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Detailed Container location element after opening
    ele_DetailContainer_Location_Text = ele_DetailContainer_Location.get_attribute("value")
    print("by opening --->  ", ele_DetailContainer_Location_Text)
    # time.sleep(2)        

    # Now getting CheckIn Date by Opening Container
    ele_DetailContainer_Date_Checkin = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]/div/div[2]") # Detailed Container location Date CheckIn by Opening
    ele_DetailContainer_Date_Checkin_Text = ele_DetailContainer_Date_Checkin.text
    print("by opening --->  ",ele_DetailContainer_Date_Checkin_Text)
    # time.sleep(2)        

    # Now getting CheckOut Date by Opening Container
    ele_DetailContainer_Date_Checkout = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[3]/div[1]/div/div[2]") # Detailed Container location Date Checkout by Opening
    ele_DetailContainer_Date_Checkout_Text = ele_DetailContainer_Date_Checkout.text
    print("by opening --->  ",ele_DetailContainer_Date_Checkout_Text)
    time.sleep(5)        
    # Now getting Guests by Opening Container
    saasa = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div/div[1]")
    saasa.click()
    time.sleep(2)
    ele_GuestsAdultsElement = driver.find_element_by_xpath("//div[@class='_1665lvv']//span[@data-testid='stepper-adults-value']")
    ele_GuestsAdultsElementText = ele_GuestsAdultsElement.text
    print("By Opening Adults are: --->", ele_GuestsAdultsElementText)

    ele_GuestsChildernElement = driver.find_element_by_xpath("//div[@class='_1665lvv']//span[@data-testid='stepper-children-value']")
    ele_GuestsChildernElementText = ele_GuestsChildernElement.text
    print("By Opening Childerns are: --->" ,ele_GuestsChildernElementText)

    ele_DetailContainer_Guest_Text = int(ele_GuestsAdultsElementText) + int(ele_GuestsChildernElementText)  
    ##################
    # ele_DetailContainer_Guest = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div/div[2]") # Detailed Container Guests element
    # ele_DetailContainer_Guest_Text = ele_DetailContainer_Guest.text
    # print("by opening --->  ",ele_DetailContainer_Guest_Text)
    time.sleep(1)
    ####################################### Getting Filters from Container by Opening code Ends ############################################################################################################################


    ########### Applying assert commands //////////
    assert ele_DetailContainer_Location_Text == location , "Failed Due to not matched"
    assert ele_DetailContainer_Date_Checkin_Text == checkin , "Failed Due to not matched"
    assert ele_DetailContainer_Date_Checkout_Text == checkout , "Failed Due to not matched"
    assert ele_DetailContainer_Guest_Text == guests , "Failed Due to not matched"



def VerifyDetailedPageMatchesExtraFilters ():
    driver = applyFiltersOnHomePage()
    # driver = webdriver.Chrome('./webDrivers/chromedriver')
    # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    # driver.get(url1)
    # driver.maximize_window()

    # Now clicking on option More Filters to open the more filters pop-up
    ele_MoreFilters = driver.find_element_by_xpath("//*[@id='menuItemButton-dynamicMoreFilters']/button") # More filters pop-op opening element
    ele_MoreFilters.click()
    time.sleep(1)

    # Now Locating Element to add number of beds
    ele_Bedrooms = driver.find_element_by_xpath("//*[@id='filterItem-rooms_and_beds-stepper-min_bedrooms-0']/button[2]") # Bedroom element on morefilter pop-up
        
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(2)

    # Now findind element Pool 
    ele_Pool = driver.find_element_by_xpath("//*[@id='filterItem-facilities-checkbox-amenities-7']") # pool element on more filters pop-up
    #Scrooling to pool item 
    ele_Pool.location_once_scrolled_into_view
    # ele_PoolValue = ele_Pool.get_attribute("value")
    # print(ele_PoolValue)
    ele_Pool.click()
    time.sleep(2)

    # Finding button Show Stays on more filters pop-up
    ele_ShowStays = driver.find_element_by_xpath("//button[@data-testid='more-filters-modal-submit-button']") # Button show stays button Element 
    ele_ShowStays.click()
    time.sleep(10)

    ################### ---------------------------------------------------------
    ### assert list accumodate the number of bedrooms
    ################### ---------------------------------------------------------

    ############### Starts --> Opening detail of first property and verify pool is available on new page ###############################################
    # window_before = driver.window_handles[0]

    # Opening detail of first property on new page
    ele_link = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
    time.sleep(2)
    ele_link.click()
    window_after = driver.window_handles[1]
    time.sleep(2)
    # Navigates the driver to the new opened page
    driver.switch_to_window(window_after)
    time.sleep(2)
    # print(ele_link.get_attribute("href"))
    print(driver.current_url)
    time.sleep(2)

    # find element "Show all Aminites"
    ele_AllAminites = driver.find_element_by_xpath("//*[@id='site-content']/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div[3]/a") # button Show all aminites""
    ele_AllAminites.click()
    time.sleep(2)

    # Opeing The pop-up Amenites
    ele_PoolUnderFacilities = driver.find_element_by_xpath("/html/body/div[11]/section/div/div/div[3]/div/div/section/div[2]/div[11]/div[4]/div")
    # Getting text Pool on the Aminites pop-up
    ele_PoolUnderFacilitiesText = ele_PoolUnderFacilities.text
    print(" ---asasasasas---->   ",ele_PoolUnderFacilitiesText)

    assert ele_PoolUnderFacilitiesText == "Pool" , "Pool is not available under the Facilites Heading"

    time.sleep(10)

    ############### Ends --> Opening detail of first property and verify pool is available on new page ###############################################




def VerifyPropertiesCanAccommodateNumberOfGuests ():
    driver = applyFiltersOnHomePage()
    time.sleep(8)
    # driver = webdriver.Chrome('./webDrivers/chromedriver')
    # driver.get("https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=filter_change&gps_lat=31.4573521&gps_lng=74.3000763")
    # driver.maximize_window()
    # driver.implicitly_wait(10)   

    ele_bedrooms = driver.find_elements_by_xpath("//div[@class='_kqh46o' and @style='margin-top: 9px;']")
    print("Length of total cards is :: --->> " , len(ele_bedrooms))

    rooms = []
    i=0
    for x in ele_bedrooms:
        t = x.text
        parts = t.split(" ")
        temp = parts[3]
        print(temp)
        # temp1 = parts[4]
        # print(temp1)
        rooms.append(temp)
        i = i + 1

    for y in rooms:
        assert int(y) >= 5 , "Property Does Not Accomudate the Number of Bedrooms"
        print(y)


    




def test_VerifyPropertyDisplayedOnMapCorrectly ():
    driver = applyFiltersOnHomePage()
    driver = webdriver.Chrome('./webDrivers/chromedriver')
    url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    driver.get(url1)
    driver.maximize_window()
    time.sleep(5)
    print("FINE ASIMMM")
    # ele_to_hover_over =driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]")
    # hover = ActionChains(driver).move_to_element(ele_to_hover_over)
    # hover.perform()

    ########################## Getting data to compare with the property on the map ############################
    # driver = webdriver.Chrome('./webDrivers/chromedriver')
    # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-17&checkout=2021-01-24&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click&min_bedrooms=5&amenities%5B%5D=7&query=Rome%2C%20Italy"
    # driver.get(url1)
    # driver.maximize_window()
     
    # time.sleep(5)


    ele_PropertyName = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div")
    propertyNameText = ele_PropertyName.text
    print(propertyNameText)

    ele_PropertyLocation = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]")
    propertyLocationText = ele_PropertyLocation.text
    print(propertyLocationText)

    # ele_PropertyRating = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[5]/div[1]/span/span[2]")
    # propertyRatingText = ele_PropertyRating.text
    # print(propertyRatingText)

    # ele_PropertyReviews = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[5]/div[1]/span/span[3]")
    # propertyReviewsText = ele_PropertyReviews.text
    # print(propertyReviewsText)

    # ele_PropertyPrice = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div[1]/span/span")
    # propertyPriceText = ele_PropertyPrice.text
    # print(propertyPriceText)
    ############################################################################################################ 
    print("\n ------------ \n Reached End of Page \n ---------------\n")

    action = ActionChains(driver)

    ele_to_mouse_hover = driver.find_elements_by_xpath("//div[@class='_1nz9l7j']")
    print(len(ele_to_mouse_hover))
    action.move_to_element(ele_to_mouse_hover[0]).perform()
    # time.sleep(10)

    time.sleep(15)
    ele_on_map = driver.find_element_by_xpath("//div[@style='align-items: center; background-color: rgb(34, 34, 34); border-radius: 28px; box-shadow: rgba(0, 0, 0, 0.24) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px; color: rgb(255, 255, 255); display: flex; height: 28px; justify-content: center; padding: 0px 8px; position: relative; white-space: nowrap;']")
    # time.sleep(2)
    ele_on_map.click()

    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()

    # hello = driver.find_element_by_xpath("//div[@class='_1q6k59c']//span[@class='_11ry7lz' and @aria-hidden='true']").text
    # ele_hello_text = ele_hello.text
    # print (hello)
    # print(len(ele_hello))

    mapPropertyNameText= driver.find_elements_by_xpath("//div[@class='_v3gzda1']//ol[@class='_194e2vt2']//li")
    print(mapPropertyNameText[0].text)
 
    mapPropertyLocationText = driver.find_element_by_xpath("//div[@class='_1q6k59c']//div[@class='_1isz8pdq']").text
    print(mapPropertyLocationText)

    # ppxpxx = driver.find_element_by_xpath("//div[@class='_1q6k59c']//span[@class='_11ry7lz']']").text
    # print(ppxpxx)

    print("\n ------------ \n Reached End of Page \n ---------------\n")
    time.sleep(5)


    assert propertyNameText == mapPropertyNameText, "Location Doesnot matches on MAP"

    assert propertyLocationText == mapPropertyLocationText, "Location Doesnot matches on MAP"