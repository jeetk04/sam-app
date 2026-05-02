import json
from hello_world.app import lambda_handler

with open("event.json") as f:
	event = json.load(f)

response = lambda_handler(event, None)
print(response)
