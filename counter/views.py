from django.shortcuts import render

#hBluR909ifYpPghMYe7Lsw==OedcDrpwV8h2udQW
# Create your views here.
def home(request):
    import requests

    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'hBluR909ifYpPghMYe7Lsw==OedcDrpwV8h2udQW'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, 'main.html')