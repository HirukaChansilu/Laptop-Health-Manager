Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "[Your Base Folder's Path]\main.bat" & Chr(34), 0
Set WshShell = Nothing