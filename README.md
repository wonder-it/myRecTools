# Campus-network-login-Njupt
Campus network login Njupt, for PC Web

# 自动检测网络并登录脚本

# 概述

这个 Python 脚本用于自动检测网络连接状态。如果检测到网络断开，脚本会显示通知并尝试通过 Chromium 浏览器登录指定网站。脚本使用 `requests` 库检测网络状态，使用 `selenium` 库自动化浏览器操作，并使用 `plyer` 库显示通知。


#  本项目使用chromium浏览器，所以配置了浏览器位置，chrome浏览器不需要这一步
ps:    
chrome_options.binary_location = chromium_path  # 指定 Chromium 浏览器的位置



#  配置
1.  用户名和密码: 在 username 和 password 变量中设置您的用户名和密码。


      
2.  Chromium 和 ChromeDriver 路径: 设置 chromium_path 和 chromedriver_path 为您实际的路径。


                  
3.  日志文件: 日志记录到 netSts.log 文件中

# 使用说明
1.  确保已安装所需的库：requests, logging, selenium, plyer。



2.  配置 Chromium 和 ChromeDriver 的路径。    



3.  运行脚本并确保其具有访问网络和显示通知的权限。








