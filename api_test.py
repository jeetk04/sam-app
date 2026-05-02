import json
from hello_world.app import lambda_handler

def simulate_api(method, path, query=None, body=None):
  event = {
    "httpMethod": method,
    "path": path,
    "queryStringParameters": query,
    "body": json.dumps(body) if body else None
  }
  return lambda_handler(event, None)

print("Get ->", simulate_api("GET", "/hello", query={"name": "RD"}))
print("POST ->", simulate_api("POST", "/hello", body={"name": "AWS"}))
print("GET missing ->", simulate_api("GET", "/hello"))
print("POST missing ->", simulate_api("POST", "/hello"))
