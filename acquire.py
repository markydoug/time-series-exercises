import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split

import requests

def get_swapi_results(url):
    response = requests.get(url)
    data = response.json()
    people_df = pd.DataFrame(data['results'])
    while data['next'] != None:
        response = requests.get(data['next'])
        data = response.json()
        people_df = pd.concat([people_df, pd.DataFrame(data['results'])], ignore_index=True)

    return people_df