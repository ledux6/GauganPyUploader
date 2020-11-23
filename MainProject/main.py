from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import sys
import helpers

start_frame = int(sys.argv[1])
style_filter = sys.argv[2]
speed = float(sys.argv[3])

print 'Starting program at frame: ' + str(start_frame)
if style_filter == 'f':
    print 'Using a custom style filter.'
else:
    print 'Using example filter ' + style_filter
print 'Running script ' + str(speed) + 'x slower than recommended.'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://34.216.122.111/gaugan/')
driver.execute_script("document.body.style.zoom='67%'")
driver.maximize_window()
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

helpers.click_check_box(driver)
current_dir = os.getcwd()
helpers.enable_download_headless(driver, current_dir + '\Gaugan')

if style_filter == 'f':
    upload_style_filter = driver.find_element_by_id('imgfile')
    style_file_name = os.listdir(current_dir + '\StyleFilter')
    upload_style_filter.send_keys(current_dir + '\StyleFilter\\' + style_file_name[0])
    load_button = driver.find_element_by_id('btnLoad')
    driver.execute_script("arguments[0].click();", load_button)
    time.sleep(1 * speed)
    custom_filter = driver.find_element_by_id('customBtn')
    driver.execute_script("arguments[0].click();", custom_filter)
else:
    style = driver.find_element_by_id('example' + style_filter)
    driver.execute_script("arguments[0].click();", style)


frames = os.listdir(current_dir + '\Frames')
frames.sort(key=lambda f: int(filter(str.isdigit, f)))
count = start_frame

for i in range(start_frame, len(frames)):
    upload_frame = driver.find_element_by_id('segmapfile')
    upload_frame.send_keys(current_dir + '\Frames' + '\\' + frames[i])
    time.sleep(1 * speed)
    e = driver.find_element_by_id('btnSegmapLoad')
    driver.execute_script("arguments[0].click();", e)
    time.sleep(1 * speed)
    e = driver.find_element_by_id('render')
    driver.execute_script("arguments[0].click();", e)
    time.sleep(3 * speed)
    e = driver.find_element_by_id('save_render')
    driver.execute_script("arguments[0].click();", e)
    time.sleep(3 * speed)
    os.rename(current_dir + '\Gaugan\gaugan_output.jpg', current_dir + '\Gaugan\gaugan_'+ str(count) +'.jpg')
    count += 1


