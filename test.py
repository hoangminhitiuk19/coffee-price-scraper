browser = .chromium.launch(headless=False)  # Set headless=True for automation
page = browser.new_page()
url = "https://giacaphe.com/gia-ca-phe-noi-dia/"
page.goto(url)