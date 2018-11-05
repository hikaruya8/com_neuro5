import pandas as pd
df = pd.read_csv('data.txt', sep='\t')
num = df["n"]
color_num = df["Yn"]
blue_num = 0
red_num = 0
for c in color_num:
    if c  == 1:
        blue_num += c
        if n == 20:
            break
        print(blue_num)