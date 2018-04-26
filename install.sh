#!/bin/bash
loc1=$(pwd)
echo "Do you want to install pubip[Y/N] (default=N)"
read op
if [ $op == 'y' ] || [ $op == 'Y' ] || [ $op == '\n' ]
then
  cp ebvgt /bin
  cd /bin
  chmod +x ebvgt
  cd
  mkdir ebvgt
  cd ebvgt
  loc2=$(pwd)
  cd $loc1
  cp generator.py $loc2
  cp code.txt $loc2
  cp code2.txt $loc2
  echo "Done"
  echo "To use it just type ebvgt"

else
  echo "As you like"
fi
