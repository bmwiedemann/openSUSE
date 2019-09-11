#
# spec file for package libsmpp34
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
Name:           libsmpp34
Version:        1.13.0
Release:        0
Summary:        PDU SMPP packaging and unpackaging tool
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://osmocom.org/projects/libsmpp34
Source:         %name-%version.tar.xz
BuildRequires:  autoconf >= 2.57
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.20
BuildRequires:  pkgconfig(libxml-2.0)

%description
The library provides the PDU handling of the SMPP-3.4 protocol.

%package -n libsmpp34-%sover
Summary:        SMPP-3.4 protocol library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libsmpp34-%sover
This library provides the Protocol Data Unit (PDU) handling of the
SMPP-3.4 protocol. SMPP (Short Message Peer-to-Peer) is a protocol
providing a data communication interface for the transfer of short
message data between External Short Messaging Entities, Routing
Entitites and Message Centres.

%package devel
Summary:        Development files for the SMPP-3.4 protocol library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsmpp34-%sover = %version
# Wrong package name
Obsoletes:      libsmpp34-0-devel <= %version-%release
Provides:       libsmpp34-0-devel = %version-%release

%description devel
The library provides the PDU handling of the SMPP-3.4 protocol.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmpp34.

%prep
%setup -q

%build
echo "%version" >.tarball-version
autoreconf -fi
%configure --disable-static --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%post   -n libsmpp34-%sover -p /sbin/ldconfig
%postun -n libsmpp34-%sover -p /sbin/ldconfig

%files -n libsmpp34-%sover
%_libdir/libsmpp34.so.%{sover}*

%files devel
%license COPYING
%doc ChangeLog
%_includedir/%name/
%_libdir/libsmpp34.so
%_libdir/pkgconfig/*.pc

%changelog
