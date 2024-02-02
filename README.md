# Django Rating App

This is a Django project that includes a rating system for articles, with caching implemented using Redis.

## Features

- Article listing with average rating and rated count
- Rate articles with a score between 0 and 5
- Caching of average rating and rated count using Redis
- You can find requirements of this project [here](https://github.com/mostafa-msn/articles-rating/blob/main/requirements.txt)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/mostafa-msn/articles-rating.git

2. Run with Docker
    
   ```bash
    docker-compose up -d --build