#!/bin/zsh
git config --global user.email "a05558@126.com"
git config --global user.name "a05558"
git add .
echo "Input Update: "
read str
git commit -m $str
git push origin master
cp *.py ~/

