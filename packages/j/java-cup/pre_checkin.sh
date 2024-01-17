#!/bin/bash

NAME1=java-cup
NAME2=java-cup-bootstrap
COPY_CHANGES=true

EDIT_WARNING="##### WARNING: please do not edit this auto generated spec file. Use the ${NAME1}.spec! #####\n"
sed "s/^%global _without_bootstrap.*$/${EDIT_WARNING}%global with_bootstrap 1/;
     s/^\(Name:.*\)$/\1-bootstrap/;
    " < ${NAME1}.spec > ${NAME2:-${NAME1}-bootstrap}.spec

if ${COPY_CHANGES}; then
    cp ${NAME1}.changes ${NAME2:-${NAME1}-bootstrap}.changes
fi
