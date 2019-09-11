#
# spec file for package libcroco
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libcroco
Version:        0.6.13
Release:        0
Summary:        CSS2 Parser Library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://gitlab.gnome.org/GNOME/libcroco
Source:         https://download.gnome.org/sources/libcroco/0.6/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

# PATCH-FIX-UPSTREAM libcroco-CVE-2017-8834.patch boo#1043898 boo#1043899 mgorse@suse.com -- fix infinite loop on invalid UTF-8.
Patch0:         libcroco-CVE-2017-8834.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.23

%description
Libcroco is a stand-alone CSS2 parsing library. It provides a low-level
event-driven SAC-like API and a CSS object model-like API.

%package 0_6-3
Summary:        CSS2 Parser Library
# bug437293
Group:          System/Libraries
%ifarch ppc64
Obsoletes:      libcroco-64bit
%endif

%description 0_6-3
Libcroco is a stand-alone CSS2 parsing library. It provides a low-level
event-driven SAC-like API and a CSS object model-like API.

%package devel
Summary:        CSS2 Parser Library Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Libcroco is a stand-alone CSS2 parsing library. It provides a low-level
event-driven SAC-like API and a CSS object model like API.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post 0_6-3 -p /sbin/ldconfig
%postun 0_6-3 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%{_bindir}/csslint-0.6

%files 0_6-3
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/libcroco/
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
