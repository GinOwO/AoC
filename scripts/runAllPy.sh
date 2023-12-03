#!/usr/bin/bash

# Run all tests

clear
cd "$1" || exit 2
echo "Running all tests in $PWD"
a=1
echo "----------------------------------------------------------------------"
for p in *.py; do
    echo "Running $p"
    echo "-----------------------------------"
    for i in *.txt; do
        echo "Test $a: $i"
        if [ $2 -eq "0" ]; then python3 "$p" < "$i"
        else time python3 "$p" < "$i"
        fi
        a=$((a+1))
        echo "-----------------------------------"
    done
    echo "----------------------------------------------------------------------"
    echo ""
done
