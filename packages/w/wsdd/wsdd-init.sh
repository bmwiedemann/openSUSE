#!/bin/sh

umask 0644

WSDD_CONFIG=/etc/sysconfig/wsdd
if test -r "${WSDD_CONFIG}"; then
  . "${WSDD_CONFIG}"
fi

if [ "${WSDD_DOMAIN}" != "" ]; then
  WSDD_DOMAIN="-d \"${WSDD_DOMAIN}\""
elif [ "${WSDD_WORKGROUP}" != "" ]; then
  WSDD_DOMAIN="-w \"${WSDD_WORKGROUP}\""
fi

if [ "${WSDD_HOSTNAME}" != "" ]; then
  WSDD_HOSTNAME="-n \"${WSDD_HOSTNAME}\""
fi

WSDD_INTERFACE_ARGS=""
if [ "${WSDD_INTERFACES}" != "" ]; then
  for intf in ${WSDD_INTERFACES}; do
    WSDD_INTERFACE_ARGS="${WSDD_INTERFACE_ARGS} -i \"${intf}\""
  done
fi

echo "WSDD_ARGS=${WSDD_HOSTNAME} ${WSDD_DOMAIN} ${WSDD_INTERFACE_ARGS} \
	${WSDD_ARGS}" >/run/wsdd/env-vars
