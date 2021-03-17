@echo off

echo Enter the extension you want to list
echo Leave empty for folders, * for everything
set /p extension=Extension (ex: pdf): 

echo.
dir *.%extension% /b |clip
dir *.%extension% /b
echo. && echo List copied to clipboard.
echo If needed, use right click (and not ctrl-c) to copy text in the console.

pause