import time
import threading
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import shutil  # to verify geckodriver is available





# Fixture to initialize and quit the WebDriver
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# 1. Test: Page Load Time
def test_streamlit_page_load_time(driver):
    start = time.time()
    driver.get("http://localhost:8501")
    load_time = time.time() - start
    print(f"Page load time: {load_time:.2f} seconds")
    assert load_time < 5, "Page load too slow!"

# 2. Test: Concurrent User Sessions
def test_concurrent_user_sessions():
    def simulate_user():
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        try:
            driver.get("http://localhost:8501")
            # Perform actions as needed
            time.sleep(2)  # Simulate user interaction duration
        finally:
            driver.quit()

    threads = []
    num_users = 10  # Number of concurrent users to simulate

    for _ in range(num_users):
        thread = threading.Thread(target=simulate_user)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# 3. Test: Streamlit opens in Firefox and exits immediately
def test_access_streamlit_with_firefox():
    firefox_options = FirefoxOptions()
    firefox_options.headless = True  # Run in headless mode

    driver = None
    try:
        driver = webdriver.Firefox(options=firefox_options)
        driver.get("http://localhost:8501")
        time.sleep(2)  # Allow time for the page to load
        title = driver.title
        print("Firefox page title:", title)
        assert "Streamlit" in title or len(title.strip()) > 0, "Streamlit page did not load in Firefox"
    finally:
        if driver:
            driver.quit()
