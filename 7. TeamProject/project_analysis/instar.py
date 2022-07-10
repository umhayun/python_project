## 인스타 해시태그 크롤링 함수
def start_instar():
    from selenium import webdriver
    import time
    driver = webdriver.Chrome("c:\webdriver\chromedriver.exe")
    driver.get("https://www.instagram.com")
    time.sleep(2)
    email = 'djagkdbs@naver.com'  
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)
    password = 'dytjq7169' 
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(password)
    input_pw.submit()
    time.sleep(3)
    return driver
def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/"+word
    return url
def select_first(driver):
    import time
    first = driver.find_element_by_css_selector("div._aagw")
    first.click()
    time.sleep(4)
def move_next(driver):
    import time
    right = driver.find_element_by_css_selector("div._aaqg._aaqh>button")
    right.click()
    time.sleep(4)
def get_content(driver):
    import re
    from bs4 import BeautifulSoup
    import unicodedata  
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    try:
        content = soup.select("div._a9zs > span")[0].text
        content = unicodedata.normalize('NFC', content)
    except:
        content = ' '
    tags = re.findall(r'#[^\s#,\\]+', content)
    date = soup.select("time._aaqe")[0]['datetime'][:10]
    try:
        like = soup.select("div._aacl._aaco._aacw._aacx._aada._aade > span")[0].text
    except:
        like = 0
    try: 
        place = soup.select("a.oajrlxb2")[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place = ''
    data = [content, date, like, place, tags]
    return data 

def crawling(words):
    driver=start_instar()
    import time
    results=[]
    for word in words:
        url=insta_searching(word)
        driver.get(url)
        time.sleep(10)
        select_first(driver)
        target=1000
        for i in range(target):
            try:
                data = get_content(driver)
                results.append(data)
                move_next(driver)
            except:
                time.sleep(3)
                move_next(driver)
    return results