# Django Instagram-like Project


## About 

This is my study project in which I tried to replicate 
an Instagram-like blog.

I wrote it in Django, I used PostgreSQL as the database. Also, I added MinIO 
for storing pictures and Celery (and RabbitMQ) for sending 
confirmation emails. In the end, I packed it into docker-compose.

I started with writing some technical requirements and designing 
project and database structure (you may find it in docs directory).
Then I created Django project with all basic functionality. 
After that I applied a ready-made page template to the project. 
Finally, I added Postgres, Minio and Celery and dockerized the app. 

## Technology stack

- Django
- Postgres
- Minio
- Celery
- RabbitMQ

## Install

1. Set up your environment variables in .env file.
2. Run `docker-compose build` and `docker-compose up` in the root directory.


## Screenshots

![screen_main.png](docs%2Fscreen_main.png)


![screen_post.png](docs%2Fscreen_post.png)


![screen_profile.png](docs%2Fscreen_profile.png)
