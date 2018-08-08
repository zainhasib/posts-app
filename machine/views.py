from django.shortcuts import render
import quandl
import numpy
import urllib3
import json

# Create your views here.
def index(request):

    http = urllib3.PoolManager()  
    r = http.request('GET',
        'https://api.github.com/users?since=135',
        headers={
            'User-Agent': 'https://api.github.com/meta'
        }
     )  
    d = json.loads(r.data.decode('utf-8'))
    data = []
    for dat in d:
        data.append(dat['url'])
    dataset = quandl.get("FINRA/FNRA_GOOGL", authtoken="D1Vh-5_33-PTdh9yi_Xz")

    context = {
        'title': 'Machine Learning Implementation',
        'dataset': dataset,
        'data': data
    }

    return render(request, 'machine/index.html', context)
