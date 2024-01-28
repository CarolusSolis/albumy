# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/CarolusSolis/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with conda: 
```
$ conda create -n albumy python=3.8
$ conda activate albumy
$ pip install -r requirements.txt
```

Create a Azure vision key, link: https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/

Create a file called `.env` in the root directory of the project and add the following configuration:
```
VISION_KEY=<your Azure vision key>
VISION_ENDPOINT=<your Azure vision endpoint>
```

generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
