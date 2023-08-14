from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


df = pd.DataFrame()

#sending the bot at the url
driver = webdriver.Chrome()
to_be_searched_number = 90000000
while to_be_searched_number < 90000005:
    #driver.execute_cdp_cmd("Emulation.clearGeolocationOverride", params)
    driver.get("https://number.xmohamed.com")
    wait = WebDriverWait(driver, 10)

    #sending details on the first page
    number = driver.find_element(By.CLASS_NAME, "q-field__native")
    number.clear()
    number.send_keys(to_be_searched_number)

    #dropdown = driver.find_element(By.CLASS_NAME,'q-select__dropdown-icon')
    input_element = driver.find_element(By.XPATH,"//input[contains(@class, 'q-field__input') and contains(@class, 'q-placeholder') and contains(@class, 'col')]")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(input_element)).click()
    input_element.clear()
    input_element.send_keys("Oman")
    driver.implicitly_wait(5)
    countries = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'q-item__label') and contains(text(),'Oman')]")))
    wait.until(EC.visibility_of(countries)).click()

    button = driver.find_element(By.CSS_SELECTOR,".input.btn .q-btn")
    button.click()

    #interactions of bot on the second page
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "q-table")))
        ''' this is the piece of code that handles the logic for the second dropdown where we wish to select "All" 
        dropdown_pg = driver.find_elements(By.CLASS_NAME,'q-icon.notranslate.material-icons.q-select__dropdown-icon')
        wait.until(EC.element_to_be_clickable(dropdown_pg[-1])).click()
        #options =driver.find_elements(By.CLASS_NAME, 'q-item__label')

        options = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='q-item__label' and contains(span/text(), 'All')]")))
        wait.until(EC.element_to_be_clickable(options)).click()
        '''
        table_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "q-table")))
        table_rows = table_element.find_elements(By.TAG_NAME, "tr")
        new_list = []
        new_list.append(to_be_searched_number)
        for row in table_rows:
            name = row.find_elements(By.CLASS_NAME, "text-center")[-1].text
            if not(name == "Name" or name=="Name\narrow_upward"):
                new_list.append(name)
        new_list_df = pd.DataFrame([new_list])
        df = df.append(new_list_df)
        print(str(to_be_searched_number) + "record found")
        to_be_searched_number +=1
    #print(options.text)
        '''
        options.clear()
        for option in options:
            if option.text == 'All':
                WebDriverWait(driver,100000).until(EC.visibility_of(option)).click()
                break
        #wait()

        #'''
    except:
        try:
            to_be_searched_number += 1
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,"q-card.bg-teal.text-white.cairo-all")))
            print(str(to_be_searched_number) + "No name detected")
        except:
            print("Neither condition was met. Driver bugged")

#df.to_csv('output.csv',index=False)
print("Scrape Succesful")
#wait()
driver.quit()