# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)
# options.add_argument("--headless")
# 1. Login
# browser.get("http://fb.com/login")
# username = browser.find_element("name","email")
# password = browser.find_element("name","pass")
# submit   = browser.find_element("name","login")
# username.send_keys("kien0207")
# password.send_keys("DuongKien@2022")
# submit.click()
# 2. Go to http://lgedv.payroll.lge.com/Attendance/index/Summary
# browser.get("http://fb.com/me")


import requests
from bs4 import BeautifulSoup

# Create a session
with requests.Session() as session:
    # Do a GET request to the login page
    login_url = 'https://m.facebook.com/login'
    response = session.get(login_url)

    # Parse the HTML to find default values
    soup = BeautifulSoup(response.content, 'html.parser')
    form = soup.find('form', id='login_form')
    default_values = {input['name']: input.get('value', '') for input in form.find_all('input')}

    # Set your email and password
    email = 'kien0207'
    password = 'DuongKien@2022'

    # Combine default values with login data
    data = default_values
    data['email'] = email
    data['pass'] = password
    data['login'] = 'Log In'

    # Send the login request
    response = session.post(login_url, data=data)

    profile_url = 'https://m.facebook.com/kien0207'
    response = session.get(profile_url)
    profile_html = response.content
    soup = BeautifulSoup(profile_html, 'html.parser')
    name_element = soup.find('title')
    user_name = name_element.text.split(' | ')[0]
    print(f"User's name: {user_name}")



