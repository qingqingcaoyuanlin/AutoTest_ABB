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
��������á�����������ѡ�ע��������������
�˴�ѡ��������foundIndex = 2 ��ѡ��ע����=3��ѡ�п�������
��ʵ =1ʱѡ��������
'''
logout = menubar.MenuItemControl(foundIndex=2)
logout.Click()
print 'end'