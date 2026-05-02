import json
import os
import base64
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  logger.info(f"Incoming event: {event}")

  try:
    method = event.get("httpMethod")
    env_name = os.environ.get("APP_ENV", "dev")
    
    if method == "GET":
        params = event.get("queryStringParameters") or {}
        name = params.get("name")
        if not name:
            return{
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'name' in query"})
            }

    elif method == "POST":
        body = event.get("body")
        if not body:
            return{
                    "statusCode": 400,
                "body": json.dumps({"error": "Missing request body"})
            }

        if event.get("isBase64Encoded"):
            body = base64.b64decode(body).decode("utf-8")

        if isinstance(body, str):
            body = json.loads(body)

        name = body.get("name")
        if not name:
            return{
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'name' in body"})
            }

    else: return{
            "statusCode": 405,
            "body": json.dumps({"error": "Method Not Allowed"})
          }

    logger.info(f"Response: {name}, method={method}, env={env_name}")

    return{
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello {name}",
            "environment": env_name,
            "method": method
         })
    }
  except Exception as e:
      return{
         "statusCode": 500,
         "body": json.dumps({"error": str(e)})
      }

