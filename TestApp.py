import os
import sys
import subprocess
import uiautomation
import time
#import wmi
from win32com.client import GetObject

TestAppName = "ABB HB Management Center.exe"
def Is64Winows():
	return 'PROGRAMFILES(X86)' in os.environ
def AppPath():
	if Is64Winows():
		print 64
		return "C:\Program Files (x86)\ABB HB Management Center\ABB HB Management Center.exe"
	else:
		print 32
		return "C:\Program Files\ABB HB Management Center\ABB HB Management Center.exe"

def GetProcess(TestAppName):
	objWMIService = GetObject("winmgmts:")
	colProcesses = objWMIService.ExecQuery("Select * from Win32_Process")
	for objProcess in colProcesses:
		if objProcess.Name == TestAppName:
			return objProcess
def CheckAppRunning(imagename):
	'''
	������Ҫfrom win32com.client import GetObject��ֱ��ʹ��GetObject("winmgmts:")�Ϳ�����
	ʹ��import win32com��ʹ��win32com.client.GetObject('winmgmts:')�����⣬��֪Ϊ��
	'''
	objWMIService = GetObject("winmgmts:")
	colProcesses = objWMIService.ExecQuery("Select * from Win32_Process")
	for objProcess in colProcesses:
		if objProcess.Name == imagename:
			print "Process:" + objProcess.Name			
			print "Process ID: " + str(objProcess.ProcessID)
			print "Working Set Size: " + str(objProcess.WorkingSetSize)
			print "Page File Size: " + str(objProcess.PageFileUsage)
			print "Page Faults: " + str(objProcess.PageFaults)
			return True
	return False
'''
	#���кķ�ʱ�䳤
	p = os.popen('tasklist /FI "Imagename eq %s"' % imagename)  
	count = p.read().count(imagename)
	print count
	c = wmi.WMI()
	for process in c.Win32_Process():
		if process.Name == imagename :
			print str(process.ProcessId) + "  &  " + process.Name
			return True
	return False
'''

def GetWindow(className):
	return uiautomation.WindowControl(searchDepth = 1, ClassName = className)
