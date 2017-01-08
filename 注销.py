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
点击“设置”，弹出下拉选项“注销、开机启动”
此处选中下拉框，foundIndex = 2 即选中注销，=3则选中开机启动
其实 =1时选中了设置
'''
logout = menubar.MenuItemControl(foundIndex=2)
logout.Click()
print 'end'