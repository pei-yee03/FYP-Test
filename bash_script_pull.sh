#!/usr/bin/env bash
# This bash script serves as a preliminary function to test pulling specific files from GitHub.

set -euo pipefail
# Reference to bash strict mode: https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425?permalink_comment_id=3935570

curl -sSL "https://raw.githubusercontent.com/pei-yee03/FYP-Test/main/model_roles/tester" -o "testing_file"
# Structure of URL should be "https://raw.githubusercontent.com/${user}/${repo}/${branch}/${filepath}"