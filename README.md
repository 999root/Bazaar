<h1 align="center">Bazaar</h1>

**Bazaar** is a web application that allows users to browse and download files from a public directory. This project is containerized using Docker to ensure an easy setup and deployment process.

## Features

- Browse files in a public directory
- Download files with ease
- Simple setup with Docker

## Getting Started

These instructions will help you get Bazaar up and running on your local machine.

### Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)

### Installation

#### 1. Clone the Repository

```bash
git clone <repository_url>
cd Bazaar
```

#### 2. Build the Docker Image
To build the Docker image locally:

```bash
docker build -t bazaar .
```

#### 3. Run the Docker Container
Once the image is built, you can run it with:

```bash
docker run -p 8080:80 bazaar
```

This command will start the Bazaar application on port 8080. You can change the port if needed by modifying the -p flag.

#### Pulling from Docker Hub (Optional)
If the image is hosted on Docker Hub, you can pull it directly:

```bash
docker pull your-dockerhub-username/bazaar:latest
docker run -p 8080:80 your-dockerhub-username/bazaar
```

Usage

Once the container is running, open your browser and go to:

```bash
http://localhost:8080
```

You should now see the Bazaar interface, where you can browse and download files.
