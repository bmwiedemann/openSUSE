#!/bin/sh

# This script is based on libcdio_spec-prepare.sh (thanks to sbrabec@suse.cz)
# create a -mini spec for majority of Java packages for bootstrapping
#
#Usage:
# 1.) add these two lines below into the spec file including hash sign (#)
#     behind the Name: tag
#   # This line is not a comment, please do not remove it!
#   #%(sh %{_sourcedir}/jpackage-mini-prepare.sh %{_sourcedir} %{name})
# 2.) you need to define a bootstrap macro with value 0
# 3.) you need to define a real macro with name of package and replace all
#     occurences of %{name} with %{real} to avoid the name problems in -mini package
#
# How it works:
# 1.) Was called by rpmbuild (or Re, or should be invoked manually from command line)
# 2.) Rename the package name to name-mini
# 3.) Redefine the bootstrap macro to 1
# 4.) Add an explicit Provides to real name
# 5.) Copy the .changes to -mini.changes


ORIG_SPEC=${2%-mini}
# Never update -mini file when it is already opened. It will break advanced build scripts:
if [[ "${2}" != "${ORIG_SPEC}" ]]; then
    exit
fi

if [[ ! -f ${1}/${ORIG_SPEC}.spec ]] ; then
    exit
fi

EDIT_WARNING="##### WARNING: please do not edit this auto generated spec file. Use the ${ORIG_SPEC}.spec! #####\n"
sed "s/^%define bootstrap.*$/${EDIT_WARNING}%define bootstrap 1/;
     s/^\(Name:.*\)$/\1-mini/;
     s/^BuildRoot.*/&\n\nProvides:    %{real} = %{version}-%{release}\n/
    " < ${1}/${ORIG_SPEC}.spec > ${1}/${ORIG_SPEC}-mini.spec

cp -a ${1}/${ORIG_SPEC}.changes ${1}/${ORIG_SPEC}-mini.changes
