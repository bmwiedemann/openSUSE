#!/bin/sh

NAME=NetworkManager

if ! test -f ${NAME}-branding.spec.in ; then
    exit
fi

for variant in openSUSE SLE ; do
    cp ${NAME}-branding.spec.in ${NAME}-branding-${variant}.spec
    cp ${NAME}-branding.changes.in ${NAME}-branding-${variant}.changes
    sed -i "s/%{branding_name}/${variant}/g" ${NAME}-branding-${variant}.spec
    sed -i "s/\(%define *build_${variant} *\)0/\11/" ${NAME}-branding-${variant}.spec
    sed -i "
    /^Name: *${NAME}-branding-${variant}/i \
# Do not edit this auto generated file! Edit ${NAME}-branding.spec.in.
" ${NAME}-branding-${variant}.spec
done
