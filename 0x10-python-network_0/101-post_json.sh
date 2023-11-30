#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file
curl -sH "Content-Type: application/json" -d @"$2" "$1"
