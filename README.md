# django-devcontainer

This repository contains a starter repository to develop an app using Django and Postrgres with a devcontainer.

## How to use

With a brand new project, the first step is to start the project in a development container, whether that's using vscode
or with neovim and devcontainer CLI.

Once the project is up, create the new Django project:

```shell
django-admin startproject mynewproject
cd mynewproject
python manage.py startapp mynewapp
```

To run the development environment and test the new Django app, simply run the dev server:

```shell
python manage.py runserver
```

## Deploymewnt

### Azure Pipelines

The current Azure Pipelines deployment builds the container image and pushes it to a Docker-compatible registry. Prior
to pushing the image, the service connection in Azure DevOps needs to be setup with Azure, and a runner available,
whether that's the Microsoft-hosted or self-hosted ones.

### Kubernetes

Coming soon

:::mermaid
graph LR
inet[Internet] --> lb[nginx-service]
lb --> web[nginx-deployment]
web -- "^/static" --> app[django-service]
app --> django[django-deployment]
