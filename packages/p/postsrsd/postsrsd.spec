#
# spec file for package postsrsd
#
# Copyright (c) 2023 SUSE LLC
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


Name:           postsrsd
Version:        2.0.2
Release:        0
Summary:        Sender Rewriting Support for postfix
License:        GPL-2.0-only
Group:          Productivity/Networking/Email/Servers
URL:            https://github.com/roehling/postsrsd

Source:         https://github.com/roehling/postsrsd/archive/%version.tar.gz
BuildRequires:  cmake >= 3.24
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)

%description
PostSRSd provides the Sender Rewriting Scheme (SRS) via TCP-based
lookup tables for Postfix. SRS is needed if your mail server acts
as forwarder.

%prep
%autosetup -p1

%build
%cmake -DFETCHCONTENT_TRY_FIND_PACKAGE_MODE=ALWAYS \
	-DGENERATE_SRS_SECRET=0 -DCHROOT_DIR=/var/lib/empty \
	-DUSE_APPARMOR=1 -DINIT_FLAVOR=systemd \
	-DWITH_SQLITE=BOOL:ON -DBUILD_TESTING:BOOL=OFF
%make_jobs

%install
%cmake_install
b="%buildroot"
mkdir -p "$b/%_defaultdocdir"
mv "$b/%_datadir/doc/%name" "$b/%_defaultdocdir/"
cp README.rst "$b/%_defaultdocdir/%name/"

%pre
%service_add_pre postsrsd.service

%post
s="%_sysconfdir/postsrsd.secret"
if [ ! -e "$s" ]; then
	echo "No postsrsd secret found in $s, generating one."
	dd if=/dev/urandom of="$s" bs=64 count=1
fi
%service_add_post postsrsd.service

%preun
%service_del_preun postsrsd.service

%postun
%service_del_postun postsrsd.service

%files
%_sbindir/postsrsd
%_unitdir/*
%_docdir/%name/
%license LICENSES/*

%changelog
