import urllib.request
import pandas as pd

def extract_data(url,filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        print(e)

extract_data('https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/c9509ab4-6f6d-4b97-979a-0cf2a10c922b/download/tmphrybkxuh.csv',"data/data_2015.csv")    
extract_data('https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/b7ea6b1b-3ca4-4c5b-9713-6dc1db52379a/download/tmpzxzxeqfb.csv',"data/data_2016.csv")
extract_data('https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/30022137-709d-465e-baae-ca155b51927d/download/tmpzccn8u4q.csv',"data/data_2017.csv")
extract_data('https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/2be28d90-3a90-4af1-a3f6-f28c1e25880a/download/tmp7602cia8.csv',"data/data_2018.csv")
extract_data('https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/ea2e4696-4a2d-429c-9807-d02eb92e0222/download/tmpcje3ep_w.csv',"data/data_2019.csv")
extract_data('https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/6ff6a6fd-3141-4440-a880-6f60a37fe789/download/tmpcv_10m2s.csv',"data/data_2020.csv")

arquivos = [
"data/data_2015.csv",
"data/data_2016.csv",
"data/data_2017.csv",
"data/data_2018.csv",
"data/data_2019.csv",
"data/data_2020.csv"   
]

dfs={}

for arquivo in arquivos:
    ano = arquivo.split("_")[-1].split(".")[0]
    dfs[ano] = pd.read_csv(arquivo)
    