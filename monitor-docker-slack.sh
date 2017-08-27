#!/bin/bash -e
python /monitor-docker-slack.py --whitelist "$WHITE_LIST" \
       --slack_channel "$SLACK_CHANNEL" --slack_token "$SLACK_TOKEN" \
       --msg_prefix "$MSG_PREFIX" --check_interval "$CHECK_INTERVAL"
## File : monitor-docker-slack.sh ends
