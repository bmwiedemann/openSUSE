#!/bin/bash


CLIENT_VERSION=$(tar -xzOf runthis-sphinxext-0.0.3.tar.gz runthis-sphinxext-0.0.3/setup.py | awk '/^CLIENT_VERSION/ {print gensub("\"", "", "G", $3)}')

wget https://github.com/regro/runthis-client/releases/download/${CLIENT_VERSION}/runthis-client-${CLIENT_VERSION}.min.js
wget -O sha256-${CLIENT_VERSION}.txt https://github.com/regro/runthis-client/releases/download/${CLIENT_VERSION}/sha256.txt
