# -*- Utf-8 -*-
import selenium
import pyperclip
import time
import requests
import random
import os
from bestdllever import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Firefox()
files = []

with open('tree.txt','r') as file:
    for line in file:
        if '.filter' in line:
            files.append(line[:len(line)-1])

print(files)
os.remove('tree.txt')
testflag = 1

class devcardssettings: #Настройки должны идти от меньшего уровня к большему.
    number = [1,2,3]
    value = [10,100,1000]
    alertValue = 50
    settings = ['    SetFontSize 40\n    SetBorderColor 37 205 241\n\n',
                '    SetFontSize 50\n    SetBorderColor 37 205 241\n    SetBackgroundColor 36 26 166\n    MinimapIcon 2 Blue Square\n\n',
                '    SetFontSize 60\n    SetBorderColor 151 232 249\n    SetBackgroundColor 15 192 230\n    SetTextColor 0 0 0\n    MinimapIcon 2 Blue Square\n    PlayEffect Blue\n    PlayAlertSound 6 '+str(alertValue)+'\n\n']
    basesettings = 'Show\n    Class "Card"\n    SetFontSize 30\n\n'
    namesettings = 'BaseType'
    markname = 'divcard'
    httppageflag = 'divcard'
    

class devitemssettings: #Настройки должны идти от меньшего уровня к большему.
    number = [1,2,3]
    value = [10,100,1000]
    alertValue = 50
    settings = ['    SetFontSize 30\n    SetBorderColor 255 0 255\n\n',
                '    SetFontSize 50\n    SetBorderColor 255 0 255\n    SetBackgroundColor 119 0 119\n    SetTextColor 0 150 255\n    MinimapIcon 2 Brown Circle\n\n',
                '    SetFontSize 60\n    SetBorderColor 255 0 255\n    SetBackgroundColor 255 128 255\n    SetTextColor 255 0 0\n    MinimapIcon 2 Brown Circle\n    PlayEffect Red\n    PlayAlertSound 6 '+str(alertValue)+'\n\n']
    basesettings = 'Show\n    Prophecy ""\n    SetFontSize 30\n\n'
    namesettings = 'Prophecy'
    markname = 'divian'
    httppageflag = 'prop'
    
class fossilssettings: #Настройки должны идти от меньшего уровня к большему.
    number = [1,2,3]
    value = [10,20,50]
    alertValue = 50
    settings = ['    SetFontSize 30\n    SetBorderColor 228 136 33\n    SetTextColor 228 136 33\n\n',
                '    SetFontSize 40\n    SetBorderColor 228 136 33\n    SetBackgroundColor 240 213 99 100\n    SetTextColor 228 136 33\n    MinimapIcon 2 Brown Circle\n\n',
                '    SetFontSize 60\n    SetBorderColor 228 136 33\n    SetBackgroundColor 255 255 74\n    SetTextColor 228 136 33\n    MinimapIcon 2 Brown Circle\n    PlayEffect Brown\n    PlayAlertSound 10 '+str(alertValue)+'\n\n']
    basesettings = 'Show\n    BaseType "Fossil"\n    Class "Stackable Currency"\n    SetFontSize 30\n    SetTextColor 228 136 33\n\n'
    namesettings = 'BaseType'
    markname = 'fos'
    httppageflag = 'foss'

def getip(ip):
    global browser
    try:
        browser.get(ip)
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]').click()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/img[1]').click()
    except NoSuchElementException:
        getip(ip)
       
def getfilter(ip,levels,testflag):
    if testflag:
        getip(ip)
    else:
        browser.get(ip)
    flag1 = 1
    numberofcards = 1
    data = [[],[],[]] #data[0]:имя карточки data[1]:прайс карточки data[2]:уровень карточки

    while flag1:
        try:
            browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]').click()
        except NoSuchElementException:
            flag1 = 0

    flag1 = 1
    while flag1:
        try:
            name = browser.find_element_by_xpath('/html/body/div[4]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[1]/div/div[1]').get_attribute('title')
            data[0].append(name)
            if levels.httppageflag == 'divcard':
                try:
                    price = float(browser.find_element_by_xpath('/html/body/div[4]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[4]/div/span[2]').get_attribute('title'))
                except:
                    price = float(browser.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[4]/div/span').get_attribute('title'))
            elif levels.httppageflag == 'prop':
                try:
                    price = float(browser.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[3]/div/span[2]').get_attribute('title'))
                except:
                    price = float(browser.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[3]/div/span').get_attribute('title'))
            elif levels.httppageflag == 'foss':
                try:
                    price = float(browser.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[3]/div/span[2]').get_attribute('title'))
                except:
                    price = float(browser.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[3]/div/span').get_attribute('title'))
            else:
                try:
                    price = float(browser.find_element_by_xpath('/html/body/div[4]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[4]/div/span[2]').get_attribute('title'))
                except:
                    price = float(browser.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr['+str(numberofcards)+']/td[4]/div/span').get_attribute('title'))
            data[1].append(price)
            templevel = 0
            for num in range(len(levels.number)):
                if price >= levels.value[num]:
                    templevel = levels.number[num] 
            data[2].append(templevel)
            print(str(data[0][numberofcards-1])+' '*(30-len(str(data[0][numberofcards-1]))),str(data[1][numberofcards-1])+' '*(30-len(str(data[1][numberofcards-1]))),str(data[2][numberofcards-1])+' '*(30-len(str(data[2][numberofcards-1]))))
            numberofcards += 1
        except NoSuchElementException:
            flag1 = 0

    if price <= 300:
        levels.alertValue = price
    else:
        levels.alertValue = 300
        
    txtall = ''
    for levelnum in levels.number:
        stringofnames = ''
        for num in range(len(data[0])):
            if data[2][num] == levelnum:
                stringofnames += '"'+data[0][num]+'" '
        txtall += 'Show\n    '+levels.namesettings+' '+stringofnames+'\n'+levels.settings[levels.number.index(levelnum)]
        for file in files:
            filereplace(file,'#{'+levels.markname+str(levelnum)+'}',levels.namesettings,'    '+levels.namesettings+' '+stringofnames)
    txtall += levels.basesettings
    print(txtall)
    
getfilter('https://poe.ninja/challenge/divinationcards',devcardssettings,1)
getfilter('https://poe.ninja/challenge/prophecies',devitemssettings,0)
getfilter('https://poe.ninja/challenge/fossils',fossilssettings,0)
input('Press any key to exit...')
