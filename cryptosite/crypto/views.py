from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    import requests
    import json

    #Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,BCH,ETH,BCH,EOS,LTC,BCH,ETC,ZEC,QTUM,NEO,BSV,BGG,DASH,BNB,OKB,ABT,ZB,ONT,OMG,XMR,AE,TRUE,DOGE,RVN,XLM,ADA,USDT,MIOTA,TRX,XRP,RVN,HT,IOST,PAX,OCN,SWFTC,BTT,FET,TUSD,GTC,TCH,BTS,TCC,WAVES,ICX,IOT,XEM,ZIL,BAT,IHT,BMX,SNT&tsyms=INR")
    price = json.loads(price_request.content)

    return render(request, 'index.html', {'price': price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=INR")
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Enter a crypto currency symbol into a form above..."
        return render(request, 'prices.html', {'notfound': notfound})

def news(request):
    import requests
    import json

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'news.html', {'api': api})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

