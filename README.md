<p align="center">
    <a href="/">
        <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build" />
    </a>
    <a href="https://www.djangoproject.com/">
        <img src="https://img.shields.io/badge/django-2.0-blue.svg" alt="django" />
    </a>
    <a href="https://getbootstrap.com/">
        <img src="https://img.shields.io/badge/bootstrap-4.0-orange.svg" alt="Bootstrap" />
    </a>
    <a href="https://github.com/mahmudahsan/pythonbangla.com/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License" />
    </a>
    <a href="https://twitter.com/mahmudahsan">
        <img src="https://img.shields.io/badge/contact%40-mahmudahsan-red.svg" alt="Twitter: @mahmudahsan" />
    </a>
</p>

# pythonbangla.com
A dynamic content management system for publishing youtube videos and blog post in a single page web application.
I developed this web app to place all my youtube video tutorials and related blog post links in one place. 
Demo: [Pythonbangla.com](http://pythonbangla.com)

## Usage
If you know django, postgresql, bootstrap you can easily modify html template and backend according to your project needs. But if you just want a site like the demo [Pythonbangla.com](http://pythonbangla.com) you can change the images in static directory in the project, and add contents from your or your client's youtube channel or blog post. To know how to setup, follow the table of contents.

# Table of Contents

- [Technology Used](#technology-used)
- [Features](#features)
- [Setup in local machine](#setup-in-local-machine)
- [Setup PostgreSQL in local machine](#setup-postgresql-in-local-machine)
- [How to use admin panel to manage contents](#how-to-use-admin-panel-to-manage-contents)
- [Setup Amazon S3 CDN to upload static content](#setup-amazon-s3-cdn-to-upload-static-content)
- [Setup And Running in Heroku without static content](#setup-and-running-in-heroku-without-static-content)
- [Setup And Running in Heroku with static content](#setup-and-running-in-heroku-with-static-content)
- [How to force https in django](#how-to-force-https-in-django)
- [Contribution](#contribution)
- [Questions or feedback?](#questions-or-feedback)

## Technology Used
1. [Django](https://www.djangoproject.com/)
2. [PostgreSQL](https://www.postgresql.org)
3. [Bootstrap](https://getbootstrap.com/)
4. [JQuery](https://jquery.com/)
5. [Linkyfy](https://github.com/cowboy/javascript-linkify)

## Features
1. Responsive single page webapp
2. Admin Panel for content management
3. Automatic playlist created based on content
4. Mainly developed for youtube videos
5. Blog post or external link list also supported
6. Youtube video description also can be added from admin panel
7. In description, link automatically converted to hyperlink
8. In Admin easy way to add javascript code within head tag
9. Easy way to add Google Analytics or Google Adsense auto ads

## Setup in local machine

1. First clone this project or fork and clone your fork url
```shell
git clone https://github.com/mahmudahsan/pythonbangla.com.git djangodemo
cd djangodemo # Enter the project dir
```

2. Now run and install django by [pipenv](https://docs.pipenv.org)

```shell
pipenv install django
pipenv shell # Activate pipenv
```

### Setup PostgreSQL in local machine

1. Downlaod and install [PostgreSQL](https://www.postgresql.org/download/) 
2. Run the PostgreSQL in your machine
3. Download [pgAdmin](https://www.pgadmin.org) if you prefer managing PostgreSQL visually
4. Run pgAdmin to create database visually
5. Or Create a database in PostgreSQL in terminal
6. Update django frameworks's project settings djangodemo/pythonbangla_project/settings.py

```Python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "YOUR_LOCAL_DB_NAME",
        "USER": "YOUR_POSTGRESQL_USER_NAME",
        "PASSWORD": "YOUR_POSTGRESQL_PASSWORD",
        "HOST": "localhost", 
        "PORT": "5432", # usually this port unless your port is different
    }
}
```
7. Apply database migration from django to postgresql
This will convert all the models to SQL tables in postgresql

```shell
python3 manage.py migrate
```

8. Start django server locally
```shell
python3 manage.py runserver
```

9. Visit http://127.0.0.1:8000/ in a web browser. You will see the following blank webpage without any contents
<p align="center">
    <img src="github-readme-assets/demo1.png" width="800" alt="demo 1" />
</p>	

10. Quit the server with CONTROL-C in terminal 
```shell
CONTROL-C
```

## How to use admin panel to manage contents

1. First create a superuser
```shell
python3 manage.py createsuperuser
```
2. Now run the server again
```shell
python3 manage.py runserver
```
3. Now in web browser visit http://127.0.0.1:8000/admin . Login with the superuser name and password you created already.

You will see the following admin panel with 4 tables
<p align="center">
    <img src="github-readme-assets/demo2.png" width="800" alt="demo 2" />
</p>	

4. Now add a topic category. Click the [+ Add] button

You will see the following form
<p align="center">
    <img src="github-readme-assets/demo3.png" width="800" alt="demo 3" />
</p>	

Now fill the form for our demo purpose. In later you can modify/remove/add anything according to your requirments. After filling, SAVE the form.

| Column  	|  Data 	|
|---	    |---	|
|  Title English 	|   Python Beginner	|
|  Title Other 	|   পাইথন বিগিনার	|
|  Short Description 	|   পাইথন দিয়ে আমরা একটা ওয়েব অ‍্যাপ বানাই।	|
|  Image Name	|   py-beg.png	|
|  Topic Type 	|   Youtube	|

 py-beg.png image already stored in projects djangodemo/static/img/py-beg.png. So if you want to use other image, please put that on this directory and mention the name in the form.
 
 5. Now go to Home › Main_App and click [+ Add] in Topic Contents
 
 You will see the following form. Fill with some data like the demo and click SAVE. 
 
 * Url is used for Blog Post link, so for youtube no need. 
 * Tag is optional as well. If you put tag, it will be shown in the home page playlist. 
 * Order is used to rank list item accordingly.
 
<p align="center">
    <img src="github-readme-assets/demo4.png" width="800" alt="demo 4" />
</p>
 
 6. Now visit http://127.0.0.1:8000 again 
 
 You will see the following web page
 
 <p align="center">
    <img src="github-readme-assets/demo5.png" width="800" alt="demo 5" />
</p>

7. To publish URL links like the following example
 
 <p align="center">
    <img src="github-readme-assets/demo6.png" width="800" alt="demo6" />
 </p>
 
 * Add a topic category and set the Topic Type URL
 
 <p align="center">
    <img src="github-readme-assets/demo7.png" width="800" alt="demo7" />
 </p>

* Add topic content and provide Title and URL

 <p align="center">
    <img src="github-readme-assets/demo8.png" width="800" alt="demo8" />
 </p>

Now visit http://127.0.0.1:8000 again to see the updates

#### Social Links
1. 


## Setup Amazon S3 CDN to upload static content 
Django by default doesn't support serving static files in production. 

## Setup And Running in Heroku without static content 

## Setup And Running in Heroku with static content

## How to force https in django

## Contribution
If you want to contribute on this project, you're welcome to fork the project and submit a pull request. Just try to not break the existing things.

## Questions or feedback?

Feel free to [open an issue](https://github.com/mahmudahsan/pythonbangla.com/issues/new), or find me [@mahmudahsan on Twitter](https://twitter.com/mahmudahsan).
