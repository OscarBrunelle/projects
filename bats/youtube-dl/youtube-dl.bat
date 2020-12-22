@echo off
set /p url=Enter the Youtube URL, or leave empty to exit: 
:loop
	if "%url%" == "" (exit)
	youtube-dl.exe -o "%%USERPROFILE%%\Music\%%(title)s.%%(ext)s" -x --audio-format mp3 --add-metadata %url%
	echo(
	set /p url=Enter the Youtube URL, or leave empty to exit: 
	goto loop