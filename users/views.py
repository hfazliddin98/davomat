from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from davomat.models import Davomat


def home(request):
    davomat = Davomat.objects.all()

    data = []
    for d in davomat:
        data.append(d.id, d.bor)

    df = pd.DataFrame(data)

    df.to_excel('test_jadval.xlsx', index=False)

    df_read = pd.read_excel('test_jadval.xlsx')

    print(df_read)
    return HttpResponse('<h1>Bosh sahifa</h1>') 