python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pytest --cov=src tests/
python3 src/report.py