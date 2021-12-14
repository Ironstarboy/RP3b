Dim WshShell
Set WshShell=WScript.CreateObject("WScript.Shell") 
WshShell.Run "cmd.exe" 
WScript.Sleep 1500 
WshShell.SendKeys "ssh root@192.168.208.132" 
WshShell.SendKeys "{ENTER}" 
WScript.Sleep 1500 
WshShell.SendKeys "123456" 
WshShell.SendKeys "{ENTER}"