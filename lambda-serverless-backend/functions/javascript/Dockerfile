# Use the official Node.js image as a base
FROM node:18-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file into the container
COPY package.json .

# Install dependencies
RUN npm install

# Copy the function file into the container
COPY function.js .

# Use ENTRYPOINT so additional args are passed to function.js
#earlier: CMD ["node", "function.js"]
ENTRYPOINT ["node", "function.js"]  