@echo off
for %%f in (*.dat) do (
    if "%%~xf"==".dat" (
::   echo %%f
	python randomizer.py %%f

	)
)
pause
