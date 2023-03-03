import requests ,json

image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLmKLoGBUEyX_bQ35xGNK5iMAeiTai5OjJbmLRWlN6JqzvzbyoiM_UBI3HA_g&s'

response = requests.get(image_url)

with open("test.jpg","wb") as file:
    file.write(response.content)
    