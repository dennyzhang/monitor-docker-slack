# Introduction
Get Slack Notifications, When Containers Run Into Issues

Read more: https://www.dennyzhang.com/docker_monitor

# General Idea
1. Start a container in the target docker host.
2. This container will query status for all containers.

```curl -XGET --unix-socket /var/run/docker.sock http://localhost/containers/json```

3. Send slack notifications, we get matched of "unhealthy"

# How To Use
- Specify slack credentials via env

```
export SLACK_CHANNEL="#XXX"
export SLACK_USERNAME="XXX"
export SLACK_TOKEN="xoxp-XXX-XXX-XXX-XXXXXXXX"
```

- Start container to check
```
container_name="monitor-docker-slack"
# Start container to monitor docker healthcheck status
docker run -v /var/run/docker.sock:/var/run/docker.sock \
   -t -d --privileged -h $container_name \
   --name $container_name --restart=always \
   denny/monitor-docker-slack:latest
```

# More customization
- TODO: add message
export MSG_PREFIX="Docker Env in XXX"

- TODO: add whitelist for checking
