import pandas as pd
from davomat.models import Davomat





davomat = Davomat.objects.all()

# data = {'Başlık 1': v1,
#         'Başlık 2': v1}

df = pd.DataFrame(davomat)

df.to_excel('test_jadval.xlsx', index=False)

df_read = pd.read_excel('test_jadval.xlsx')

print(df_read)
