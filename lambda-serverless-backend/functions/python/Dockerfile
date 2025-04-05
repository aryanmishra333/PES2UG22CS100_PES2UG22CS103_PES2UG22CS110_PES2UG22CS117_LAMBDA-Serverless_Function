# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the function file into the container
COPY function.py .

# Command to execute the function
# earlier: CMD ["python", "function.py"]
ENTRYPOINT ["python", "function.py"]