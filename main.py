from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI()


@app.get('/title')
def title():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.google.com/")
    title = driver.title
    driver.quit()
    return title
