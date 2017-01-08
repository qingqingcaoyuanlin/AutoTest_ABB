#-*- encoding: utf-8 -*-   
'''
import wmi   
import time   
c = wmi.WMI()

print ("下面显示的是本机的进程名和ID号")   
print "PID   &   Image Name "  
for process in c.Win32_Process():   
	print str(process.ProcessId) + "  &  " + process.Name

import os,sys
from win32com.client import GetObject
def proc_exist(process_name):
	is_exist = False
	wmi = win32com.client.GetObject('winmgmts:')
	processCodeCov = wmi.ExecQuery('select * from Win32_Process where name=\"%s\"' %(process_name))
	if len(processCodeCov) > 0:
		is_exist = True
	return is_exist
a = proc_exist("ABB HB Management Center.exe")
print a
'''

'''
import os,sys
from win32com.client import GetObject
objWMIService = GetObject("winmgmts:")
colProcesses = objWMIService.ExecQuery("Select * from Win32_Process")
for objProcess in colProcesses:
	if objProcess.Name == "ABB HB Management Center.exe":
		print "Process:" + objProcess.Name
		#sngProcessTime = (CSng(objProcess.KernelModeTime) + CSng(objProcess.UserModeTime)) / 10000000
		#print "Processor Time: " & sngProcessTime
		print "Process ID: " + str(objProcess.ProcessID)
		print "Working Set Size: " + str(objProcess.WorkingSetSize)
		print "Page File Size: " + str(objProcess.PageFileUsage)
		print "Page Faults: " + str(objProcess.PageFaults)
'''

