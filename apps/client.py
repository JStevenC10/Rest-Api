import requests

ENDPOINT = 'http://127.0.0.1:8000/Api/'

def login():
    username = input('Username: ')
    password = input('Password: ')
    user = {
        "username": username,
        "password": password
    }
    response = requests.post(url=ENDPOINT + 'token/', data=user)
    return response.json()

# TOKEN AUTHORIZATION FOR API 
USER_LOGIN = login()
try:
    HEADERS = {
        'Authorization': 'Bearer {}'.format(USER_LOGIN['access'])
    }
except:
    HEADERS = None

# GET MOVIE
def get_api_movies(pk=None):
    if pk == None:
        response = requests.get(url=ENDPOINT + 'Movies', headers=HEADERS)
    else:
        response = requests.get(url=ENDPOINT + 'Movies/{}/'.format(pk), headers=HEADERS)
    return response.json()
print(get_api_movies(1))

# POST NEW MOVIE
def post_api_movie():
    new_movie = {
        'name': 'Megalodon',
        'resume': 'Prehistoric animal is deep sea',
        'clasification': '+18',
        'release_date': '2021-03-12',
        'available': True,
    }
    response = requests.post(url=ENDPOINT + 'Movies/', data=new_movie, headers=HEADERS)
    return response.json()
# print(post_api_movie())

# PATCH OR PARTIAL_UPDATE MOVIE
def update_api_movie(pk):
    new_name = {
        'name': 'Megalodon',
        "release_date": "2020-12-10"
    } 
    response = requests.patch(url=ENDPOINT + 'Movies/{}/'.format(pk), data=new_name, headers=HEADERS)
    return response.json()
# print(update_api_movie(1))

# DELETE MOVIE
def delete_api_movie(pk):
    response = requests.delete(url=ENDPOINT + 'Movies/{}/'.format(pk), headers=HEADERS)
    return response.json()
print(delete_api_movie(3))