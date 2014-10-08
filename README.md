maxsum
======

abstract algebra

These are scripts for Abstract Algebra to calculate the maximum of the least common multiples of all sets of integers that add up to all integers in the set [1,20].

Make sure that the shell script and python script are in the same directory, and you have edited permissions on both scripts to run them.
Call the shell script, and the output will be of the form:
[maxlcm] [set of numbers responsible for maxlcm] [sum of numbers in previous set]

To change the maximum value (initially 20) edit the python code, changing the value from 21 to any other desired integer.  Note that the script runtime increases exponentially (<20 is instantaneous, 50 takes 10-20 seconds, 100 takes (???).

All steps:
1. Download .zip file
cd ~/Downloads
unzip maxsum-master.zip
cd maxsum-master
sudo chmod +x max*
./maxsum
