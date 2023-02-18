import requests
from datetime import datetime
USERNAME = "karan684"
TOKEN = "jkh34jkb3v453lj35dsxz"
pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "DSA Ques",
    "unit": "ques",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

add_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many dsa ques did u do today? ")
}

# response=requests.post(url=add_pixel_endpoint,json=add_pixel_config,headers=headers)
# print(response.text)

update_endpoint = f"{add_pixel_endpoint}/{datetime(year=2023,month=2,day=17).strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "18"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{add_pixel_endpoint}/{datetime(year=2023,month=2,day=17).strftime('%Y%m%d')}"

response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)
