from pywinauto.application import Application
from ctypes import *
import os
import sys
import win32api,win32con,win32gui,time
import pywinauto
from abb import *


app = Application().connect(process = GetProcess(TestAppName).ProcessID)
app 
print 'end'