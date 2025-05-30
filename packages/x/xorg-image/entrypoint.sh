#!/bin/bash

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')] $@"
}

log "Starting X11 entrypoint script"

# Trap signals for graceful shutdown
trap 'log "Received SIGTERM, initiating shutdown"; cleanup' SIGTERM
trap 'log "Received SIGINT, initiating shutdown"; cleanup' SIGINT

# Cleanup function to stop all relevant processes
cleanup() {
    log "Cleaning up and stopping processes"

    pkill -TERM -f "/usr/bin/Xorg" || true
    pkill -TERM -f icewm-session-lite || true
    pkill -TERM -f icewmbg || true
    pkill -TERM -f icewm || true

    sleep 3

    # Force kill if needed
    pkill -KILL -f "/usr/bin/Xorg" || true
    pkill -KILL -f icewm || true

    log "Cleanup complete, exiting"
    exit 0
}

# Set default DISPLAY if not set
if [ -z "$DISPLAY" ]; then
    log "DISPLAY variable is not set, defaulting to :0"
    DISPLAY=:0
fi

# Extract display number from DISPLAY variable
DISPLAY_NUM=$(echo $DISPLAY | sed 's/^://')

# Clean up existing X server lock files and sockets
log "Cleaning up existing X server lock files for display $DISPLAY"
rm -f /tmp/.X${DISPLAY_NUM}-lock /tmp/.X11-unix/X${DISPLAY_NUM}

if [ $# -gt 0 ]; then
    log "Executing custom command: $@"
    exec "$@"
else
    # Start X server
    log "Starting X server on display $DISPLAY"
    startx -- "$DISPLAY" &
    X_PID=$!

    # Wait for X server process (Xorg) to finish
    log "X server (startx) running"
    wait $X_PID

    log "X server has exited"
fi
