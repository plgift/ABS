#! /bin/bash

while read line; do
    model=${line::-3}
    python abs.py "bline1${model}" $line
done < modelnames.txt 
