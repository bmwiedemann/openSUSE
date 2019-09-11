#
# spec file for package libdbusmenu-qt
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libdbusmenu-qt
Version:        0.9.2+14.04.20131209
Release:        0
Url:            https://launchpad.net/libdbusmenu-qt/
Summary:        A Qt implementation of the DBusMenu protocol
License:        LGPL-2.0+
Group:          System/Libraries
Source0:        http://archive.ubuntu.com/ubuntu/pool/main/libd/%{name}/%{name}_%{version}.orig.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM noqDebug-qWarnings.patch -- libdbusmenu uses it's own qDebug's and qWarnings,
# which are useless, and annoy users, so this patch just disables them in release mode
Patch1:         noqDebug-qWarnings.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libqjson-devel
BuildRequires:  libqt4-devel
BuildRequires:  pkg-config
Provides:       dbusmenu-qt = 0.3.3
Obsoletes:      dbusmenu-qt < 0.3.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package devel
Summary:        Development package for libdbusmenu-qt
Group:          Development/Libraries/Other
Requires:       libdbusmenu-qt2 = %{version}
Provides:       dbusmenu-qt-devel = 0.3.3
Obsoletes:      dbusmenu-qt-devel < 0.3.3

%description devel
This package contains development files for libdbusmenu-qt.

%package -n libdbusmenu-qt2
Summary:        Development package for dbusmenu-qt
Group:          System/Libraries
%requires_ge    libqt4-x11

%description -n libdbusmenu-qt2
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%prep
%setup -q
%patch1 -p1

# Remove build time references so build-compare can do its work
sed -i "s/HTML_TIMESTAMP         = YES/HTML_TIMESTAMP         = NO/" Doxyfile.in

%build
mkdir build
cd build
export CFLAGS="%{optflags} -DQT_NO_DEBUG -DQT_NO_DEBUG_OUTPUT -DQT_NO_WARNING_OUTPUT"
export CXXFLAGS="%{optflags} -DQT_NO_DEBUG -DQT_NO_DEBUG_OUTPUT -DQT_NO_WARNING_OUTPUT"
export LDFLAGS="-Wl,-Bsymbolic-functions $LDFLAGS"
_libsuffix=$(echo %{_lib} | cut -b4-)
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DLIB_SUFFIX="$_libsuffix" \
      -DUSE_QT5=OFF \
      -DCMAKE_BUILD_TYPE=release ..
make %{?_smp_mflags} VERBOSE=1
cd ..

%install
%makeinstall -C build

# Install the documentation in the correct location
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
mv %{buildroot}%{_datadir}/doc/libdbusmenu-qt-doc/ %{buildroot}%{_docdir}/%{name}-devel/html/
# Install additional documentation
install -pm 0644 COPYING NEWS README %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}

%post -n libdbusmenu-qt2 -p /sbin/ldconfig

%postun -n libdbusmenu-qt2 -p /sbin/ldconfig

%files -n libdbusmenu-qt2
%defattr(-,root,root,-)
%{_libdir}/libdbusmenu-qt.so.2*

%files devel
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-devel/
%{_libdir}/libdbusmenu-qt.so
%{_includedir}/dbusmenu-qt/
%{_libdir}/pkgconfig/dbusmenu-qt.pc
%{_libdir}/cmake/dbusmenu-qt/

%changelog
