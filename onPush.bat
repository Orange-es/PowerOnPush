@echo off  
setlocal  
  
:: 获取当前时间  
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)  
for /f "tokens=1-3 delims=:." %%a in ('time /t') do (set mytime=%%a:%%b:%%c)  
  
:: 写入开始时间到日志文件  
echo [%mydate% %mytime%] --------------   startSoftware onPush.py...  -------------- >> G:\Pycharm\PythonProject\compareData\PowerOnPush\logfile.txt  
  
:: 运行Python脚本，并将输出重定向到日志文件  
python G:\Pycharm\PythonProject\compareData\PowerOnPush\onPush.py >> G:\Pycharm\PythonProject\compareData\PowerOnPush\logfile.txt 2>&1  
  
:: 获取结束时间  
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)  
for /f "tokens=1-3 delims=:." %%a in ('time /t') do (set mytime=%%a:%%b:%%c)  
  
:: 写入结束时间到日志文件  
echo [%mydate% %mytime%] --------------   endSoftware...  --------------  >> G:\Pycharm\PythonProject\compareData\PowerOnPush\logfile.txt  
  
endlocal