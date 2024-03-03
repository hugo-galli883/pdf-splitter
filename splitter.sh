#!/bin/bash

files=$(ls input)
for i in ${files}
do
	echo "Processing for file $i"
	echo "    Splitting pdf into separate pages"
	pdftoppm input/"$i" pages/p -png
	echo "    Done !"
	echo "    Splitting each page into 2 separate pages"
	pages=$(ls pages)
	count=$(ls -1 pages/ | wc -l)
	for j in ${pages}
	do
		echo "Page $j"
		convert pages/"$j" -crop 50%x100% pages/%01d_"$j"
    rm pages/"$j"
	done
	echo "    Done !"
  echo "    Changing name of pages"
  python3 sort.py
  echo "    Done !"
  echo "    Converting pages into a single pdf"
  convert pages/* output/"$i"
  rm pages/*
  echo "    Done !"
  echo "File $i is available in the output/ folder"
done
