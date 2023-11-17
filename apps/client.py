import requests

ENDPOINT = 'http://127.0.0.1:8000/Api/'

# GET MOVIE
def get_api_movies(pk=None):
    if pk == None:
        response = requests.get(url=ENDPOINT + 'Movies')
    else:
        response = requests.get(url=ENDPOINT + 'Movies/{}/'.format(pk))
    return response.json()

# POST NEW MOVIE
def post_api_movie():
    new_movie = {
        'name': 'Megalodon',
        'resume': 'Prehistoric animal is deep sea',
        'clasification': '+18',
        'release_date': '2021-03-12',
        'available': True,
    }
    response = requests.post(url=ENDPOINT + 'Movies/', data=new_movie)
    return response.json()

# print(post_api_movie())

# PATCH OR PARTIAL_UPDATE MOVIE
def update_api_movie(pk):
    new_name = {
        'name': 'Megalodon',
        "release_date": "2020-12-10"
    } 
    response = requests.patch(url=ENDPOINT + 'Movies/{}/'.format(pk), data=new_name)
    return response.json()

# print(update_api_movie(1))

# DELETE MOVIE
def delete_api_movie(pk):
    response = requests.delete(url=ENDPOINT + 'Movies/{}/'.format(pk))
    return response.json()

# print(delete_api_movie(3))