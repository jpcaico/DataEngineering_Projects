import numpy as np
from numpy import add
import pandas as pd

df = pd.read_csv('data.csv', nrows=100)

# add a json column to the dataframe
#splitlines will split the json into multiple rows not a single
df['json'] = df.to_json(orient='records', lines=True).splitlines()

#just takt eht json column of the dataframe
dfjson = df['json']

#print out the dataframe to a file
#note that the timestamp forward slash will be escaped to stay
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')