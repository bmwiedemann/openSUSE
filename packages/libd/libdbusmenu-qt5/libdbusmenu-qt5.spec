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
Group:          System/Libraries
Source:         https://github.com/unity8-team/%{rname}/archive/%{version}-0ubuntu1.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM noqDebug-qWarnings.patch -- libdbusmenu uses it's own qDebug's and qWarnings,
# which are useless, and annoy users, so this patch just disables them in release mode
Patch1:         noqDebug-qWarnings.patch
# PATCH-FIX-UPSTREAM full_include_dir.patch -- CMake 2.8.12 creates a fatal error on relative include dirs for a target. silence that policy
Patch2:         full_include_dir.patch
#Needed for DISABLE_FIND_PACKAGE
BuildRequires:  cmake >= 2.8.6
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus. Qt5 library

%package -n libdbusmenu-qt5-2
Summary:        Development package for dbusmenu-qt5
Group:          System/Libraries

%description -n libdbusmenu-qt5-2
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus. Qt5 library

%package -n libdbusmenu-qt5-devel
Summary:        Development package for libdbusmenu-qt5
Group:          Development/Libraries/Other
Requires:       libdbusmenu-qt5-2 = %{version}
Requires:       pkgconfig(Qt5Core)

%description -n libdbusmenu-qt5-devel
This package contains development files for libdbusmenu-qt5.

%prep
%setup -q -n %{rname}-%{version_}-0ubuntu1
%patch1 -p1
%if 0%{?suse_version} <= 1310
%patch2 -p1
%endif

# Remove build time references so build-compare can do its work
sed -i "s/HTML_TIMESTAMP         = YES/HTML_TIMESTAMP         = NO/" Doxyfile.in

%build
mkdir build
pushd build
export CFLAGS="%{optflags} -DQT_NO_DEBUG -DQT_NO_DEBUG_OUTPUT -DQT_NO_WARNING_OUTPUT"
export CXXFLAGS="%{optflags} -DQT_NO_DEBUG -DQT_NO_DEBUG_OUTPUT -DQT_NO_WARNING_OUTPUT"
export LDFLAGS="-Wl,-Bsymbolic-functions $LDFLAGS"
_libsuffix=$(echo %{_lib} | cut -b4-)
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DLIB_SUFFIX="$_libsuffix" \
      -DUSE_QT5=ON \
      -DCMAKE_DISABLE_FIND_PACKAGE_QJSON=TRUE \
      -DCMAKE_BUILD_TYPE=release ..
make %{?_smp_mflags} VERBOSE=1
popd

%install
%makeinstall -C build

# Install the documentation in the correct location
mkdir -p %{buildroot}%{_docdir}/libdbusmenu-qt5-devel
mv %{buildroot}%{_datadir}/doc/libdbusmenu-qt5-doc/ %{buildroot}%{_docdir}/libdbusmenu-qt5-devel/html/
# Install additional documentation
install -pm 0644 COPYING NEWS README %{buildroot}%{_docdir}/libdbusmenu-qt5-devel/

%fdupes -s %{buildroot}%{_docdir}/libdbusmenu-qt5-devel/

%post -n libdbusmenu-qt5-2 -p /sbin/ldconfig

%postun -n libdbusmenu-qt5-2 -p /sbin/ldconfig

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
