# TikTak
This is a simple script showing communication between docker containers.
>Based on [this post](https://habr.com/ru/post/554190/) from Habr 

## Before start
1) Install Docker on your PC
2) Clone this project on your PC

## Quick start
1) Open your terminal in this work dir
2) Type: 
>       docker-compose up -d
3) Open your browser and go to [localhost:5000](http://localhost:5000/) for check first container
>Hello, I am Tik service!
4) Open your browser and go to [localhost:5001](http://localhost:5001/) for check second container
>Hello, I am Tak service!
5) Open your browser and go to [localhost:5000/tik](http://localhost:5000/tik) for check communication between docker containers
>Tik ... Tak
6) Open your terminal and type for stop second service: 
>       docker stop tak-service-container
7) Now you can repeat point 5 to look: "Tik..." instead of "Tik... Tak"
>Tik...