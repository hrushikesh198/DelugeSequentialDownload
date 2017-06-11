#!/bin/bash
echo "(*) Building and linking Plugin"
cd ~/workspace/DelugeSequentialDownload/
mkdir temp
export PYTHONPATH=./temp
/usr/bin/python setup.py build develop --install-dir ./temp
cp ./temp/SequentialDownload.egg-link ~/.config/deluge/plugins
rm -fr ./temp
echo "(*) Starting Deluge"
~/Public/Deluge.app/Contents/MacOS/Deluge -L info
