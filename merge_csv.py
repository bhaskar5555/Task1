import pandas as pd		
import glob		
import os		
path = os.getcwd()		
files = os.path.join(path, "*.csv")	
csv_files = glob.glob(files)
print(csv_files)
df = pd.concat(map(pd.read_csv,csv_files), ignore_index=True)
print(df)
print("++++++++++++++++++++++++")
df.drop_duplicates(subset=['Source IP','Count','Events per Second'],keep='false')
print(df)
df.to_csv("combined1.csv",header=True,index=False)
print("end")
