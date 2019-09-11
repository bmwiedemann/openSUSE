#
# spec file for package libqt5-qtnetworkauth
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define qt5_snapshot 0

%define libname libQt5NetworkAuth5

Name:           libqt5-qtnetworkauth
Version:        5.13.0
Release:        0
Summary:        Qt 5 NetworkAuth Library
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            http://qt.io
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtnetworkauth-everywhere-src-5.13.0
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt Network Authorization provides a set of APIs that enable Qt
applications to obtain limited access to online accounts and HTTP
services without exposing users' passwords. It supports OAuth
versions 1 and 2.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 NetworkAuth Library
Group:          System/Libraries
%requires_ge libQt5Core5

%description -n %libname
Qt Network Authorization provides a set of APIs that enable Qt
applications to obtain limited access to online accounts and HTTP
services without exposing users' passwords. It supports OAuth
versions 1 and 2.

%package devel
Summary:        Development files for the Qt5 NetworkAuth Library
Group:          Development/Libraries/C and C++
Requires:       %libname = %{version}

%description devel
Qt Network Authorization provides a set of APIs that enable Qt
applications to obtain limited access to online accounts and HTTP
services without exposing users' passwords.

This subpackage contains the header files for developing
applications that want to make use of libQt5NetworkAuth5.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 NetworkAuth Library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}

%description private-headers-devel
This package provides private headers of libqt5-qtnetworkauth that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 networkauth examples
Group:          Documentation/Other
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtnetworkauth module.

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %libname
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5NetworkAuth.so.*

%files private-headers-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_includedir}/QtNetworkAuth/%{so_version}

%files devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/QtNetworkAuth/%{so_version}
%{_libqt5_includedir}/QtNetworkAuth/
%{_libqt5_libdir}/cmake/Qt5NetworkAuth/
%{_libqt5_libdir}/libQt5NetworkAuth.prl
%{_libqt5_libdir}/libQt5NetworkAuth.so
%{_libqt5_libdir}/pkgconfig/Qt5NetworkAuth.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
