#!/bin/sh
sudo systemctl stop callbacksample
sudo systemctl disable callbacksample
sudo rm -f /etc/systemd/system/callbacksample.service
sudo systemctl daemon-reload
sudo unlink /opt/apl/python-callback-sample
rm -rf src/venv/
