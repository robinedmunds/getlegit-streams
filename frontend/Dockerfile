FROM node:lts-alpine AS build

ENV NODE_ENV=development

WORKDIR /usr/src/app

COPY ./package.json .
RUN npm install

COPY . .
RUN npm run build

# -----

FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY --from=build /usr/src/app/dist .

EXPOSE 80
