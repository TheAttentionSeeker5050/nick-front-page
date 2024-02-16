# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# install Flask and pymongo
RUN pip install Flask pymongo python-dotenv

# Add any needed packages specified in requirements.txt
RUN pip freeze > requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable
# ENV MONGO_URI="mongodb://mongodb_host:27017/your_database"

# Run app.py when the container launches
CMD ["python", "app.py"]
