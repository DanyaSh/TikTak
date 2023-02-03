# TikTak
This is a simple script showing communication between docker containers.
>Based on [this post](https://habr.com/ru/post/554190/) from Habr 

# Quick start
0.1) Install Docker on your PC
0.2) Clone this project on your PC
1) Open your terminal in this work dir
2) Type: docker-compose up -d
2.1) Just wait a little
3) Open your browser and go to [localhost:5000](http://localhost:5000/) for check first container
4) Open your browser and go to [localhost:5001](http://localhost:5001/) for check second container
5) Open your browser and go to [localhost:5000/tik](http://localhost:5000/tik) for check communication between docker containers
6) Open your terminal and type: docker stop tik-service-container
7) Now you can repeat point 5 to look: "Tik..." instead of "Tik... Tak"