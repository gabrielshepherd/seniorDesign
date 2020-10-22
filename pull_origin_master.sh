#!/bin/bash
# this script will pull down code from the origin from master
# move from Desktop to home
cd ..
# move from home to Documents (repo is here
cd Documents/master/
# fetch origin and reset hard
git pull origin master
git reset --hard origin/master