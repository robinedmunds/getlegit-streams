# GETLEGIT! streams

## Purpose

Provide simple, cloud based service for streaming desktops/games between friends.

## Issues

To play streaming video in a browser requires that the video be converted from the RTMP format to the browser compatible HLS. This software can do this, however it is a CPU intensive process utilising ffmpeg and so the relevant code has been disabled to fit my use case.

## Dependencies

1. linux box running docker engine/podman
2. docker-compose
3. OBS (or equivalent encoding/streaming software)
4. VLC or other modern video player

## Setup

### Server

1. clone repo
2. define global stream key in .env file at root of repo: `AUTH_STREAM_KEY=LONG-STREAM-KEY`
3. run `docker-compose up -d` to start the docker containers

### Streamer

1. in OBS stream settings: -
   1. Server: `rtmp://domain.example:1935/stream?$LONG-STREAM-KEY`
   2. Stream key: `$CHANNEL_NAME`

### Client

1. open VLC, press Ctrl+N
2. `rtmp://domain.example/stream/$CHANNEL_NAME`

## Borrowed building blocks

### RTMP

1. http://nginx-rtmp.blogspot.com/
2. [nginx-rtmp module pre-compiled inside a Docker image](https://github.com/alfg/docker-nginx-rtmp)

### Authentication

Ensures that only permitted users who hold a global stream key can stream to the service.

1. code forked from: [Nesseref/nginx-rtmp-auth](https://github.com/Nesseref/nginx-rtmp-auth)

### Web playback

Live stream capable web player. Stream must be transcoded from RTMP to HLS for the web UI to function.

1. [VideoJS, HTML5 player](https://videojs.com/)

## License

All code MIT license bar that contained within the frontend directory. Logos and images are protected by copyright.

