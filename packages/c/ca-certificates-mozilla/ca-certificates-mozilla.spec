#
# spec file for package ca-certificates-mozilla
#
# Copyright (c) 2024 SUSE LLC
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


# ensure p11-kit has the required features on SLE for
# https://bugzilla.suse.com/show_bug.cgi?id=1154871
%if 0%{?suse_version} == 1500
%if 0%{?is_opensuse}
# Leap 15.1
%define p11_kit_min 0.23.2-lp151.4.3.1
%else
# 15GA
%define p11_kit_min 0.23.2-4.5.2
%endif
%else
%if 0%{?suse_version} == 1315 && 0%{?sle_version} > 120300
# 12SP3
%define p11_kit_min 0.20.7-3.3.1
%endif
%endif
#
%define certdir %{trustdir_static}
Name:           ca-certificates-mozilla
# Version number is NSS_BUILTINS_LIBRARY_VERSION in this file:
# http://hg.mozilla.org/projects/nss/file/default/lib/ckfw/builtins/nssckbi.h
Version:        2.68
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
Source:         https://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/certdata.txt
Source1:        https://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/nssckbi.h
#Source10:       https://src.fedoraproject.org/rpms/ca-certificates/raw/master/f/certdata2pem.py
Source10:       certdata2pem.py
Source11:       %{name}.COPYING
Source12:       compareoldnew
BuildRequires:  ca-certificates
BuildRequires:  openssl
BuildRequires:  p11-kit-devel
BuildRequires:  python3-base
# for update-ca-certificates
Requires(post): ca-certificates
Requires(postun):ca-certificates
#
# replaces this package from SLE11 times
Obsoletes:      openssl-certs < %version
BuildArch:      noarch
%if %{defined p11_kit_min}
Conflicts:      p11-kit-tools < %p11_kit_min
%endif

%description
This package contains some CA root certificates for OpenSSL extracted
from MozillaFirefox

%prep
%setup -qcT

mkdir certs
cp %{SOURCE0} certs

install -m 644 %{SOURCE11} COPYING
ver=`sed -ne '/NSS_BUILTINS_LIBRARY_VERSION /s/.*"\(.*\)"/\1/p' < "%{SOURCE1}"`
if [ "%{version}" != "$ver" ]; then
	echo "*** Version number mismatch: spec file should be version $ver"
	false
fi

%build
export LANG=en_US.UTF-8
cd certs
python3 %{SOURCE10}
cd ..
(
  cat <<-EOF
	# This is a bundle of X.509 certificates of public Certificate
	# Authorities.  It was generated from the Mozilla root CA list.
	# These certificates and trust/distrust attributes use the file format accepted
	# by the p11-kit-trust module.
	#
	# Source: nss/lib/ckfw/builtins/certdata.txt
	# Source: nss/lib/ckfw/builtins/nssckbi.h
	#
	# Generated from:
	EOF
   awk '$2 = "NSS_BUILTINS_LIBRARY_VERSION" {print "# " $2 " " $3}';
   echo '#';
   ls -1 certs/*.tmp-p11-kit | sort | xargs cat
) > %{name}.trust.p11-kit

%install
mkdir -p %{buildroot}/%{trustdir_static}
install -m 644 %{name}.trust.p11-kit "%{buildroot}/%{trustdir_static}/%{name}.trust.p11-kit"

%post
update-ca-certificates || true

%postun
update-ca-certificates || true

%posttrans
update-ca-certificates || true

%files
%license COPYING
%{trustdir_static}

%changelog
