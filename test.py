# coding=utf-8
from pywinauto.application import Application
from ctypes import *
import os
import sys
import win32api,win32con,win32gui,time
import pywinauto

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

def Is64Winows():
    return 'PROGRAMFILES(X86)' in os.environ
def AppPath():
    if Is64Winows():
        print 64
        return "C:\Program Files (x86)\ABB HB Management Center\ABB HB Management Center.exe"
    else:
        print 32
        return "C:\Program Files\ABB HB Management Center\ABB HB Management Center.exe"



#print appLnkPath
#os.system(appLnkPath)
print AppPath()
app = Application().start(AppPath())
time.sleep(1)

def window_handle_Title(Title):
    handle = win32gui.FindWindow(None, Title)
    return handle

def window_handle_class(className):
    handle = win32gui.FindWindow(className, None)
    return handle

def click_btn(hWnd, Button):
    hbutton = win32gui.FindWindowEx(hWnd, 0, 'Button', Button)
    if hbutton != 0:
        win32api.PostMessage(hbutton, win32con.WM_LBUTTONDOWN, 0, 0)
        win32api.PostMessage(hbutton, win32con.WM_LBUTTONUP, 0, 0)
        return True
    return None


DialogName = u"登录界面"
ButtonName = u"确认"



hWnd = window_handle_Title(DialogName)

hbtn = win32gui.FindWindowEx(hWnd,None,None,ButtonName)

print hWnd
print hbtn








