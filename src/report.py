import pandas as pd
from numpy import double

weather_20160201_source = "data/csv/weather.20160201.csv"
weather_20160301_source = "data/csv/weather.20160301.csv"
parquet_dest_path = "data/parquet/combination.parquet.gzip"


def read_csv(source_path: str) -> pd.DataFrame:
    """Reading CSV Files"""
    data_frame = pd.read_csv(source_path)
    return data_frame


def to_parquet(data_frame: pd.DataFrame, dest_path: str) -> pd.DataFrame:
    """Converting To Parquet File"""
    parquet_data = data_frame.to_parquet(dest_path, compression='gzip')
    return parquet_data


if __name__ == "__main__":
    """Reading CSV Files"""
    dataframe_1 = read_csv(source_path=weather_20160201_source)
    dataframe_2 = read_csv(source_path=weather_20160301_source)
    """Appending dataFrames"""
    bigdata = dataframe_1.append(dataframe_2, ignore_index=True)
    combined_parquet = to_parquet(bigdata, parquet_dest_path)
    combined_dataframe = pd.read_parquet(parquet_dest_path, engine='pyarrow')
    max_temp_dataframe = combined_dataframe[
        combined_dataframe.ScreenTemperature == combined_dataframe.ScreenTemperature.max()]
    print(f'hottest day:{"".join(max_temp_dataframe["ObservationDate"].values)}')
    print(f'temperature on hottest day:{double(max_temp_dataframe["ScreenTemperature"].values)}')
    print(f'region:{"".join(max_temp_dataframe["Region"].values)}')
