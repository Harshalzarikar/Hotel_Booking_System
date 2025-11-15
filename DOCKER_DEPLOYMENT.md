# Docker Deployment Guide

## Prerequisites
- Docker installed in WSL
- WSL2 enabled on Windows

## Deployment Steps

### 1. Open WSL Terminal
Navigate to your project directory:
```bash
cd /mnt/c/Users/Asus/Desktop/hotel_booking_project
```

### 2. Build and Run with Docker Compose
```bash
docker-compose up --build
```

This will:
- Build the Docker image
- Install all dependencies
- Collect static files
- Start the application on port 8000

### 3. Access Your Application
Open your browser and go to:
```
http://localhost:8000
```

## Alternative Docker Commands

### Build image only:
```bash
docker build -t hotel-booking-app .
```

### Run container manually:
```bash
docker run -p 8000:8000 -e DEBUG=False hotel-booking-app
```

### Stop the application:
```bash
docker-compose down
```

### View logs:
```bash
docker-compose logs -f
```

### Rebuild after changes:
```bash
docker-compose up --build
```

## Troubleshooting

### Port already in use:
```bash
# Change port in docker-compose.yml from "8000:8000" to "8001:8000"
# Then access at http://localhost:8001
```

### Permission issues in WSL:
```bash
sudo docker-compose up --build
```

### Clear everything and restart:
```bash
docker-compose down
docker system prune -a
docker-compose up --build
```
