#
# spec file for package kdsoap
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


%define soname 2
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define qt5 1
%define pkg_suffix %{nil}
%define lib_suffix %{soname}
%define mkspecsdir %{_libqt5_archdatadir}/mkspecs
%endif
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
# to have libkdsoap-qt6-2
%define lib_suffix -%{soname}
%define mkspecsdir %{_qt6_mkspecsdir}
%endif
Name:           kdsoap%{pkg_suffix}
Version:        2.1.1
Release:        0
Summary:        A Qt-based client-side and server-side SOAP component
# No "or later" clause, licenses specified explicitly
License:        MIT
Group:          System/Libraries
URL:            https://www.kdab.com/products/kd-soap
Source:         https://github.com/KDAB/KDSoap/releases/download/kdsoap-%{version}/kdsoap-%{version}.tar.gz
BuildRequires:  cmake > 3.12
BuildRequires:  fdupes
BuildRequires:  pkgconfig
%if 0%{?qt5}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
%endif
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
%endif
BuildRequires:  pkgconfig(zlib)

%description
KD Soap is a Qt-based client-side and server-side SOAP component.
It can be used to create client applications for web services and also provides
the means to create web services without the need for any further component such
as a dedicated web server.

%package -n libkdsoap%{pkg_suffix}%{lib_suffix}
Summary:        A Qt-based client-side and server-side SOAP component
Group:          System/Libraries

%description -n libkdsoap%{pkg_suffix}%{lib_suffix}
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides the library for the client-side component.

%package -n libkdsoap-server%{pkg_suffix}%{lib_suffix}
Summary:        A Qt-based client-side and server-side SOAP component
Group:          System/Libraries

%description -n libkdsoap-server%{pkg_suffix}%{lib_suffix}
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides the library for the server-side component.

%package devel
Summary:        Development files for kdsoap, a Qt-based client and server-side SOAP component
Group:          Development/Libraries/C and C++
Requires:       libkdsoap%{pkg_suffix}%{lib_suffix} = %{version}
Requires:       libkdsoap-server%{pkg_suffix}%{lib_suffix} = %{version}
# Headers are not co-installable (yet)
%if 0%{?qt6}
Conflicts:      kdsoap-devel
%endif

%description devel
KD Soap is a Qt-based client-side and server-side SOAP component.
This package provides development headers to use KD Soap in Qt based
applications.

%prep
%autosetup -p1 -n kdsoap-%{version}

%build
%if 0%{?qt5}
%cmake
%cmake_build
%endif
%if 0%{?qt6}
# The two helloworld examples fail to build
%cmake_qt6 -DKDSoap_QT6:BOOL=TRUE -DKDSoap_EXAMPLES:BOOL=FALSE
%qt6_build
%endif

%install
%if 0%{?qt5}
%cmake_install
%endif
%if 0%{?qt6}
%qt6_install
%endif

%if 0%{?qt5}
mkdir -p %{buildroot}%{mkspecsdir}/features
mv %{buildroot}%{_datadir}/mkspecs/features/kdsoap.prf %{buildroot}%{mkspecsdir}/features/
%endif

%fdupes %{buildroot}%{_includedir}/KDSoapClient/

%post -n libkdsoap-server%{pkg_suffix}%{lib_suffix} -p /sbin/ldconfig
%post -n libkdsoap%{pkg_suffix}%{lib_suffix} -p /sbin/ldconfig
%postun -n libkdsoap-server%{pkg_suffix}%{lib_suffix} -p /sbin/ldconfig
%postun -n libkdsoap%{pkg_suffix}%{lib_suffix} -p /sbin/ldconfig

%files -n libkdsoap%{pkg_suffix}%{lib_suffix}
%license LICENSES/MIT.txt
%{_libdir}/libkdsoap%{pkg_suffix}.so.%{soname}*

%files -n libkdsoap-server%{pkg_suffix}%{lib_suffix}
%license LICENSES/MIT.txt
%{_libdir}/libkdsoap-server%{pkg_suffix}.so.%{soname}*

%files devel
%license LICENSES/MIT.txt
%{_bindir}/kdwsdl2cpp%{pkg_suffix}
%{_datadir}/doc/KDSoap%{pkg_suffix}/
%{_includedir}/KDSoapClient/
%{_includedir}/KDSoapServer/
%{_libdir}/cmake/KDSoap%{pkg_suffix}
%{_libdir}/libkdsoap%{pkg_suffix}.so
%{_libdir}/libkdsoap-server%{pkg_suffix}.so
%{mkspecsdir}/modules/qt_KDSoapClient.pri
%{mkspecsdir}/modules/qt_KDSoapServer.pri
%if 0%{?qt5}
%{mkspecsdir}/features/kdsoap.prf
%endif

%changelog
