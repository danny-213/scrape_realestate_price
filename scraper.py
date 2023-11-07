from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-features=PermissionsPolicy")  # Ensure GUI is off
chrome_options.add_argument('--permissions-policy="geolocation=(self)"')
# Set path to chromedriver as per your configuration
webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_options.binary_location = webdriver_path

# Initialize Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

df = pd.DataFrame(columns=['Title','Address','Attributes','Price'])
for p in range(1,100): 
    print(f"reading page {p}")
    url = f"https://mogi.vn/mua-dat?cp={p}"

    # Open the URL in Chrome browser
    driver.get(url)
    time.sleep(10)
    # Get the page source and parse it with BeautifulSoup
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')



    # Find the <ul> element with class "props"
    ul_props = soup.find('ul', class_='props')
    prop_title = ul_props.find_all('h2', class_='prop-title')
    title = [i.get_text() for i in prop_title]
    prop_addr = ul_props.find_all('div', class_='prop-addr')
    addr = [i.get_text() for i in prop_addr]
    prop_attr = ul_props.find_all('ul', class_='prop-attr')
    attr = [i.get_text() for i in prop_attr]
    prop_price = ul_props.find_all('div', class_='price')
    price = [i.get_text() for i in prop_price]
    data = {'Title':title, 
            'Address': addr,
            'Attributes':attr,
            'Price':price}

    df_page = pd.DataFrame(data) 
    df = pd.concat([df,df_page],ignore_index=True)


df.to_excel("pricing-data.xlsx")


# Close the browser window
driver.quit() 

