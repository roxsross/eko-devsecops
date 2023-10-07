# FROM node:19.4.0-bullseye-slim
FROM node:19-alpine

LABEL org.opencontainers.image.description="vulnerable-node" \
      org.opencontainers.image.authors="RoxsRoss" 

ENV STAGE "DOCKER"

RUN apk add --no-cache netcat-openbsd

# Build app folders
RUN mkdir /app
WORKDIR /app

# Install depends
COPY package.json /app/
RUN npm install

# Bundle code
COPY . /app

EXPOSE 3000

CMD [ "npm", "start" ]
