FROM node:lts-alpine AS build

WORKDIR /usr/src/app

COPY ./package.json .
RUN npm install

COPY . .
RUN npm build

# -----

FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY --from=build /usr/src/app/dist .

EXPOSE 80
