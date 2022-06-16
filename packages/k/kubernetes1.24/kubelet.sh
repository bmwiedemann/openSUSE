#!/bin/sh
# Loader Script for Multi-Version Kubelet arrangement introduced to openSUSE in March 2020
source /etc/sysconfig/kubelet

if [ -z "$KUBELET_VER" ]      
then
   echo "ERROR: KUBELET_VER= not defined in /etc/sysconfig/kubelet"
   exit 1
else
   /usr/bin/kubelet$KUBELET_VER "$@"
fi

