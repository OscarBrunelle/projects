@echo off

set /p network_name=Nom du reseau: 
netsh.exe wlan show profiles name=%network_name% key=clear

pause