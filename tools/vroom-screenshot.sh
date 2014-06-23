#!/bin/bash

VROOM_APPLICATION=$1
IMAGE_DESTINATION=$2

echo " -- capturing screenshot for $VROOM_APPLICATION => $IMAGE_DESTINATION"

echo " -- launching $1..."
vroom-wrapper $VROOM_APPLICATION 1>/dev/null &

sleep 3
bspc window -t floating

echo " -- waiting 10 seconds..."
sleep 10

echo " -- taking screenshot..."
scrot screenshot.png

sleep 1

echo " -- killing vroom application..."
killall vroom

echo " -- cropping image..."
#mogrify -crop 800x600 screenshot.png
mogrify -crop 800x600+1042+602 screenshot.png

echo " -- saving cropped image..."
mv screenshot.png $IMAGE_DESTINATION

#echo " -- removing temporary files..."
#rm screenshot-*.png
