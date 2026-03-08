from selenium import webdriver
from selenium.webdriver.common.by import By
"""
#### 4. **Find the “Edit” Link for Row 4**
Each row ends with “edit” and “delete” links.  
🛠️ Challenge: Locate the “edit” link for the row that starts with `Iuvaret4`. What’s its `href` or any unique attribute?
"""

def test_edit_element():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/challenging_dom")
    row_cols = driver.find_element(By.XPATH, "//*[text()='Iuvaret4']/parent::tr")
    edit_link = row_cols.find_element(By.XPATH, ".//a[text()='edit']")
    href_value = edit_link.get_attribute("href")
    print(f"'edit' link href for row starting with 'Iuvaret4': {href_value}")
    driver.close()


