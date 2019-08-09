#!/bin/bash -ex
python /monitor-docker-slack.py  --check_interval "$CHECK_INTERVAL" \
       --slack_token "$SLACK_TOKEN" --whitelist "$WHITE_LIST" \
       --slack_channel "$SLACK_CHANNEL" --msg_prefix "$MSG_PREFIX" \
       --slack_username "$SLACK_USERNAME"
## File : monitor-docker-slack.sh ends
