#!/bin/sh
cp systemd/callbacksample.service /etc/systemd/system
systemctl daemon-reload
systemctl enable callbacksample
echo "finished"
