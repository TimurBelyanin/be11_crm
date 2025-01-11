# my first image
FROM alpine:latest AS base
ARG buildno=1

WORKDIR /
WORKDIR app

RUN touch test.txt && echo "Hello, nigga" > test.txt

COPY crm crm