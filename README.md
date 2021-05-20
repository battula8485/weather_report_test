# weather_report_test

##what is this project about:
Convert the weather data into parquet format. Set the row group to the appropriate value you see fit for this data
##How To Run This Project:
steps:
  
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 src/report.py
pytest --cov=src tests/
```
   
   
or you can use below automated shell script to execute project and tests
```
sh project_run.sh
```

