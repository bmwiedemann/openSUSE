#!/bin/sh

cd /usr/share/java && exec /usr/bin/java -jar JAP.jar \
        -Djava.net.preferIPv4Stack=true \
        -XX:-UsePerfData \
        --hideUpdate --noSystemErrorLog
