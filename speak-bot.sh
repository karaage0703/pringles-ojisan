#!/bin/bash

cd `dirname $0`
cd TextGenerator
python GenerateText.py 1 > ../speak.txt
cd ..
python jtalk.py speak.txt
