#!/bin/sh
EDIT_WARNING="##### WARNING: please do not edit this auto generated spec file. Use the xmlbeans.spec! #####\n"
sed "s/^%global bootstrap.*$/${EDIT_WARNING}%global bootstrap 1/;
     s/^\(Name:.*\)$/\1-mini/;
    " < xmlbeans.spec > xmlbeans-mini.spec
rm -f xmlbeans-mini.changes
ln xmlbeans.changes xmlbeans-mini.changes
