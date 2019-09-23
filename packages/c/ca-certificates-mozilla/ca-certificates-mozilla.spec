#
# spec file for package ca-certificates-mozilla
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define certdir %{trustdir_static}
Name:           ca-certificates-mozilla
# Version number is NSS_BUILTINS_LIBRARY_VERSION in this file:
# http://hg.mozilla.org/projects/nss/file/default/lib/ckfw/builtins/nssckbi.h
Version:        2.34
Release:        0
Summary:        CA certificates for OpenSSL
License:        MPL-2.0
Group:          Productivity/Networking/Security
URL:            https://www.mozilla.org
# IMPORTANT: procedure to update certificates:
# - Check the log of the cert file:
#   http://hg.mozilla.org/projects/nss/log/default/lib/ckfw/builtins/certdata.txt
# - download the new certdata.txt
#   wget -O certdata.txt "http://hg.mozilla.org/projects/nss/file/default/lib/ckfw/builtins/certdata.txt"
# - run compareoldnew to show fingerprints of new and changed certificates
# - check the bugs referenced in hg log and compare the checksum
#   to output of compareoldnew
# - Watch out that blacklisted or untrusted certificates are not
#   accidentally included!
Source:         http://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/certdata.txt
Source1:        http://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/nssckbi.h
# from Fedora. Note: currently contains extra fix to remove quotes. Pending upstream approval.
Source10:       certdata2pem.py
Source11:       %{name}.COPYING
Source12:       compareoldnew
BuildRequires:  ca-certificates
BuildRequires:  openssl
BuildRequires:  p11-kit-devel
BuildRequires:  python3-base
# for update-ca-certificates
Requires(post): ca-certificates
Requires(postun): ca-certificates
#
# replaces this package from SLE11 times
Obsoletes:      openssl-certs
BuildArch:      noarch

%description
This package contains some CA root certificates for OpenSSL extracted
from MozillaFirefox

%prep
%setup -qcT

/bin/cp %{SOURCE0} .

install -m 644 %{SOURCE11} COPYING
ver=`sed -ne '/NSS_BUILTINS_LIBRARY_VERSION /s/.*"\(.*\)"/\1/p' < "%{SOURCE1}"`
if [ "%{version}" != "$ver" ]; then
	echo "*** Version number mismatch: spec file should be version $ver"
	false
fi

%build
export LANG=en_US.UTF-8
python3 %{SOURCE10}

%install
mkdir -p %{buildroot}/%{trustdir_static}/anchors
set +x
for i in *.crt; do
	args=()
	trust=`sed -n '/^# openssl-trust=/{s/^.*=//;p;q;}' "$i"`
	distrust=`sed -n '/^# openssl-distrust=/{s/^.*=//;p;q;}' "$i"`
	alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' "$i"`
	args+=('-trustout')
	for t in $trust; do
		args+=("-addtrust" "$t")
	done
	for t in $distrust; do
		args+=("-addreject" "$t")
	done
	[ -z "$alias" ] || args+=('-setalias' "$alias")

	echo "$i ${args[*]}"
	fname="%{buildroot}/%{trustdir_static}$d/${i%%:*}.pem"
	if [ -e "$fname" ]; then
		fname="${fname%.pem}"
		j=1
		while [ -e "$fname.$j.pem" ]; do
			j=$((j+1))
		done
		fname="$fname.$j.pem"
	fi
	{
		grep '^#' "$i"
		openssl x509 -in "$i" "${args[@]}"
	} > "$fname"
done
for i in *.p11-kit ; do
	install -m 644 "$i" "%{buildroot}/%{trustdir_static}"
done
set -x

%post
update-ca-certificates || true

%postun
update-ca-certificates || true

%files
%license COPYING
%{trustdir_static}

%changelog
