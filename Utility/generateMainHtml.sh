#!/bin/bash

dir_data=$1

echo "<html>"
echo "<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head>"
echo "<body>"
echo "<ul>"

for file in $(ls $dir_data)
do
	echo "<li><a href=\"www/$file.html\">$file</a></li>"
done

echo "</ul>"
echo "</body>"
echo "</html>"
