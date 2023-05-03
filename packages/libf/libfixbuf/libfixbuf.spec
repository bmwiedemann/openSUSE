#
# spec file for package libfixbuf
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013-2021, Martin Hauke <mardnh@gmx.de>
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


%define sover 9
Name:           libfixbuf
Version:        2.4.2
Release:        0
Summary:        Implementation of the IPFIX Protocol as a C library
License:        LGPL-3.0-only
Group:          System/Libraries
URL:            https://tools.netsa.cert.org/fixbuf
Source:         https://tools.netsa.cert.org/releases/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig

%description
libfixbuf is a compliant implementation of the IPFIX Protocol, as defined in
RFC 5101. It supports the information model defined in RFC 5102, extended as
proposed by RFC 5103 to support information elements for representing biflows.
libfixbuf supports UDP, TCP, SCTP, TLS over TCP, and Spread as transport
protocols. It also supports operation as an IPFIX File Writer or IPFIX File
Reader.

ipfixDump is a command line tool for printing the contents of an IPFIX
file as text.

%package -n libfixbuf%{sover}
Summary:        Development files for the libfixbuf library
Group:          System/Libraries

%description -n libfixbuf%{sover}
libfixbuf is a compliant implementation of the IPFIX Protocol, as defined in
RFC 5101. It supports the information model defined in RFC 5102, extended as
proposed by RFC 5103 to support information elements for representing biflows.
libfixbuf supports UDP, TCP, SCTP, TLS over TCP, and Spread as transport
protocols.

%package devel
Summary:        Development files for the libfixbuf library
Group:          Development/Libraries/C and C++
Requires:       libfixbuf%{sover} = %{version}

%description devel
libfixbuf aims to be a compliant implementation of the IPFIX Protocol
and message format, from which IPFIX Collecting Processes and
IPFIX Exporting Processes may be built.

This subpackage contains libraries and header files for developing
applications that want to make use of libfixbuf.

%package tools
Summary:        IPFIX file dumper
Group:          Productivity/Networking/Diagnostic

%description tools
libfixbuf is a compliant implementation of the IPFIX Protocol, as defined in
RFC 5101. It supports the information model defined in RFC 5102, extended as
proposed by RFC 5103 to support information elements for representing biflows.
libfixbuf supports UDP, TCP, SCTP, TLS over TCP, and Spread as transport
protocols.

ipfixDump is a command line tool for printing the contents of an IPFIX
file as text.

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
rm %{buildroot}/%{_libdir}/*.{la,a}

%post   -n libfixbuf%{sover} -p /sbin/ldconfig
%postun -n libfixbuf%{sover} -p /sbin/ldconfig

%files -n libfixbuf%{sover}
%license LICENSE.txt
%doc AUTHORS NEWS README
%{_libdir}/libfixbuf.so.%{sover}*

%files devel
%license LICENSE.txt
%dir %{_includedir}/fixbuf
%{_includedir}/fixbuf/*.h
%{_libdir}/libfixbuf.so
%{_libdir}/pkgconfig/libfixbuf.pc

%files tools
%license LICENSE.txt
%{_bindir}/ipfixDump
%{_datadir}/libfixbuf
%{_datadir}/libfixbuf/cert_ipfix.xml
%{_mandir}/man1/ipfixDump.1%{?ext_man}

%changelog
