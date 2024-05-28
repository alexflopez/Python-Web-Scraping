from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


# Chrome driver for selenium
def chrome_driver(url: str):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver


# Expanding the filter view page when accessing it to retrieve at least little more data
def expand_filter(path: str, driver) -> None:
    element = driver.find_element(By.XPATH, path)
    return element.click()


# List to store the data retrieved
sort = []
logo = []
name = []
percentage = []
price = []
rating = []
release = []
ends = []
started = []


# Main chrome driver
driver = chrome_driver('https://steamdb.info/sales/')

# Expanding table
expand_filter('//*[@id="dt-length-0"]/option[8]', driver)

# Accessing all data table
responses = driver.find_elements(By.TAG_NAME, "tr")


rows = driver.find_elements(By.XPATH, "//table[@id='DataTables_Table_0']/tbody/tr")
# Get the count of rows
row_count = len(rows)
#print("Number of rows:", row_count)

i = 1

# //tr/td[1]
for response in responses:
    # print(response.text)
    sort.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[1]').text)
    logo.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[2]/a/img').get_attribute("src"))
    name.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[3]').text)
    percentage.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[4]').text)
    price.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[5]').text)
    rating.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[6]').text)
    release.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[7]').text)
    ends.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[8]').text)
    started.append(response.find_element(By.XPATH, '//tr['+str(i)+']/td[9]').text)

    # print(name)
    i += 1     

    if i == row_count + 1:
        break

driver.quit()

df = pd.DataFrame({"sort": sort,
                   "logo": logo,
                   "name": name,
                   "percentage": percentage,
                   "price": price,
                   "rating": rating,
                   "release": release,
                   "ends": ends,
                   "started": started})

print(df)

df.to_csv('response.csv', index=False)
