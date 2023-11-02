import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)
zee = redis_client.get('username')

redis_client.set('msw_fundamental_data', json.dumps({"pe": 33}))

print(zee)

