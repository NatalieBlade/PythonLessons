from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math


@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(25)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#@pytest.mark.xfail
def test_check_urls(browser, link):
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    # browser.implicity_wait(20)
    answer = str(math.log(int(time.time())))

    text_area = browser.find_element(By.CSS_SELECTOR, ".textarea")
    text_area.send_keys(answer)

    # button = browser.find_element_by_class_name("submit-submission")
    # button.click()
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    # browser.implicity_wait(25)
    text_el = browser.find_element_by_class_name("smart-hints__hint")
    assert text_el.text == 'Correct!', f"Получили {text_el} instead of 'Correct!'"


if __name__ == "__main__":
    pytest.main()