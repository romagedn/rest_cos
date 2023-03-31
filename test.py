
import requests
import json
import base64

filename = './data/face.png'


with open(filename, 'rb') as fp:
    img = fp.read()
    img64 = base64.standard_b64encode(img).decode()
    img_ = base64.standard_b64decode(img64)
    data = json.dumps({
        'image64': img64,
    })

    header = {
        "Content-Type": "text/plain",
    }
    response = requests.post(url='http://localhost:13130/upload', data=data, headers=header)
    print(response.content)
