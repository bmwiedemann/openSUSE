#!/bin/bash

# This file contains a file list mapping of GPG key file paths to well-known names
# It installs symlinks relative to a specific parent directory

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
RPMGPGKEYS["openSUSE"]="gpg-pubkey-3dbdc284-53674dd4.asc"
RPMGPGKEYS["openSUSE-2022"]="gpg-pubkey-29b700a4-62b07e22.asc"
RPMGPGKEYS["openSUSE-Backports"]="gpg-pubkey-65176565-61a0ee8f.asc"
RPMGPGKEYS["SuSE-SLE-15"]="gpg-pubkey-39db7c82-5847eb1f.asc"
RPMGPGKEYS["SuSE-SLE-15.3"]="gpg-pubkey-39db7c82-5847eb1f.asc"
RPMGPGKEYS["SuSE-SLE-15.4"]="gpg-pubkey-39db7c82-5847eb1f.asc"
RPMGPGKEYS["SuSE-SLE-15.5"]="gpg-pubkey-39db7c82-5847eb1f.asc"

# Create the target directories
mkdir -p ${ROOTDIR}${RPMGPGKEYDIR}

# Set up symlinks for GPG keys
for RPMGPGKEY in "${!RPMGPGKEYS[@]}"; do
   ln -sfr "${ROOTDIR}${BUILDKEYDIR}/${RPMGPGKEYS[${RPMGPGKEY}]}" "${ROOTDIR}${RPMGPGKEYDIR}/RPM-GPG-KEY-${RPMGPGKEY}"
done
