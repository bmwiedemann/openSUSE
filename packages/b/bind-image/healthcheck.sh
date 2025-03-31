#!/bin/bash

set -euo pipefail

dig @127.0.0.1 +short suse.com A|grep -E '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'
