#!/bin/bash
pip install pymongo pandas matplotlib jupyter python-dotenv seaborn

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

tail -f /dev/null