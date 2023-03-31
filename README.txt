
upload file 2 tecent COS


pip install -r requirements.tzt


./config.txt

{
    "secret_id": secret_id,
    "secret_key": secret_key,
    "region": region,
    "Bucket": Bucket,
}


request

Content-Type: text/plain
body
{
    "image64": base64 encode png data
}


response

{
    "status": True / False,
    "storage_url": file storage url
}


port
13130

