import uiautomation
TestAppName = "ABB HB Management Center.exe"

def GetWindow(className):
	return uiautomation.WindowControl(searchDepth = 1, ClassName = className)
