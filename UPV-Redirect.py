#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# CREDENTIALS 
myusername = ""
mypassword = ""
redirectemail = "" 


chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
	"download.default_directory": r"~/",
	"download.prompt_for_download": False,
	"download.directory_upgrade": True,
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://casv3.univ-montp3.fr/casv3/login?service=https://courrier.etu.univ-montp3.fr") 
time.sleep(1)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys(myusername)
password.send_keys(mypassword)

browser.find_element_by_name("commit").send_keys(Keys.RETURN)


time.sleep(1)
browser.get("https://courrier.etu.univ-montp3.fr/horde/ingo/filters.php")
time.sleep(1)
browser.get("https://courrier.etu.univ-montp3.fr/horde/imp/mailbox.php?no_newmail_popup=1&mailbox=INBOX")
# time.sleep(1)
# browser.find_element_by_xpath("/html/body/div[4]/span[1]/a[2]")
time.sleep(1)
browser.get("https://courrier.etu.univ-montp3.fr/horde/imp/mailbox.php?mailbox=INBOX%2FInboxReel")
time.sleep(1)
browser.get("https://courrier.etu.univ-montp3.fr/horde/imp/mailbox.php?actionID=filter&page=1")
time.sleep(0.5)
browser.get("https://courrier.etu.univ-montp3.fr/horde/imp/mailbox.php?mailbox=INBOX%2FInboxReel")

time.sleep(2)

try:
	dropdown = Select(browser.find_element_by_name("filter"))
	dropdown.select_by_visible_text("Non vu")
	browser.find_element_by_link_text("Transfert").send_keys(Keys.RETURN)
	time.sleep(2)

	browser.switch_to_window(browser.window_handles[1])
	time.sleep(2)


	to = browser.find_element_by_id("to")
	to.send_keys(redirectemail)
	browser.find_element_by_name("btn_send_message").send_keys(Keys.RETURN)
	time.sleep(2)

	browser.switch_to_window(browser.window_handles[0])
	time.sleep(2)

	dropdown = Select(browser.find_element_by_name("filter"))
	time.sleep(1)
	dropdown.select_by_visible_text("Non vu")
	time.sleep(1)
	dropdown = Select(browser.find_element_by_name("flag"))
	time.sleep(1)
	dropdown.select_by_visible_text("Ouvert")
	time.sleep(2)
except Exception: 
	try:
		pass
	except Exception:
		browser.close()

try:
	browser.switch_to_window(browser.window_handles[0])
	time.sleep(2)
	dropdown = Select(browser.find_element_by_name("filter"))
	time.sleep(1)
	dropdown.select_by_visible_text("Ouvert")
	time.sleep(1)
	dropdown = Select(browser.find_element_by_name("targetMailbox"))
	time.sleep(1)
	dropdown.select_by_visible_text("Read")
	time.sleep(1)
	browser.find_element_by_link_text("Déplacer").send_keys(Keys.RETURN)
	time.sleep(2)
except Exception: 
	try:
		browser.switch_to_.alert().accept()
		pass
	except Exception:
		browser.close()

browser.close()
