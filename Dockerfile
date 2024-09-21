# Use the official Python image from the Docker Hub
FROM python:3.9-alpine3.13

# Set the maintainer label
LABEL maintainer="londonappdeveloper.com"

# Ensure stdout and stderr are flushed immediately
ENV PYTHONUNBUFFERED 1

# Copy the requirements files to the /tmp directory in the container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Copy the application code to the /app directory in the container
COPY ./app /app

# Set the working directory to /app
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Define a build argument for development mode
ARG DEV=false

# Create a virtual environment, install dependencies, and create a user
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # psycop2 dependency
    apk add --update --no-cache postgresql-client && \ 
    # sets virtual dependency package                           
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # install packages defined in requirements file
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    # remove installed packages, keeps Dockerfile lightweight
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Add the virtual environment to the PATH
ENV PATH="/py/bin:$PATH"

# Switch to the django-user
USER django-user