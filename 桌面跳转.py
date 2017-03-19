# coding=utf-8
from pywinauto.application import Application
from ctypes import *
import os
import sys
import win32api,win32con,win32gui,time
import pywinauto
#from abb import *
from TestApp import *


'''
app = Application().connect(process = GetProcess(TestAppName).ProcessID)
window = app.window(class_name = 'WindowsForms10.Window.8.app.0.3e799b_r11_ad1') 
print(window.name)
item = window.ListView(automation_id = "Desktop")
print(item.name)
#window(name = u'系统设置',control_type = "ListItem").click()
'''
'''
app = Application().connect(process = GetProcess(TestAppName).ProcessID)
autowin = app.window(class_name = className) 
#autotab = app.autowin.Tab(automation_id ="MyTabControl1")
autotab = autowin["MyTabControl1"]
#autowin["MyTabControl1"].select(1).click()
tabitem =  autotab.select(1)
print tabitem.click()
print text
print(autotab.AutomationId)
'''
window = uiautomation.WindowControl(searchDepth = 1, ClassName = className)
desktopico = window.TextControl(Name = u"桌面")
desktopico.Click()
panel = window.PaneControl(AutomationId = "panel2")
desktop = [
    {u"系统设置":u"小区信息设置"},{u"联网设备配置":u"读取联网设备"},{u"单元设备配置":u"楼栋单元配置"},{u"管理工具":u"Ping检测与查看版本"},
    {u"紧急开锁":u"紧急开锁"},{u"工作人员管理":u"部门管理"},{u"业主信息管理":u"业主信息录入"},{u"门禁卡注册":u"单张卡注册"},
    {u"门禁卡管理":u"门禁卡列表"},{u"信息发布":u"信息发送 "},{u"设备故障报警":u"开关故障检测"},{u"记录管理":u"报警记录"},
    {u"数据库管理":u"数据库备份"}
         ]

item_list =[]
for tup in desktop:
    for (key,value) in tup.items():
        item = window.ListItemControl(Name = key)
        item_list.append(item)
        #print(item.BoundingRectangle)


'''
for item in item_list:
    print(item.BoundingRectangle)
'''  
passFlag = 0
for tup in desktop:    
    item_list[desktop.index(tup)].Click()
    time.sleep(.5)
    index = desktop.index(tup)
    
    for (key, value) in tup.items():
        #tab = panel.TabItemControl(Name = value)
        tab = panel.TabControl(AutomationId = "MyTabControl1")
        tabitem = tab.TabItemControl(Name = value)
        str = tabitem.Name
        if tabitem.CurrentIsSelected():
            passFlag += 1
            str += ":Pass"
            print(str)            
        else:
            str += ":Fail"
            print(str)
        
        
        desktopico.Click()
        time.sleep(.5)
print passFlag
print len(desktop)
if passFlag == len(desktop):
    print("All Pass!!!")
else:
    print("Some Fail!!!")
        
print 'end'