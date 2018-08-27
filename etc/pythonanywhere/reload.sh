#!/bin/bash

# bash strict mode
set -euo pipefail
IFS=$'\n\t'

curl -X POST -H "Authorization: Token ${PYTHONANYWHERE_API_TOKEN}" https://www.pythonanywhere.com/api/v0/user/${PYTHONANYWHERE_USERNAME}/webapps/${PYTHONANYWHERE_DOMAIN}/reload/
