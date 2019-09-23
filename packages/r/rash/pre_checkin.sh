#!/bin/bash
ORIG_SPEC=rash
EDIT_WARNING="##### WARNING: please do not edit this auto generated spec file. Use the ${ORIG_SPEC}.spec! #####\n"
sed -r "s/^%define bootstrap .*$/${EDIT_WARNING}%define bootstrap 1/
	s/^%define base .*$/${EDIT_WARNING}%define base -base/
	s/^(Name:.*)$/\1-base/ " < ${ORIG_SPEC}.spec > ${ORIG_SPEC}-base.spec
cp ${ORIG_SPEC}.changes   ${ORIG_SPEC}-base.changes
osc service localrun format_spec_file
