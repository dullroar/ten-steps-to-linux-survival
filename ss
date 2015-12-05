#!/bin/bash
scrot -s ./images/${1}.png && mogrify -resize 750 ./images/${1}.png
