# coding=utf-8
from pywinauto.application import Application
from ctypes import *
import os
import sys
import win32api,win32con,win32gui,time
import pywinauto
from abb import *
from TestApp import *
'''
app = Application().connect(process = GetProcess(TestAppName).ProcessID)
window = app.window(class_name = 'WindowsForms10.Window.8.app.0.3e799b_r11_ad1') 
print(window.name)
item = window.ListView(automation_id = "Desktop")
print(item.name)
#window(name = u'系统设置',control_type = "ListItem").click()
'''


window = uiautomation.WindowControl(searchDepth = 1, ClassName = className)
desktopico = window.TextControl(Name = u"桌面")
desktopico.Click()
panel = window.PaneControl(AutomationId = "panel2")
desktop = [
    {u"系统设置":"SystemSet"},{u"联网设备配置":"NetworkConfig"},{u"单元设备配置":"ProjectConfig"},{u"管理工具":"ManageTool"},
    {u"紧急开锁":"NetworkConfig"},{u"工作人员管理":"NetworkConfig"},{u"业主信息管理":"NetworkConfig"},{u"门禁卡注册":"NetworkConfig"},
    {u"门禁卡管理":"NetworkConfig"},{u"信息发布":"NetworkConfig"},{u"设备故障报警":"NetworkConfig"},{u"记录管理":"NetworkConfig"},
    {u"数据库管理":"NetworkConfig"}
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

for tup in desktop:    
    item_list[desktop.index(tup)].Click()
    time.sleep(.5)
    index = desktop.index(tup)
    for (key, value) in tup.items():
        '''
        win = panel.WindowControl(Name = value)
        str = key
        if win.AutomationId == item_list[index].Name:
            str += ":Pass"
            print(str)
        else:
            str += ":Fail"
            print(str)
        '''
        desktopico.Click()
        time.sleep(.5)
print 'end'