#
# spec file for package libdbusmenu-qt5
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


%define rname libdbusmenu-qt
%define version_ %(echo %{version} | sed -e "s/+/-/")

Name:           libdbusmenu-qt5
Version:        0.9.3+16.04.20160218
Release:        0
URL:            https://launchpad.net/libdbusmenu-qt/
Summary:        A Qt implementation of the DBusMenu protocol
License:        LGPL-2.0-or-later
Source0:        https://github.com/unity8-team/%{rname}/archive/%{version}-0ubuntu1.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM noqDebug-qWarnings.patch -- libdbusmenu uses it's own qDebug's and qWarnings,
# which are useless, and annoy users, so this patch just disables them in release mode
Patch0:         noqDebug-qWarnings.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Fix-build-with-CMake-4.patch
#Needed for DISABLE_FIND_PACKAGE
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus. Qt5 library

%package -n libdbusmenu-qt5-2
Summary:        Development package for dbusmenu-qt5

%description -n libdbusmenu-qt5-2
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus. Qt5 library

%package -n libdbusmenu-qt5-devel
Summary:        Development package for libdbusmenu-qt5
Requires:       libdbusmenu-qt5-2 = %{version}
Requires:       pkgconfig(Qt5Core)

%description -n libdbusmenu-qt5-devel
This package contains development files for libdbusmenu-qt5.

%prep
%autosetup -p1 -n %{rname}-%{version_}-0ubuntu1

# Remove build time references so build-compare can do its work
sed -i "s/HTML_TIMESTAMP         = YES/HTML_TIMESTAMP         = NO/" Doxyfile.in

%build
_libsuffix=$(echo %{_lib} | cut -b4-)
%cmake \
  -DLIB_SUFFIX="$_libsuffix" \
  -DUSE_QT5=ON \
  -DCMAKE_DISABLE_FIND_PACKAGE_QJSON=TRUE \
  -DCMAKE_BUILD_TYPE=release
%cmake_build

%install
%cmake_install

# Install the documentation in the correct location
mkdir -p %{buildroot}%{_docdir}/libdbusmenu-qt5-devel
mv %{buildroot}%{_datadir}/doc/libdbusmenu-qt5-doc/ %{buildroot}%{_docdir}/libdbusmenu-qt5-devel/html/
# Install additional documentation
install -pm 0644 COPYING NEWS README %{buildroot}%{_docdir}/libdbusmenu-qt5-devel/

%fdupes %{buildroot}%{_docdir}/libdbusmenu-qt5-devel/

%ldconfig_scriptlets -n libdbusmenu-qt5-2

%files -n libdbusmenu-qt5-2
%defattr(-,root,root,-)
%{_libdir}/libdbusmenu-qt5.so.2*

%files -n libdbusmenu-qt5-devel
%defattr(-,root,root,-)
%doc %{_docdir}/libdbusmenu-qt5-devel/
%{_libdir}/libdbusmenu-qt5.so
%{_includedir}/dbusmenu-qt5/
%{_libdir}/pkgconfig/dbusmenu-qt5.pc
%{_libdir}/cmake/dbusmenu-qt5/

%changelog
