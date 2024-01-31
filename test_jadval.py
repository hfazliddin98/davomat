import pandas as pd



df_read = pd.read_excel('talabalar.xlsx')


data = pd.DataFrame(df_read)

print(data)
print(data.values)
