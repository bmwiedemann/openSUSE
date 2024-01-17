#
# spec file for package libe131
#
# Copyright (c) 2020 SUSE LLC
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


%define sover   1
Name:           libe131
Version:        1.4.0
Release:        0
Summary:        A C/C++ library for the E1.31 (sACN) protocol
License:        Apache-2.0
URL:            https://github.com/hhromic/libe131
Source0:        https://github.com/hhromic/libe131/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE libe131-nodoc.patch do not install docs -- aloisio@gmx.com
Patch0:         libe131-nodoc.patch
# PATCH-FIX-UPSTREAM libe131-soversion.patch
Patch1:         libe131-soversion.patch
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
A C/C++ library that provides an API for packet, client and server programming
to be used for communicating with devices implementing the E1.31 (sACN)
protocol.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{name}-%{sover}
Summary:        A C/C++ library for the E1.31 (sACN) protocol

%description -n %{name}-%{sover}
A C/C++ library that provides an API for packet, client and server programming
to be used for communicating with devices implementing the E1.31 (sACN)
protocol.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# creates support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: %{name}
Description: A C/C++ library for the E1.31 (sACN) protocol
Version: %{version}
Libs: -L${libdir} -le131
Cflags: -I${includedir}
EOF

%post -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

%files -n %{name}-%{sover}
%license LICENSE
%{_libdir}/%{name}.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/e131.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
