#!/bin/sh

set -e

[ -n "$1" ] && UUID="$1"
[ -n "$2" ] && REMOTE_IP="$2"

if [ -n "$UUID" ] && [ "$UUID" != "<UUID>" ] && [ -n "$REMOTE_IP" ] && [ "$REMOTE_IP" != "<REMOTE_IP>" ]; then
    mkdir -p /var/lib/keylime/cv_ca
    mkdir -p /etc/keylime/agent.conf.d
    cat <<EOF > /etc/keylime/agent.conf.d/agent.conf
[agent]
 
uuid = "$UUID"
registrar_ip = "$REMOTE_IP"
revocation_notification_ip = "$REMOTE_IP"
run_as = "root:root"
EOF
fi
