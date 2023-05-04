#!/bin/bash

LUN=1
MER=3
DOW=$(date +%u)
echo $DOW

if [ $LUN -eq $DOW ] || [ $MER -eq $DOW ] 
then 
	VBoxManage startvm "Ubuntu - Magic" --type headless
fi
