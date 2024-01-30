# Use the official Node.js image as the base image
FROM node:14 AS build-stage

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . /app

# Build the Vue.js application
RUN npm run build

# Use the official Nginx image as the second base image
FROM nginx:1.21-alpine as production-stage

# Copy the built app from the build stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy the Nginx configuration file
COPY /nginx-custom.conf /app/nginx-custom.conf

# Expose port 80
EXPOSE 80

# Start Nginx and substitute the envar in the nginx config with the appTier references (taken from config map that takes them from Helm)
CMD ["/bin/sh" , "-c" , "envsubst '$VUE_APP_API_PORT' < /app/nginx-custom.conf > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
