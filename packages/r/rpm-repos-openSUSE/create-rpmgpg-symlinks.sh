#!/bin/bash

# This file contains a file list mapping of GPG key file paths to well-known names
# It installs symlinks relative to a specific parent directory

set -euxo pipefail

ROOTDIR="$1"

if [ -z "$1" ]; then
   ROOTDIR="/"
elif [ ! -d "$1" ]; then
   echo "Not a valid directory path"
   exit 1
fi

RPMGPGKEYDIR="/etc/pki/rpm-gpg"
BUILDKEYDIR="/usr/lib/rpm/gnupg/keys"

declare -A RPMGPGKEYS

# List of GPG keys and common names
RPMGPGKEYS["openSUSE"]="gpg-pubkey-29b700a4-62b07e22.asc"
RPMGPGKEYS["openSUSE-Backports"]="gpg-pubkey-287a0027-682477e3.asc"
RPMGPGKEYS["SuSE-SLE-15"]="gpg-pubkey-39db7c82-66c5d91a.asc"
RPMGPGKEYS["SuSE-SLE-15.3"]="gpg-pubkey-39db7c82-66c5d91a.asc"
RPMGPGKEYS["SuSE-SLE-15.4"]="gpg-pubkey-39db7c82-66c5d91a.asc"
RPMGPGKEYS["SuSE-SLE-15.5"]="gpg-pubkey-39db7c82-66c5d91a.asc"
RPMGPGKEYS["SuSE-SLE-15.6"]="gpg-pubkey-3fa1d6ce-67c856ee.asc"
RPMGPGKEYS["SuSE-SLE-16"]="gpg-pubkey-09d9ea69-68595a8c.asc"

# Create the target directories
mkdir -p ${ROOTDIR}${RPMGPGKEYDIR}

# Set up symlinks for GPG keys
for RPMGPGKEY in "${!RPMGPGKEYS[@]}"; do
    ln -sfr "${ROOTDIR}${BUILDKEYDIR}/${RPMGPGKEYS[${RPMGPGKEY}]}" "${ROOTDIR}${RPMGPGKEYDIR}/RPM-GPG-KEY-${RPMGPGKEY}"
done
