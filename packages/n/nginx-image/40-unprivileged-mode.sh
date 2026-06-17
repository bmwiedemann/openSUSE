#!/bin/sh

set -e

CURRENT_UID=$(id -u)
if [ "$CURRENT_UID" -gt "0" ]; then
    echo "$0: Running as unprivileged user (UID: $CURRENT_UID). Configuring for unprivileged mode (Port 8080)."

    CONF_FILES="/etc/nginx/conf.d/default.conf /etc/nginx/nginx.conf"

    for FILE in $CONF_FILES; do
        if [ -w "$FILE" ]; then
            if grep -q "listen .*80;" "$FILE"; then
                echo "Changing port 80 to 8080 in $FILE"
                sed 's/listen\s*80;/listen 8080;/g' "$FILE" > /tmp/client_temp/nginx_swap.conf && \
                cat /tmp/client_temp/nginx_swap.conf > "$FILE" && \
                rm -f /tmp/client_temp/nginx_swap.conf
            fi

            if [ "$FILE" = "/etc/nginx/nginx.conf" ]; then
                echo "Redirecting NGINX temp paths and setting PID to /tmp in $FILE"
                sed -e '/^user/d' \
                    -e 's,^#\?\s*pid\s\+.*;$,pid /var/run/nginx/nginx.pid;,' \
                    -e '/http {/a \    client_body_temp_path /tmp/client_temp;\n    proxy_temp_path /tmp/proxy_temp;\n    fastcgi_temp_path /tmp/fastcgi_temp;\n    uwsgi_temp_path /tmp/uwsgi_temp;\n    scgi_temp_path /tmp/scgi_temp;' \
                    "$FILE" > /tmp/client_temp/nginx_ultra.conf && \
                cat /tmp/client_temp/nginx_ultra.conf > "$FILE" && \
                rm -f /tmp/client_temp/nginx_ultra.conf
                echo "$0: Removed 'user' directive and updated PID path."
            fi
        fi
    done

    echo "$0: Listening on port 8080."
fi