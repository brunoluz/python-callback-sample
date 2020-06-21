#!/bin/sh
python3 -m venv src/venv
source src/venv/bin/activate
pip install -r src/requirements.txt
deactivate
sudo ln -s $(pwd)/src/ /opt/apl/python-callback-sample
sudo cp systemd/callbacksample.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable callbacksample
sudo systemctl start callbacksample
echo "installed"
