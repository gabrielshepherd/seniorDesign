#!/bin/bash
# this script will commit and push code with user inputted
# commit message to the specified branch
# move from Desktop to proper directory in Documents
cd ..
cd Documents/Gabe/
# commit and define message
echo Enter commit message:
read msg
git reset --mixed origin/Gabe
git commit -m $msg
git push origin Gabe
