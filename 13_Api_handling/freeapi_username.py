# import requests

# def fetch_random_user_freeapi():
#     url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
#     response=requests.get(url)
#     data=response.json()
    
    
#     if data ["success"] and "data" in data and "data" in data["data"]:
#         user_data=data["data"]["data"]
#         username=user_data["login"]["username"]
#         country=user_data["location"]["country"]
#         return username,country
#     else:
#         raise Exception("Failed to fetch user data")
    
# def main():
#     try:
#         username,country=fetch_random_user_freeapi()
#         print(f"Username:{username}\n Country:{country}")
#     except Exception as e:
#         print(str(e))

# if __name__=="__main__":
#     main()



#--------------------------------------------------------------------------------------------------------------------------------


import requests
import random

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
    
    if data.get("success") and "data" in data and "data" in data["data"]:
        user_data_list = data["data"]["data"]  # Correctly access the list of users
        random_user = random.choice(user_data_list)  # Select a random user
        username = random_user["login"]["username"]
        country = random_user["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
