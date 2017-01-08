from project import *
import time
className = 'WindowsForms10.Window.8.app.0.3e799b_r15_ad1'
window = GetWindow(className)
window.SetTopmost()
window.Click()
time.sleep(.5)
menubar = window.MenuBarControl(AutomationID = 'menuStrip1', Name = 'menuStrip1')
menubar.Click()

'''

'''
start = menubar.MenuItemControl(foundIndex=3)
start.Click()
print 'end'