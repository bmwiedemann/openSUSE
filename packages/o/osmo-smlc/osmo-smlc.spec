#
# spec file for package osmo-smlc
#
# Copyright (c) 2025 SUSE LLC
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


Name:           osmo-smlc
Version:        0.3.1
Release:        0
Summary:        Osmocom Serving Mobile Location Centre
License:        AGPL-3.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/osmo-smlc
#Git-Clone:     https://git.osmocom.org/osmo-smlc/
Source:         https://github.com/osmocom/osmo-smlc/archive/refs/tags/%version.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
BuildRequires:  pkgconfig(libosmo-sigtran) >= 2.0.0
BuildRequires:  pkgconfig(libosmocore) >= 1.10.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.10.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.10.0
BuildRequires:  pkgconfig(libosmovty) >= 1.10.0

%description
OsmoSMLC is the Osmocom Serving Mobile Location Centre. It implements
the SMLC functionality as specified in 3GPP networks
Location_Services architecture.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
%configure \
	--with-systemdsystemunitdir="%_unitdir" \
	--docdir="%_docdir/%name"
%make_build

%install
%make_install
# you should put this in usr
rm -rf "%buildroot/%_sysconfdir"

%check
%make_build check || (find . -name testsuite.log -exec cat {} +)

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%pre
%service_add_pre %name.service

%post
%service_add_post %name.service

%files
%_bindir/osmo*
%_unitdir/*
%doc %_docdir/%name/
%license COPYING
%doc README.md

%changelog
