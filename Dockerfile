########## How To Use Docker Image ###############
##
##  Image Name: denny/monitor-docker-slack:latest
##  Git link: https://github.com/DennyZhang/monitor-docker-slack/blob/master/Dockerfile
##  Docker hub link:
##  Build docker image: docker build --no-cache -t denny/monitor-docker-slack:latest --rm=true .
##  How to use:
##      https://github.com/DennyZhang/monitor-docker-slack/blob/master/README.md
##
##  Description: Send slack alerts, if any containers run into unhealthy
##
##  Read more: https://www.dennyzhang.com/docker_monitor
##################################################
# Base Docker image: https://hub.docker.com/_/python/

FROM python:3.6.2-jessie

ENV SLACK_CHANNEL ""
ENV SLACK_TOKEN ""

ENV MSG_PREFIX ""
ENV WHITE_LIST ""
# seconds
ENV CHECK_INTERVAL "300"

LABEL maintainer="Denny<https://www.dennyzhang.com/contact>"

USER root
WORKDIR /
ADD monitor-docker-slack.py /monitor-docker-slack.py
ADD monitor-docker-slack.sh /monitor-docker-slack.sh

RUN chmod o+x /*.sh && chmod o+x /*.py && \
    pip install -r requirements.txt && \
# Verify docker image
    pip show requests-unixsocket | grep "0.1.5" && \
    pip show slackclient | grep "1.3.0"

ENTRYPOINT ["/monitor-docker-slack.sh"]
