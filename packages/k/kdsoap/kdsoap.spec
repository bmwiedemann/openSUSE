#
# spec file for package kdsoap
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

%define soname 1_9_0
%define sonum 1.9.0

Name:           kdsoap
Version:        1.9.0
Release:        0
Summary:        A Qt5-based client-side and server-side SOAP component
# No "or later" clause, licenses specified explicitly
License:        (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only AND AGPL-3.0-only
Group:          System/Libraries
URL:            https://www.kdab.com/products/kd-soap
# Tarball without non-free, unused and not installed unit tests
# See https://github.com/KDAB/KDSoap/issues/207 for more information
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.0.2
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5Network) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5Xml) >= 5.6.0
BuildRequires:  pkgconfig(zlib)

%description
KD Soap is a Qt-based client-side and server-side SOAP component.
It can be used to create client applications for web services and also provides
the means to create web services without the need for any further component such
as a dedicated web server.

%package -n libkdsoap%{soname}
Summary:        A Qt5-based client-side and server-side SOAP component
License:        (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only
Group:          System/Libraries
Recommends:     %{name}

%description -n libkdsoap%{soname}
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides the library for the client-side component.

%package -n libkdsoap-server%{soname}
Summary:        A Qt5-based client-side and server-side SOAP component
License:        AGPL-3.0-only
Group:          System/Libraries

%description -n libkdsoap-server%{soname}
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides the library for the server-side component.

%package devel
Summary:        Development files for kdsoap, a Qt-based client and server-side SOAP component
License:        (GPL-2.0-only OR GPL-3.0-only) OR LGPL-2.1-only AND AGPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       libkdsoap%{soname} = %{version}
Requires:       libkdsoap-server%{soname} = %{version}

%description devel
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides development headers to use KD Soap in Qt based
applications.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_includedir}/KDSoapClient/

%post -n libkdsoap-server%{soname}  -p /sbin/ldconfig
%post -n libkdsoap%{soname}  -p /sbin/ldconfig
%postun -n libkdsoap-server%{soname}  -p /sbin/ldconfig
%postun -n libkdsoap%{soname}  -p /sbin/ldconfig

%files -n libkdsoap%{soname}
%license LICENSE.GPL.txt LICENSE.LGPL.txt LICENSE.txt README.txt
%{_libdir}/libkdsoap.so.%{sonum}

%files -n libkdsoap-server%{soname}
%license LICENSE.AGPL3-modified.txt README.txt
%{_libdir}/libkdsoap-server.so.%{sonum}

%files devel
%license LICENSE* README.txt
%{_bindir}/kdwsdl2cpp
%{_libdir}/libkdsoap.so
%{_libdir}/libkdsoap-server.so
%{_libdir}/cmake/KDSoap
%{_includedir}/KDSoapServer
%{_includedir}/KDSoapClient
%{_datadir}/doc/KDSoap/
%dir %{_datadir}/mkspecs
%dir %{_datadir}/mkspecs/features
%{_datadir}/mkspecs/features/kdsoap.prf

%changelog
