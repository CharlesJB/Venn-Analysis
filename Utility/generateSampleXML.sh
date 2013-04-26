#!/bin/bash

sample=$1
config_file=$2

echo '<?xml version="1.0" encoding="ISO-8859-1"?>'
echo '<venns>'

while read line
do
	for file in $(echo $line)
	do
		if [ "$file" == "$sample" ]
		then
			base_filename=$(echo $line | sed 's/ /_/g')
			echo -e "\t<combination>"
			echo -e "\t\t<name>$base_filename</name>"
			echo -e "\t\t<path>../results/$base_filename/$base_filename.html</path>"
			echo -e "\t</combination>"
		fi
	done
done < $config_file

echo '</venns>'
