#
# spec file for package xosd
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


%define libname libxosd2
Name:           xosd
Version:        2.2.14
Release:        0
Summary:        X On-Screen Display library
License:        GPL-2.0-or-later
URL:            https://sourceforge.net/projects/libxosd
Source:         http://sourceforge.net/projects/libxosd/files/libxosd/xosd-%{version}/%{name}-%{version}.tar.gz
Patch0:         xosd.patch
Patch1:         xosd-2.2.14-config.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)

%description
A tool for displaying a TV-like on-screen display in X

%package -n %{libname}
Summary:        Library for X On-Screen Display
Group:          System/Libraries
Conflicts:      xosd < %{version}-%{release}

%description -n %{libname}
A library for displaying a TV-like on-screen display in X

%package devel
Summary:        X On-Screen Display library development files
Group:          Development/Libraries/X11
Requires:       xosd = %{version}

%description devel
Development headers and libraries for xosd package

%prep
%autosetup -p1

%build
%configure \
  --disable-silent-rules \
  --disable-gtktest \
  --disable-gdk_pixbuftest \
  --disable-beep_media_player_plugin \
  --disable-static \
  --disable-new-plugin \
  --disable-old-plugin \
  --enable-xinerama
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_mandir}/man1/osd_cat.1%{?ext_man}
%license COPYING
%doc AUTHORS ChangeLog README
%{_datadir}/%{name}
%{_bindir}/osd_cat

%files -n %{libname}
%{_libdir}/libxosd.so.*

%files devel
%{_mandir}/man3/xosd*3%{?ext_man}
%{_libdir}/libxosd.so
%{_includedir}/xosd.h
%{_bindir}/xosd-config
%{_datadir}/aclocal/libxosd.m4
%{_mandir}/man1/xosd-config.1%{?ext_man}

%changelog
