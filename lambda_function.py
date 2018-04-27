from selenium import webdriver


def lambda_handler(event, context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--v=99")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--homedir=/tmp")
    options.binary_location = "./bin/headless-chromium"

    driver = webdriver.Chrome(
        "./bin/chromedriver", chrome_options=options)
    driver.get("https://www.google.co.jp")
    title = driver.title
    driver.close()

    return title


if __name__ == "__main__":
    title = lambda_handler(None, None)
    print("title:", title)
