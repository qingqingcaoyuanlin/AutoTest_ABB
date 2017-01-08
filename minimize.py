# coding=utf-8
from project import *
className = 'WindowsForms10.Window.8.app.0.3e799b_r15_ad1'
window = GetWindow(className)
#window = uiautomation.WindowControl(searchDepth = 1, ClassName = 'WindowsForms10.Window.8.app.0.3e799b_r15_ad1')
menubar = window.MenuBarControl(AutomationID = 'MainForm')
print menubar
minimize = window.ButtonControl(AutomationID = '"Minimize"',Name = u'最小化')
print minimize
minimize.Click()
print 'end'
