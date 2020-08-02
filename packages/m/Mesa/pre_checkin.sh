#!/bin/sh

# This script is based on libcdio_spec-prepare.sh (thanks to sbrabec@suse.cz)
# create a -drivers spec for systemd for bootstrapping

ORIG_SPEC=Mesa
EDIT_WARNING="##### WARNING: please do not edit this auto generated spec file. Use the ${ORIG_SPEC}.spec! #####\n"
sed "s/^%define drivers .*$/${EDIT_WARNING}%define drivers 1/;
     s/^Name:.*/&-drivers/
	      " < ${ORIG_SPEC}.spec > ${ORIG_SPEC}-drivers.spec
cp ${ORIG_SPEC}.changes ${ORIG_SPEC}-drivers.changes
cp ${ORIG_SPEC}-rpmlintrc ${ORIG_SPEC}-drivers-rpmlintrc

osc service localrun format_spec_file
