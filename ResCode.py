import requests
import time
import logging
from selenium import webdriver
from plyer import notification
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 推荐注册为任务或自行改为服务
# 该脚本实际上是断网自动检测联网


username = '<u username>'
password = '<u password>'    #你的账号密码

# 配置日志记录
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志记录级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志消息格式
    handlers=[
        logging.FileHandler('netSts.log'),  # 将日志记录到文件
        # logging.StreamHandler()  # 将日志记录到控制台
    ]
)

def show_notification(title, message):
    # 气泡弹窗提醒
    notification.notify(
        title=title,
        message=message,
        timeout=3  # timeout 是通知持续时间，单位为秒
    )

def login():
    # Chromium 和 ChromeDriver 的路径
    chromium_path = r"<u path>"  # Chromium 浏览器的实际路径
    chromedriver_path = r"<u path>"  # ChromeDriver 的实际路径

    # 配置 ChromeDriver 和 Chromium
    chrome_options = Options()
    chrome_options.binary_location = chromium_path  # 指定 Chromium 浏览器的位置
    chrome_options.add_argument("--headless")  # 无头模式（可选）::即隐藏浏览器运行

    # 初始化 Chrome 浏览器
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # 打开网页
        driver.get("https://p.njupt.edu.cn/a79.htm")    #认证网站

        # 查找用户名和密码输入框
        username_field = driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[7]/form/input[3]')
        username_field.send_keys(username)  # 输入用户名

        password_field = driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[7]/form/input[4]')
        password_field.send_keys(password)  # 输入密码

        operator_select = driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[7]/select').click()
        # 选择运营商
        driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[7]/select/option[4]').click()
        # 注明,这步操作在选择运营商,这里的option[4]是移动,option[3]是电信,option[2]是校园网

        Dic_end = driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[7]/form/input[2]').click()
        # 登陆

    finally:
        # 关闭浏览器
        driver.quit()

def check_network():
    try:
        # 尝试请求一个可靠的公共网址来检测网络连接
        response = requests.get("https://www.baidu.com", timeout=5)
        # 如果状态码是 200，则网络连接正常
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        # 处理网络连接错误
        pass
    return False

def main():
    while True:
        if check_network():
            logging.info("Network is connected.")
        else:
            logging.error("Network is disconnected.")
            show_notification("Reminder", f"Net Disconnect")

            login()
        # 每san秒钟检测一次
        # time.sleep(1)

if __name__ == "__main__":
    main()
