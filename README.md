# Serverless API (AWS SAM + WSL + Docker)

## Overview
Local serverless backend using AWS SAM, Docker, and WSL.

## Features
- Lambda function (Python)
- API Gateway simulation (GET + POST)
- Local testing with SAM CLI
- Logging + environment variables

## Endpoints

### GET
```

curl "[http://127.0.0.1:3000/hello?name=RD](http://127.0.0.1:3000/hello?name=RD)"

```

### POST
```

curl -X POST [http://127.0.0.1:3000/hello](http://127.0.0.1:3000/hello) 
-H "Content-Type: application/json" 
-d '{"name":"AWS"}'

````

## Tech Stack
- AWS SAM
- Docker
- Python
- WSL (Ubuntu)

## Learnings
- Local Lambda simulation
- API Gateway routing
- Debugging (CPU, memory, networking)
- Git workflow

## Run locally

```bash
sam build --use-container
sam local start-api
````

## Author

Jeet

````

---

# 🚀 Step 2 — Commit README

```bash
git add README.md
git commit -m "add README for project documentation"
git push
```

---
