import redis #python redis module
import requests

#connect to redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Function to fetch data (simulate API call)
def fetch_data_from_api(url):
    #https://jsonplaceholder.typicode.com/todos/1
    print("Fetching data from API...")
    respose = requests.get(url)
    return respose.text

# Function to get data with caching
def get_data_with_caching(url):
    #check if data is in cache
    cached_data = redis_client.get(url)

    if cached_data:
        print("Data found in cache")
        return cached_data.decode("utf-8")

    else:
        # Data not in cache, fetch from the API
        data = fetch_data_from_api(url)

        # Store data in cache for 30 seconds
        redis_client.setex(url, 30 , data)

        return data


sample_url = 'https://jsonplaceholder.typicode.com/posts/1'
cached_response = get_data_with_caching(sample_url)
print(cached_response)

# excute again
cached_response = get_data_with_caching(sample_url)
print(cached_response)
