def test_load_google(driver):
    """Example test to load the Google page"""
    driver.get('https://google.com')
    assert driver.title == 'Google'
