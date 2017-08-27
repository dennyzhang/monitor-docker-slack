#!/bin/bash -e
python /monitor-docker-slack.py --whitelist "$WHITE_LIST" \
       --slack_channel "$SLACK_CHANNEL" --slack_username "$SLACK_USERNAME" \
       --slack_token "$SLACK_TOKEN" --msg_prefix "$MSG_PREFIX"
## File : monitor-docker-slack.sh ends
