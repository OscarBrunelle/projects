@echo off

echo Entrer l'extension a lister
echo Laisser vide pour lister les dossiers, * pour tout
set /p extension=Extension (ex: pdf): 

echo.
dir *.%extension% /b |clip
dir *.%extension% /b
echo. && echo Liste copiee dans le presse-papiers.
echo Si necessaire, utiliser le clic droit (et non ctrl-c) pour copier dans la console.

pause