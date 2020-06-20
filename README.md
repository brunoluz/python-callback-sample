# python-callback-sample
Python + Flask + Waitress + Background task

## Install and execute
1. Create a virtualenv inside src/ directory. (python3 -m venv src/venv)
2. Load virtualenv (source src/venv/bin/activate)
3. Install dependencies (pip install -r src/requirements.txt)
4. Deactivate virtualenv (deactivate)
5. Create a symbolic link from src/ to /opt/apl/python-callback-sample/ (sudo ln -s $(pwd)/src/ /opt/apl/python-callback-sample)
6. Execute install_service.sh with admin privileges (ex. sudo ./systemd/install_service.sh)
7. Start callbacksample service (ex. systemctl start callbacksample)
8. Check if requests are ok. (curl localhost:5000)

