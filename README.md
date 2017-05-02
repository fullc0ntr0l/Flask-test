# Flask test restful API
### Install
```
pip install -r requirements.txt
python run_api.py
```

POST to localhost:5000/image:
payload: {
image: base64 string
}

returns: {
id: image_id
}

GET from localhost:5000/image/<image_id>
returns: {
image: base64 string
}

### Running inside docker
```
sudo docker-compose up --build
```