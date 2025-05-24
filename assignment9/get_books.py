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
    # driver.get(
    #     "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    raw_result = driver.get(
        "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    print(raw_result)
    results_list = driver.find_elements(
        By.CSS_SELECTOR, 'li.cp-search-result-item')
    print(results_list)

    book_list = []

    for element in results_list:
        # print(element)
        book_dict = {}
        book_title = element.find_element(
            By.CSS_SELECTOR, 'span.title-content')
        print(book_title)
        if (book_title):
            book_dict['Title'] = book_title.text
        else:
            book_dict['Title'] = 'title not found'
        print(book_dict)
        author = element.find_element(
            By.CLASS_NAME, 'author-link'
        )
        book_dict['Author'] = author.text
        print(author)
        format_year = element.find_element(
            By.CLASS_NAME, 'cp-screen-reader-message'
        )
        book_dict['Format_Year'] = format_year.text
        print(format_year)

        # append to dictionary
        book_list.append(book_dict)

    df = pd.DataFrame(book_list)
    print(df)

    # save the dataframe to a CSV
    df.to_csv("get_books.csv", index=False)
    # write to json file
    with open('get_books.json', 'w') as file:
        file.write(json.dumps(book_list))


except:
    print("An exception has occurred")
