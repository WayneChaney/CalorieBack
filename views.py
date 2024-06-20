from django.shortcuts import render

#hBluR909ifYpPghMYe7Lsw==OedcDrpwV8h2udQW
# Create your views here.
def home(request):
    import json
    import requests
#doing Post method
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'hBluR909ifYpPghMYe7Lsw==OedcDrpwV8h2udQW'}) 
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "NOOO ERROR"
            print (e)
        return render(request, 'main.html', {'api':api})
    else:
        return render(request, 'main.html',{'query': 'Enter a valid query'})


    # query = '1lb brisket and fries'
    # api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    # response = requests.get(api_url, headers={'X-Api-Key': 'hBluR909ifYpPghMYe7Lsw==OedcDrpwV8h2udQW'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)

    # return render(request, 'main.html')