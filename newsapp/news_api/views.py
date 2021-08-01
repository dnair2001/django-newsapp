from django.shortcuts import render
import requests # this is the module we use to get all the information from that API
API_KEY = '9622319c139344ba9704bd198455cb64'
# Create your views here.
# do your api request

#parse all the info from the URL and the response is converted into JSON format
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url) #we get response from request
        data = response.json()
        # get into articles object iN JSON
        articles = data['articles']
    else:
        # parse information by category
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url) #we get response from request
        data = response.json()
        # get into articles object iN JSON
        articles = data['articles']


    # parse data which is stored into context variable 
    context = {
        'articles' : articles
    }

    # return news api context
    return render(request, 'news_api/home.html', context)
