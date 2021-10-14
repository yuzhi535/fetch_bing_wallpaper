#!/usr/bin/bash

set -e

cd /home/yuxi/PycharmProjects/fetch_wallpapers
source venv/bin/activate
pip install -r requirements.txt
python main.py