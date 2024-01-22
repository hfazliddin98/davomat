import pandas as pd
from davomat.models import Davomat

v1 = []
for d in range(20):
    d += 1
    v1.append(str(d))
print(v1)

kun = []
for s in range(10):
    s += 1
    kun.append(str(s))
print(kun)

data1 = []
for v in v1:
    v2 = f"{v}"
    data1.append(v2)

davomat = Davomat.objects.all()

data = {'Başlık 1': v1,
        'Başlık 2': v1}

df = pd.DataFrame(davomat)

df.to_excel('test_jadval.xlsx', index=False)

df_read = pd.read_excel('test_jadval.xlsx')

print(df_read)
