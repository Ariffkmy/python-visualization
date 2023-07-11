import pandas as pd
import pyarrow as pa
from pyarrow.parquet import ParquetFile
import matplotlib.pyplot as plt



URL_DATA = 'https://storage.googleapis.com/dosm-public-economy/cpi_state.parquet'
df = pd.read_parquet(URL_DATA)

#first_ten_rows = next(URL_DATA.iter_batches(batch_size = 10)) 
#df = pa.Table.from_batches([first_ten_rows]).to_pandas() 
#if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

df_first3 = df.head(1)
print(df_first3)
col = len(df_first3.columns)-1
#print(df)

#print(df_first3['sarawak'].to_string(index=False))

left = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

johor = float(df_first3['johor'].to_string(index=False))
kedah = float(df_first3['kedah'].to_string(index=False))
kelantan = float(df_first3['kelantan'].to_string(index=False))
melaka = float(df_first3['melaka'].to_string(index=False))
n_sembilan = float(df_first3['negeri-sembilan'].to_string(index=False))
pahang = float(df_first3['pahang'].to_string(index=False))
perak = float(df_first3['perak'].to_string(index=False))
perlis = float(df_first3['perlis'].to_string(index=False))
p_pinang = float(df_first3['pulau-pinang'].to_string(index=False))
sabah = float(df_first3['sabah'].to_string(index=False))
sarawak = float(df_first3['sarawak'].to_string(index=False))
selangor = float(df_first3['selangor'].to_string(index=False))
terengganu = float(df_first3['terengganu'].to_string(index=False))
wpkl = float(df_first3['wp-kuala-lumpur'].to_string(index=False))
wplabuan = float(df_first3['wp-labuan'].to_string(index=False))
wpputrajaya = float(df_first3['wp-putrajaya'].to_string(index=False))

height = [johor,kedah,kelantan,melaka,n_sembilan,pahang,perak,perlis,p_pinang,sabah,sarawak,
          selangor,terengganu,wpkl,wplabuan,wpputrajaya]

tick_label = ['johor', 'kedah', 'kelantan', 'melaka' , 'n-sembilan',  'pahang',  'perak',
              'perlis', 'pulau-pinang', 'sabah', 'sarawak', 'selangor', 'terengganu',
            'wp-kuala-lumpur' , 'wp-labuan',  'wp-putrajaya']

plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red','blue','green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()