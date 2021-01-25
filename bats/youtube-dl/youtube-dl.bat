@echo off
set /p url=Enter the Youtube URL, or leave empty to exit: 
:loop
	if "%url%" == "" (exit)
	set url=%url:music.youtube=youtube%
	youtube-dl.exe -o "%%USERPROFILE%%\Music\%%(title)s.%%(ext)s" -x --audio-format mp3 --add-metadata -i %url%
	set /p url=Enter the Youtube URL, or leave empty to exit: 
	goto loop