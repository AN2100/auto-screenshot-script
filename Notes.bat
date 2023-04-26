@echo off

set /p factor=Enter image processing factor: 

if "%factor%" == "--help" (
    echo To run the program enter a number between 0 and 1
    echo this number states the factor change
) else (
    if "%factor%" neq "" (
        echo Running the screen shot code ...

        py -3 screenshot.py %factor%

        echo making markdown ...

        py -3 markdown.py
    ) else (
        echo No input detected. Enter image processing factor.
    )
)
