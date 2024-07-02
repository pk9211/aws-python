# GridMaker

## Terminology

* **gridmaker-image-input**: input_bucket where the input images
* **gridmaker-image-destination**: destination_bucket where image grids will be saved; presigned urls for image grids will be shared as output


## Running the GridMaker

### Local Script

```
$ cd s3/local-script
$ python3 -m venv path/to/venv
$ source path/to/venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
Converting: 16 source images. Creating: 4 x 4 grid.
```
### S3 Script

```
$ cd s3/s3-script
$ python3 -m venv path/to/venv
$ source path/to/venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py gridmaker-image-input gridmaker-image-destination
Converting: 16 source images. Creating 4 x 4 grid.
Create temp file /var/folders/_0/7b_1pb596659f77n6m09ndkw0000gn/T/tmplkakjz58.jpeg
Saved file to s3 bucket: gridmaker-image-destination, key: c16bcc5db3be9ab2ecd48aac74b1ee80.jpeg
Presigned url: https://gridmaker-image-destination.s3.amazonaws.com/c16bcc5db3be9ab2ecd48aac74b1ee80.jpeg?AWSAccessKeyId=AKIAQZDQV4BUIM3OPVWQ&Signature=0uB4Nznja4fLA9ANQty8lo2Ynps%3D&Expires=1713479789
```
