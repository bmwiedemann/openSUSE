#!/bin/sh
PY_BIN="/usr/bin/python3"
ANSIBLE_CMDB="/usr/lib/ansiblecmdb/ansible-cmdb.py"
$PY_BIN $ANSIBLE_CMDB "$@"
