#!/bin/bash

CMD=$1
NOHUP=${NOHUP:=$(which nohup)}

# resolve links - $0 may be a softlink
ZBXJAVAGWCTL="$0"

while [ -h "$ZBXJAVAGWCTL" ]; do
  ls=$(ls -ld "$ZBXJAVAGWCTL")
  link=$(expr "$ls" : '.*-> \(.*\)$')
  if expr "$link" : '/.*' > /dev/null; then
    ZBXJAVAGWCTL="$link"
  else
    ZBXJAVAGWCTL=$(dirname "$ZBXJAVAGWCTL")/"$link"
  fi
done

SERVICE_NAME="zabbix-java-gateway"
JAVA=${JAVA:-java}
JAVA_OPTIONS="-server"
JAVA_OPTIONS="$JAVA_OPTIONS -Dlogback.configurationFile=/etc/zabbix/zabbix-java-gateway-log.xml"
ZABBIX_OPTIONS=${ZABBIX_OPTIONS:=}
ZABBIX_JAVA_DIR=${ZABBIX_JAVA_DIR:=$(dirname "$ZBXJAVAGWCTL")}
ZABBIX_JAVA_CONF=${ZABBIX_JAVA_CONF:=/etc/zabbix/zabbix-java-gateway.conf}
ZABBIX_JAVA_GW_PID=${ZABBIX_JAVA_GW_PID:=/run/zabbixs/zabbix-java-gateway.pid}
ZABBIX_JAVA_GW_LOGFILE=${ZABBIX_JAVA_GW_LOGFILE:=/var/log/zabbixs/zabbix-java-gateway.log}
# source configuration...
. ${ZABBIX_JAVA_CONF}

# Build classpath
CLASSPATH=$(echo $(find /usr/lib/zabbix-java-gateway/ -name "*jar" -type f -print)|sed -e 's/ /:/g')
if [ -n "$PID_FILE" ]; then
	ZABBIX_OPTIONS="$ZABBIX_OPTIONS -Dzabbix.pidFile=$PID_FILE"
fi
if [ -n "$LISTEN_IP" ]; then
	ZABBIX_OPTIONS="$ZABBIX_OPTIONS -Dzabbix.listenIP=$LISTEN_IP"
fi
if [ -n "$LISTEN_PORT" ]; then
	ZABBIX_OPTIONS="$ZABBIX_OPTIONS -Dzabbix.listenPort=$LISTEN_PORT"
fi
if [ -n "$START_POLLERS" ]; then
	ZABBIX_OPTIONS="$ZABBIX_OPTIONS -Dzabbix.startPollers=$START_POLLERS"
fi

COMMAND_LINE="$JAVA $JAVA_OPTIONS -classpath $CLASSPATH $ZABBIX_OPTIONS com.zabbix.gateway.JavaGateway"

start() {
    status
    if [ $? -ne 0 ]; then
        echo "Starting ${SERVICE_NAME} ..."
        cd "$ZBXJAVAGWCTL_DIR"
        (/bin/bash -c "$COMMAND_LINE > /dev/null 2>&1 & echo \$!") > ${ZABBIX_JAVA_GW_PID}
    fi
}

run() {
    echo "Running ${SERVICE_NAME} ..."
    cd "$ZBXJAVAGWCTL_DIR"
    exec $COMMAND_LINE
}

stop() {
    pid=$(cat ${ZABBIX_JAVA_GW_PID})
    echo "Stopping ${SERVICE_NAME} ($pid) ..."
    if kill $pid; then
        rm ${ZABBIX_JAVA_GW_PID}
    fi
}

restart() {
    echo "Restarting ${SERVICE_NAME} ..."
    stop
    start
}

status() {
    pid=$(get_pid)
    if [ ! -z $pid ]; then
        if pid_running $pid; then
            echo "${SERVICE_NAME} running as pid $pid"
            return 0
        else
            echo "Stale pid file with $pid - removing..."
            rm ${ZABBIX_JAVA_GW_PID}
            return 1
        fi
    fi

    echo "${SERVICE_NAME} not running"
    return 3
}

get_pid() {
    cat ${ZABBIX_JAVA_GW_PID} 2> /dev/null
}

pid_running() {
    kill -0 $1 2> /dev/null
}

case "$CMD" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
    run)
        run
        ;;
    *)
        echo "Usage $0 {start|stop|restart|status}"
        RETVAL=1
esac
