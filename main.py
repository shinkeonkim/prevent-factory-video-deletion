import os, time, random

from selenium.webdriver import Chrome, ChromeOptions
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv(verbose=True)

def rsleep(t = 1000):
    time.sleep(random.randint(0, t)/1000)
  

def login(browser: Chrome):
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    
    signin_button = browser.find_element_by_xpath("//a[contains(@href, 'accounts')]")
    signin_button.click()

    time.sleep(1)
    rsleep(2000)
    
    email_input = browser.find_element_by_css_selector('input[type=email]')
    
    for letter in email:
        email_input.send_keys(letter)
        rsleep()
    
    time.sleep(1)
    rsleep(2000)
    
    next_button = browser.find_elements_by_css_selector('button')[2]
    rsleep(2000)
    next_button.click()
    rsleep(2000)
        
    
    password_input = browser.find_element_by_css_selector('input[type=password]')
    for letter in password:
        password_input.send_keys(letter)
        rsleep(1000)    

    time.sleep(4)   
    rsleep(2000)
    
    next_button = browser.find_elements_by_css_selector("button")[1]
    rsleep(2000)
    time.sleep(random.randint(0, 2000)/1000)    
    next_button.click()
    time.sleep(2)   
    rsleep(2000)
    
    confirm_button = browser.find_elements_by_css_selector("div[role=button]")
    rsleep(2000)
    if(len(confirm_button)>0):
        confirm_button[1].click()


def move_to(browser : Chrome, link: str):
    browser.get(link)
    time.sleep(4)


def add_comment(browser: Chrome, comment: str):
    time.sleep(25)
    browser.execute_script("window.scrollTo(0, 600)") 
    browser.get_screenshot_as_file("test_screenshot.png")
    comment_input = browser.find_element_by_css_selector("div#placeholder-area")

    entering_comment_actions = ActionChains(browser)
    entering_comment_actions.move_to_element(comment_input)
    entering_comment_actions.click()
    
    for letter in comment:
        entering_comment_actions.send_keys(letter)
        wait_time = random.randint(0, 1000)/1000
        entering_comment_actions.pause(wait_time)
    entering_comment_actions.perform()
    
    time.sleep(1)
    rsleep(1000)
    
    send_comment_button = browser.find_element_by_id('submit-button')
    send_comment_button.click()
    

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=oiQUD5WBChk"
    message = "팩토리님은 천재에요~❤️"
    chrome_driver = os.path.join('chromedriver')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument(f'user-agent={user_agent}')

    browser = Chrome(chrome_driver, options=chrome_options)
    browser.get("https://www.youtube.com")
    try:
        login(browser)
        time.sleep(1)
        rsleep(2000)
        move_to(browser, url)
        add_comment(browser, message)
        time.sleep(2)
        print("댓글이 달렸습니다.")
    except Exception as e:
        print(e)
    finally:
        browser.close()
