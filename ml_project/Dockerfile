# # syntax=docker/dockerfile:1

# # Comments are provided throughout this file to help you get started.
# # If you need more help, visit the Dockerfile reference guide at
# # https://docs.docker.com/go/dockerfile-reference/

# # Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

# ARG PYTHON_VERSION=3.10.12
# FROM python:${PYTHON_VERSION}-slim as base

# # Prevents Python from writing pyc files.
# ENV PYTHONDONTWRITEBYTECODE=1

# # Keeps Python from buffering stdout and stderr to avoid situations where
# # the application crashes without emitting any logs due to buffering.
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# # RUN pip3 install opencv-python-headless==4.9.0.80
# # RUN pip3 install opencv-contrib-python-headless==4.9.0.80

# # RUN pip3 install opencv-python-headless==4.8.1.78
# # RUN pip3 install opencv-contrib-python==4.8.1.78

# RUN apt-get update && apt-get install -y libgl1

# # Download dependencies as a separate step to take advantage of Docker's caching.
# # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# # Leverage a bind mount to requirements.txt to avoid having to copy them into
# # into this layer.
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=ml_project/deployment_req.txt,target=ml_project/deployment_req.txt \
#     python -m pip install -r ml_project/deployment_req.txt

# # Switch to the non-privileged user to run the application.
# USER appuser

# # Copy the source code into the container.
# COPY . .

# # Expose the port that the application listens on.
# EXPOSE 8000

# # Run the application.
# CMD python3 ml_project/manage.py runserver

# -------------------------------

# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update && apt-get install -y libgl1
COPY deployment_req.txt /code/
RUN pip install -r deployment_req.txt
# RUN pip install psycopg2-binary
COPY . /code/