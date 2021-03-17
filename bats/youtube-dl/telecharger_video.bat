@echo off
set /p url=Enter the Youtube URL, or leave empty to exit: 
:loop
	if "%url%" == "" (exit)
	set url=%url:music.youtube=youtube%
	youtube-dl.exe -o "%%USERPROFILE%%\Music\%%(title)s.%%(ext)s" -f best --add-metadata -i %url%
	set /p url=Enter the Youtube URL, or leave empty to exit: 
	goto loop