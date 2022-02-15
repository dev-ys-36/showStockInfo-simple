from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

stock_list_data = {
    "삼성전자",
    "하이닉스",
    "LG전자",
    "카카오",
    "두산중공업",
    "삼전",
    "테스트"
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

for stock_list in stock_list_data:
    
    driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + stock_list)

    try:
        
        driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]")
        
    except NoSuchElementException:
        
        print(stock_list + " 주식은 존재하지 않습니다, 주식 이름을 다시 확인해 주세요!")

        continue

    stock_name = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[1]/div/h3/a/span[1]")
    stock_krx = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[1]/div/h3/a/em")
    stock_status_time = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[2]/div[1]/p/em")
    stock_status_up_down = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[1]/div/h3/a/span[2]/span[2]/span[1]")
    stock_price = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[1]/div/h3/a/span[2]/strong")
    stock_status_1 = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[1]/div/h3/a/span[2]/span[2]/em[1]")
    stock_status_2 = driver.find_element(By.XPATH, "//*[@id=\"_cs_root\"]/div[1]/div/h3/a/span[2]/span[2]/em[2]")

    info = {
        
        "stock_name": stock_name.text,
        "stock_krx": stock_krx.text,
        "stock_status_time": stock_status_time.text,
        "stock_status_up_down": stock_status_up_down.text,
        "stock_price": stock_price.text,
        "stock_status": stock_status_1.text + " " + stock_status_2.text 
        
    }

    list_ = []

    list_.append(info)

    for list__ in list_:

        if (list__["stock_status_up_down"] == "하락" or list__["stock_status_up_down"] == "전일대비 하락"):

            print(list__["stock_name"] + "(" + list__["stock_krx"] + ") | "  + list__["stock_price"] + " / ▼ " + list__["stock_status"] + " | " + list__["stock_status_time"])

        elif (list__["stock_status_up_down"] == "상승" or list__["stock_status_up_down"] == "전일대비 상승"):

            print(list__["stock_name"] + "(" + list__["stock_krx"] + ") | "  + list__["stock_price"] + " / ▲ " + list__["stock_status"] + " | " + list__["stock_status_time"])

        elif (list__["stock_status_up_down"] == "보합" or list__["stock_status_up_down"] == "전일대비 보합"):

            print(list__["stock_name"] + "(" + list__["stock_krx"] + ") | " + list__["stock_price"] + " / - " + list__["stock_status"] + " | " + list__["stock_status_time"])

        else:

            print(list__["stock_name"] + "(" + list__["stock_krx"] + ") | " + "UNKNOWN")

    
