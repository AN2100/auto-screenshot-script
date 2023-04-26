#!/bin/bash

if [[ $1 == "--help" ]]; then
    echo "To run the program enter a number between 0 and 1 "
    echo "this number states the factor change"
else

    if [ $# -gt 0 ]; then

        echo "Running the screen shot code ..."

        python3 screenshot.py $1

        echo "making markdown ..."

        python3 markdown.py
    else
        echo "Enter image processing factor"
    fi
fi
