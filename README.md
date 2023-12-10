# FastAPI - Product CRUD

API for CRUD operations on product model

## Run
Run locally using 
```bash
python3 -m uvicorn main:app --reload
```

## Docker

Create docker image
```bash
docker build -t myimage .
```

Run docker imagage
```bash
docker run -d --name mycontainer -p 80:80 myimage
```
