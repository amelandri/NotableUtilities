@echo off

for /f "tokens=1-4 delims=/ " %%i in ("%date%") do (
	set day=%%i
	set month=%%j
	set year=%%k
)

for /f "tokens=1-4 delims=: " %%i in ("%time%") do (
	set hour=%%i
	set minute=%%j
)

cd C:\path\to\your\notebook\folder

git pull

reorderNotes.py

git add --all && git commit -m "Auto update %year%-%month%-%day% %hour%:%minute%" && git push origin master