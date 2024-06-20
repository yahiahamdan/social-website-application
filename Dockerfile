FROM python:3.9-slim 

#set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev

COPY  bookmarks/requirements.txt /app/

COPY .env  /app/

# Print Python and pip versions for debugging
RUN python --version && pip --version


#install any needed pacakges speicief in requirments.txt
RUN pip install --no-cache-dir -r requirements.txt --verbose 

#copy the current directory contents into the container at /app
COPY . /app
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#expost port 8000 for django 
EXPOSE 8000

#run the command
#set the working directory
WORKDIR /app/bookmarks
CMD ["python", "manage.py", "runserver"]

