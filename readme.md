# Quart Uvicorn Web App Template

This is a template to quickly get a quart web app running. 

## Installing dependencies

### With Conda

    conda create --name quart-app python=3.9
    conda install --file requirements.txt
    conda activate quart-app

## Development Server

This template comes with a development server that will automatically reload when files are changed.

    python dev_server.py

## Deployment With Docker

    docker build -t quart-hello-world .
    docker run -d -p 80:80 quart-hello-world

