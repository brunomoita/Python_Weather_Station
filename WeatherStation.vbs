Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Users\bruno\OneDrive\Documents\PythonWeatherStation\WeatherStation.bat" & Chr(34), 0
Set WshShell = Nothing