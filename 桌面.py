from project import *
import time
className = "WindowsForms10.STATIC.app.0.3e799b_r15_ad1"
#window = GetWindow(className)
window = uiautomation.WindowControl(searchDepth = 3, ClassName = className)
desktop = window.TextControl(AutomationID = 'desktoplabel', Name = u'×ÀÃæ')
#desktop = window.
desktop.Click()
print 'end'