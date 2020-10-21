#!/bin/bash
# this script will pull down code from the origin from master
# move from Desktop to home
cd ..
# move from home to Documents (repo is here
cd Documents/
# git pull origin master
# fetch origin and reset hard
git fetch --all
git reset --hard origin/master
