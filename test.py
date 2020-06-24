import pandas as pd
import json
import requests

df = pd.read_json('{data:{"1F64F":1}\}')

print(df.head())
