#!/bin/sh
cp callbacksample.service /etc/systemd/system
systemctl daemon-reload
systemctl enable callbacksample
echo "finished"
