# python-callback-sample
Python + Flask + Waitress + Background task

## Install and execute
1. Create a symbolic link from src/ to /opt/apl/python-callback-sample/ (ex. ln -s /opt/apl/python-callback-sample/ src/)
2. Execute install_service.sh with admin privileges (ex. sudo systemd/install_service.sh)
3. Start callbacksample service (ex. systemctl start callbacksample)
4. Check if requests are ok. (curl localhost:5000)

