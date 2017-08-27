#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : healthcheck-notify-slack.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-08-20>
## Updated: Time-stamp: <2017-08-27 11:43:50>
##-------------------------------------------------------------------
import requests

def send_slack_notification(slack_channel, slack_token, msg_title, msg_content):
    # TODO
    return True

def list_containers_by_sock(docker_sock_file):
    container_list = []
    return container_list

def get_unhealthy_containers(container_list):
    unhealthy_container_list = []
    return unhealthy_container_list

if __name__ == '__main__':
    docker_sock_file = "/var/run/docker.sock"
    container_list = list_containers_by_sock(docker_sock_file)
    test()
## File : healthcheck-notify-slack.py ends
