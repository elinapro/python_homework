from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

# Configure Chrome to run in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

try:
    raw_result = driver.get(
        "https://owasp.org/www-project-top-ten/")
    print(raw_result)

    (sec_main) = driver.find_element(
        By.CSS_SELECTOR, '[id="sec-main"]')  # our starting point

    links = []  # list of links
    if ((sec_main)):
        top_10_list = (sec_main).find_elements(
            By.XPATH, 'ul[2]/li/a')  # up to the parent div
        if top_10_list:
            # loop over the links in the top 10 lists
            for link in top_10_list:
                print(f"{link.text}: {link.get_attribute('href')}")
                name = link.text.strip()
                url = link.get_attribute("href")
                if name and url:
                    links.append({"name": name, "url": url})

    print(links)
    driver.quit()

    df = pd.DataFrame(links)
    print(df)

    # save the dataframe to a CSV
    df.to_csv("owasp_top_10.csv", index=False)

except:
    print("An exception has occurred")
