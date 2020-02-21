#!/bin/bash -ex
python /monitor-docker-slack.py  --check_interval "$CHECK_INTERVAL" \
       --slack_webhook "$SLACK_WEBHOOK" --whitelist "$WHITE_LIST" \
       --msg_prefix "$MSG_PREFIX"
## File : monitor-docker-slack.sh ends
