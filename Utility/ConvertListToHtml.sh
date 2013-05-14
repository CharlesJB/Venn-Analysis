#!/bin/bash

filename=$1
echo "<!DOCTYPE html>"
echo "<html>"
echo "<head>"
echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">"
echo "</head>"
echo "<body>"
for line in $(cat $filename)
do
	echo "<a href=\"http://www.genecards.org/cgi-bin/carddisp.pl?gene=$line\" target=\"_blank\">$line</a></br>"
done
echo "</body>"
echo "</html>"
