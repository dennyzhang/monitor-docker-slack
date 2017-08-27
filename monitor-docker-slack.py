#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : monitor-docker-slack.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-08-20>
## Updated: Time-stamp: <2017-08-27 14:08:21>
##-------------------------------------------------------------------
import requests
import re
import requests_unixsocket
import json
import argparse

def send_slack_notification(slack_channel, slack_token, msg_title, msg_content):
    # TODO
    return True

def name_in_list(name, name_pattern_list):
    for name_pattern in name_pattern_list:
        if re.search(name_pattern, name) is not None:
            return True
    return False
################################################################################

def list_containers_by_sock(docker_sock_file):
    session = requests_unixsocket.Session()
    container_list = []
    socket = docker_sock_file.replace("/", "%2F")
    url = "http+unix://%s/%s" % (socket, "containers/json?all=1")
    r = session.get(url)
    # TODO: error handling
    assert r.status_code == 200
    for container in json.loads(r.content):
        item = (container["Names"], container["Status"])
        container_list.append(item)
    return container_list

# TODO: simplify this by lambda
def get_stopped_containers(container_list):
    stopped_container_list = []
    for container in container_list:
        (names, status) = container
        if "Exited" in status:
            stopped_container_list.append(container)
    return stopped_container_list

def get_unhealthy_containers(container_list):
    unhealthy_container_list = []
    for container in container_list:
        (names, status) = container
        if "unhealthy" in status:
            unhealthy_container_list.append(container)
    return unhealthy_container_list

# TODO: simplify this by lambda
def containers_remove_by_name_pattern(container_list, name_pattern_list):
    l = []
    for container in container_list:
        (names, status) = container
        has_matched = False
        for name in names:
            if name_in_list(name, name_pattern_list) is True:
                has_matched = True
                break
        if has_matched is False:
            l.append(container)
    return l

def container_list_to_str(container_list):
    msg = ""
    for container in container_list:
        (names, status) = container
        msg = "%s: %s\n%s" % (names, status, msg)
    return msg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--whitelist', default='', required=False, \
                        help="Skip checking certain containers. A list of regexp separated by comma.", type=str)
    parser.add_argument('--check_interval', default='300', required=False, \
                        help="Periodical check. By seconds.", type=int)
    l = parser.parse_args()

    check_interval = l.check_interval
    docker_sock_file = "/var/run/docker.sock"

    # TODO: add a loop
    container_list = list_containers_by_sock(docker_sock_file)
    stopped_container_list = get_stopped_containers(container_list)
    unhealthy_container_list = get_unhealthy_containers(container_list)

    name_pattern_list = l.whitelist.split(',')
    stopped_container_list = containers_remove_by_name_pattern(stopped_container_list, name_pattern_list)
    unhealthy_container_list = containers_remove_by_name_pattern(unhealthy_container_list, name_pattern_list)
    
    print("stopped_container_list: %s\n\nunhealthy_container_list: %s" % \
          (container_list_to_str(stopped_container_list), container_list_to_str(unhealthy_container_list)))
## File : monitor-docker-slack.py ends
