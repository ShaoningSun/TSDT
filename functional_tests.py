from selenium import webdriver  # 从selenium引入webdriver

browser = webdriver.Chrome()  # 启动一个selenium “webdriver”去弹出一个Chrome窗口
browser.get('http://localhost:8000')  # 用它打开本地网页

assert 'Django' in browser.page_source  # 这是测试断言，检查在网页中有没有“Django”这个词
