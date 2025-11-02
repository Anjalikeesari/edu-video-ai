#!/usr/bin/env bash
# start backend then frontend (assumes venv & npm installed)
cd backend
if [ ! -d "venv" ]; then
  python3 -m venv venv
  source venv/bin/activate
  pip install -r ../requirements.txt
else
  source venv/bin/activate
fi
FLASK_APP=app.py flask run --port=5000 &
cd ../frontend
npm install
npm start
