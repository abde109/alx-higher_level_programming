#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes
curl -s "$1" --write-out '%{size_download}\n' --output /dev/null
