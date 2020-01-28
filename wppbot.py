# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime

from wpp_message import message
import time
import csv

class WppApi:
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = 'driver/geckodriver'
    browser = webdriver.Firefox(executable_path = 'driver/geckodriver')
    timeout = 10

    def __init__(self, wait):
        self.browser.get("https://web.whatsapp.com/")
        WebDriverWait(self.browser, wait).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))         
        

    # seleciona um chat
    def get_chat(self, chat_name):
        time.sleep(3)
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(chat_name+Keys.ENTER)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.message-in')))
        

    def join_group(self, invite_link):
        self.browser.get(invite_link)
        try:
            Alert(self.browser).accept()
        except:
            print("No alert Found")
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#action-button')))
        join_chat = self.browser.find_element_by_css_selector("#action-button")
        join_chat.click()
       

    def send_message(self, name, msg):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        # we will send the name to the input key box
        search.send_keys(name+Keys.ENTER)
        try:
            send_msg = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
            msgs = msg.split("\n")
            for msg in msgs:
                send_msg.send_keys(msg)
                send_msg.send_keys(Keys.SHIFT+Keys.ENTER)
            send_msg.send_keys(Keys.ENTER)
            return True
        except TimeoutException:
            raise TimeoutError(
                "Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return False
        except Exception:
            return False

    def refresh(self):
        try:
            self.browser.refresh()
            Alert(self.browser).accept()
        except Exception as e:
            print(e)
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))

    def check_exists_by_class(self, driver, class_name):
        try:
            driver.find_element_by_css_selector('.'+class_name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_xpath(self, driver, xpath):
        try:
            driver.find_element_by_xpath('//'+xpath)
        except NoSuchElementException:
            return False
        return True
    
    def check_exists_by_tag(self, driver, tag):
        try:
            driver.find_element_by_tag_name(tag)
        except NoSuchElementException:
            return False
        return True

    def get_and_save_image(self, src, chat_name):
        main_window = self.browser.current_window_handle
        self.browser.execute_script('''window.open("%s", "_blank");'''%(src))
        self.browser.switch_to_window(self.browser.window_handles[1])

        actionChains = ActionChains(self.browser)
        element =  self.browser.find_element_by_tag_name('img')
        actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # self.browser.get(src)
        print('DONE')
        # request.urlretrieve(src, "media/images/img.png")

    # retorna lista com ultimas menssagens
    def get_messages_chat(self, chat_name, wait):
        self.get_chat(chat_name)
        messages = []
        divs = self.browser.find_elements_by_class_name('message-in')

        # print(len(divs))
        for div in divs:

            if self.check_exists_by_tag(div, 'img'):
                # print('achou img')
                img = div.find_element_by_tag_name('img')
                src = img.get_attribute('src')                
                # print(src)
                # self.get_and_save_image(src, chat_name)

            if self.check_exists_by_class(div, 'copyable-text'):
                info = div.find_element_by_class_name('copyable-text')
                infoMsg = info.get_attribute('data-pre-plain-text')
                infoMsg = infoMsg.replace('[', '')
                infoMsg = infoMsg.replace(',', '')
                infoMsg = infoMsg.replace(']', '')
                vtMsg = infoMsg.split()
                msg = message(info.location, vtMsg[1], vtMsg[0], vtMsg[2], info.text)
                messages.append(msg)
                # print(msg.text)
        return messages

    def have_new_mesages(self, chat_name):
        # search = self.browser.find_element_by_css_selector("._2zCfw")
        # search.send_keys(chat_name)
        # self.browser.execute_script("document.getElementsByClassName('_2zCfw').value = '"+chat_name+"';")
        # chat = self.browser.find_element_by_css_selector('.X7YrQ')
        chats = self.chat_with_unseen_messages()
        have = False
        if chat_name in chats:
            have = True
        
        # self.browser.execute_script("document.getElementsByClassName('_2zCfw').value = '';")
        # self.browser.find_element_by_css_selector('._2heX1').click()
        return have


    def chat_with_unseen_messages(self):
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))
        time.sleep(5)

        chat_names= []
        div_side = self.browser.find_element_by_id('pane-side')
        size = self.browser.execute_script('return arguments[0].scrollHeight', div_side)
        ini = 0
        while ini + size/10 < size - size/10:
            chats = self.browser.find_elements_by_css_selector('.X7YrQ')
            for chat in chats:
                if self.check_exists_by_class(chat, 'P6z4j'):
                    neme = chat.find_element_by_css_selector('._3H4MS')
                    unseen = chat.find_element_by_css_selector('.P6z4j')
                    chat_tuple = (neme.text, unseen.text)
                    if chat_tuple not in chat_names:
                        chat_names.append(chat_tuple)
            self.browser.execute_script('arguments[0].scrollTop += arguments[0].scrollHeight/10', div_side)
            ini = self.browser.execute_script('return arguments[0].scrollTop', div_side)
            time.sleep(1)
        self.browser.execute_script('arguments[0].scrollTop = 0', div_side)
        return chat_names

    def get_chat_names(self):
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))
        time.sleep(5)
        self.browser.minimize_window()
        chat_names= []
        div_side = self.browser.find_element_by_id('pane-side')
        size = self.browser.execute_script('return arguments[0].scrollHeight', div_side)
        ini = 0
        while ini + size/10 < size - size/10:
            chats = self.browser.find_elements_by_css_selector('.X7YrQ')
            for chat in chats:
                neme = chat.find_element_by_css_selector('._3H4MS')
                chat_name = neme.text
                if chat_name not in chat_names:
                    chat_names.append(chat_name)
            self.browser.execute_script('arguments[0].scrollTop += arguments[0].scrollHeight/10', div_side)
            ini = self.browser.execute_script('return arguments[0].scrollTop', div_side)
        
        return chat_names

    def watch_groups(self, groups, datetime):
        last_messages = {}
        groups_messages = {}
        for group in groups:
                messages = self.get_messages_chat(group, 20)
                groups_messages[group] = messages
                last_messages[group]= messages[-1]
                
        i=0
        while i < 1:
            for group in groups:
                messages = self.get_messages_chat(group, 20)
                for message in messages:
                    if message.compare_time(last_messages[group].date_time) == 1:
                        last_messages[group] = message
                        groups_messages[group].append(message)
                    elif message.compare_time(last_messages[group].date_time) == 0:
                        if message.location['y'] > last_messages[group].location['y']:
                            last_messages[group] = message
                            groups_messages[group].append(message)
            i+=1
        for group in groups:
            self.write_file(group, groups_messages[group])


    def write_file(self, title, messages):
        titlefile = "archives/"+title+".csv"
        with open(titlefile, 'a') as file:
            writer = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for message in messages:
                writer.writerow([message.location, message.date_time, message.author.encode('utf-8'), message.text.encode('utf-8')])

    
    def read_from_file(self, title):
        try:
            titlefile = "archives/"+title+".csv"
            archive = open(titlefile, 'r')
            messages = archive.readlines()
            last_line = messages[len(messages)-1].split(",")            
            print(last_line[0])
            print(last_line[1])
            y = last_line[0].split(":")
            last_line[1]= last_line[1].replace("|", "")
            last_line[1] = last_line[1].replace("{", "")
            last_line[1] = last_line[1].replace("}", "")
            x = last_line[1].split(":")            
            location = {'y' : float(y[1]), 'x' : float(x[1])}
            last_message = message.set_message(location, last_line[2], last_line[3], last_line[4])
            return [last_mesage]
        except IOError as e:
            return []

