#!/usr/bin/bash

# Run all tests

clear
cd "$1" || exit 2
echo "Running all tests in $PWD"
a=1
echo "----------------------------------------------------------------------"
for p in *.cpp; do
    echo "Running $p"
    g++ "$p" -o "$p.out"
    echo "-----------------------------------"
    for i in *.txt; do
        echo "Test $a: $i"
        if [ "$2" -eq "0" ]; then "./$p.out" < "$i"
        else time "./$p.out" < "$i"
        fi
        a=$((a+1))
        echo "-----------------------------------"
    done
    rm "$p.out"
    echo "----------------------------------------------------------------------"
    echo ""
done
