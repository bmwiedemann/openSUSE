#
# spec file for package kdsoap
#
# Copyright (c) 2021 SUSE LLC
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


%define soname 2

Name:           kdsoap
Version:        2.0.0
Release:        0
Summary:        A Qt-based client-side and server-side SOAP component
# No "or later" clause, licenses specified explicitly
License:        (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only AND AGPL-3.0-only
Group:          System/Libraries
URL:            https://www.kdab.com/products/kd-soap
Source:         https://github.com/KDAB/KDSoap/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.9.0
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(zlib)

%description
KD Soap is a Qt-based client-side and server-side SOAP component.
It can be used to create client applications for web services and also provides
the means to create web services without the need for any further component such
as a dedicated web server.

%package -n libkdsoap%{soname}
Summary:        A Qt-based client-side and server-side SOAP component
License:        (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only
Group:          System/Libraries
Recommends:     %{name}

%description -n libkdsoap%{soname}
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides the library for the client-side component.

%package -n libkdsoap-server%{soname}
Summary:        A Qt-based client-side and server-side SOAP component
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

mkdir -p %{buildroot}%{_libqt5_archdatadir}/mkspecs/features
mv %{buildroot}%{_datadir}/mkspecs/features/kdsoap.prf %{buildroot}%{_libqt5_archdatadir}/mkspecs/features/

%fdupes %{buildroot}%{_includedir}/KDSoapClient/

%post -n libkdsoap-server%{soname}  -p /sbin/ldconfig
%post -n libkdsoap%{soname}  -p /sbin/ldconfig
%postun -n libkdsoap-server%{soname}  -p /sbin/ldconfig
%postun -n libkdsoap%{soname}  -p /sbin/ldconfig

%files -n libkdsoap%{soname}
%license LICENSES/{GPL-2.0-only.txt,GPL-3.0-only.txt,LGPL-2.1-only.txt,LGPL-3.0-only.txt} README.txt
%{_libdir}/libkdsoap.so.%{soname}*

%files -n libkdsoap-server%{soname}
%license LICENSES/LicenseRef-KDAB-KDSoap-AGPL3-Modified.txt README.txt
%{_libdir}/libkdsoap-server.so.%{soname}*

%files devel
%license LICENSES/* README.txt
%{_bindir}/kdwsdl2cpp
%{_libdir}/libkdsoap.so
%{_libdir}/libkdsoap-server.so
%{_libdir}/cmake/KDSoap
%{_includedir}/KDSoapServer
%{_includedir}/KDSoapClient
%{_datadir}/doc/KDSoap/
%{_libqt5_archdatadir}/mkspecs/features/kdsoap.prf
%{_libqt5_archdatadir}/mkspecs/modules/qt_KDSoapClient.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_KDSoapServer.pri

%changelog
