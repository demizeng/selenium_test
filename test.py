from selenium import webdriver
import time
import requests
import os

# 测试的小例子，利用selenium和requests爬取网站上的图片

dir = os.path.dirname(os.path.abspath(__file__))
driver_dir = os.path.join(os.path.dirname(dir),"driver")
chrome_driver = os.path.join(driver_dir,"chromedriver.exe")



driver = webdriver.Chrome(chrome_driver)
# driver = webdriver.Ie()  # 使用IE之前需要取消IE浏览器的保护模式，在internet选项-安全下面，将internet和受限制的站点下面的保护模式取消
driver.implicitly_wait(10) # 静默等待1秒
driver.maximize_window()

driver.get('http://detail.zol.com.cn/cell_phone/index1318500.shtml')

# 百度搜索框：<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
# https://cn.bing.com/ bing的搜索框：<input class="b_searchbox" id="sb_form_q" name="q" title="输入搜索词" type="search" value="" maxlength="100" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" aria-controls="sw_as" aria-autocomplete="both" aria-owns="sw_as" data-bm="20">
search_field = driver.find_elements_by_css_selector('img')
imgpaths = [imgpath.get_attribute('src') for imgpath in search_field]
imgpaths = [img for img in imgpaths if img is not None]

filedir = os.path.join(os.getcwd(), 'images')
if not os.path.isdir(filedir):
    os.makedirs(filedir)

for pa in imgpaths:
    if pa.endswith('.jpg') or pa.endswith('.JPG'):
        imgdata = requests.get(pa)
        imgname = pa.strip().split('/')[-1]
        imgpath = os.path.join(filedir, imgname)
        with open(imgpath, 'wb+') as f:
            f.write(imgdata.content)
        
time.sleep(1)
driver.quit()
