# Use the official Python image from the Docker Hub
FROM python:3.10.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y netcat-openbsd libffi-dev libssl-dev musl cron
RUN apt-get install --fix-broken
# Set the working directory
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip3 install --upgrade pip==23.2.1
RUN pip3 install -r requirements.txt
RUN pip3 cache purge

# Copy the project
COPY . /app/

# Expose port 8000 (default port for Django)
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
