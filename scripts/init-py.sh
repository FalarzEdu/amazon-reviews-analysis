#!/bin/bash

sudo apt update && sudo apt install -y pandoc

pip install pymongo pandas matplotlib jupyter python-dotenv seaborn

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

tail -f /dev/null