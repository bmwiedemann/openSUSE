#
# spec file for package libqt5-qtx11extras
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


%define qt5_snapshot 0
%define libname libQt5X11Extras5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtx11extras-everywhere-src-5.15.1
Name:           libqt5-qtx11extras
Version:        5.15.1
Release:        0
Summary:        Qt 5 X11 Extras Addon
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libQt5PlatformHeaders-devel >= %{version}
BuildRequires:  xz
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt X11 Extras enables the Qt programmer to write applications for the
Linux/X11 platform. (Applications developed with Qt can also be
deployed across several other desktop and embedded operating systems
without having to rewrite the source code.)

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 X11 Extras Addon
Group:          Development/Libraries/X11
%requires_ge    libQt5Gui5

%description -n %{libname}
Qt X11 Extras enables the Qt programmer to write applications for the
Linux/X11 platform. (Applications developed with Qt can also be
deployed across several other desktop and embedded operating systems
without having to rewrite the source code.)

%package devel
Summary:        Development files for the Qt5 X11 Extras library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Provides:       libQt5X11Extras-devel = %{version}
Obsoletes:      libQt5X11Extras-devel < %{version}

%description devel
You need this package if you want to compile programs with qtx11extras.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5X11Extras.so.*

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtX11Extras
%{_libqt5_libdir}/cmake/Qt5X11Extras
%{_libqt5_libdir}/libQt5X11Extras.prl
%{_libqt5_libdir}/libQt5X11Extras.so
%{_libqt5_libdir}/pkgconfig/Qt5X11Extras.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_x11extras*.pri

%changelog
