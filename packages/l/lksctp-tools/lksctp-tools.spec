#
# spec file for package lksctp-tools
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


Name:           lksctp-tools
Version:        1.0.19
Release:        0
Summary:        Utilities for SCTP (Stream Control Transmission Protocol)
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            http://lksctp.sourceforge.net
#Git-Clone:     https://github.com/sctp/lksctp-tools
Source:         https://github.com/sctp/lksctp-tools/archive/refs/tags/v%version.tar.gz
BuildRequires:  libtool

%description
This package contains the SCTP base runtime library and command line
tools.

SCTP (Stream Control Transmission Protocol) is a message-oriented,
reliable transport protocol with congestion control, support for
transparent multihoming, and multiple ordered streams of messages.

%package devel
Summary:        Development files for SCTP (Stream Control Transmission Protocol)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       glibc-devel

%description devel
This package contains the SCTP development libraries and C header
files.

SCTP (Stream Control Transmission Protocol) is a message oriented,
reliable transport protocol, with congestion control, support for
transparent multi-homing, and multiple ordered streams of messages.

%prep
%setup -q

%build
autoreconf -fi
%configure --prefix=%{_prefix} \
	--enable-shared \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.lib
%doc AUTHORS ChangeLog
%doc doc/*.txt
%{_bindir}/*
%{_libdir}/libsctp.so.*
%dir %{_libdir}/lksctp-tools
%{_libdir}/lksctp-tools/*.so.*
%{_mandir}/man7/*

%files devel
%{_includedir}/netinet/sctp.h
%{_libdir}/pkgconfig/libsctp.pc
%{_libdir}/libsctp.so
%dir %{_libdir}/lksctp-tools
%{_libdir}/lksctp-tools/*.so
%dir %{_datadir}/lksctp-tools
%{_datadir}/lksctp-tools/*
%{_mandir}/man3/*

%changelog
