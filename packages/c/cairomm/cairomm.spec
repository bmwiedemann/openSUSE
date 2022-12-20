#
# spec file for package cairomm
#
# Copyright (c) 2022 SUSE LLC
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


Name:           cairomm
Version:        1.16.1
Release:        0
Summary:        C++ Interface for Cairo
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://www.cairographics.org/
Source:         https://www.cairographics.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(sigc++-3.0) >= 2.5.1

%description
This package provides a C++ interface for Cairo.

%package -n libcairomm-1_16-1
Summary:        C++ interface for Cairo
Group:          System/Libraries

%description -n libcairomm-1_16-1
This package provides a C++ interface for Cairo.

%package devel
Summary:        Header files for the Cairo C++ interface
Group:          Development/Libraries/GNOME
Requires:       libcairomm-1_16-1 = %{version}

%description devel
This package contains the header files for developing
applications that want to make use of cairomm.

%package doc
Summary:        Documentation for the Cairo C++ interface
Group:          Documentation/HTML

%description doc
This package provides documentation for the Cairo C++ interface.

%prep
%autosetup -p1
# fix permissions
chmod 0644 AUTHORS ChangeLog NEWS README

%build
%meson \
	-Dbuild-documentation=true \
	%{nil}
%meson_build

%install
%meson_install

%post -n libcairomm-1_16-1 -p /sbin/ldconfig
%postun -n libcairomm-1_16-1 -p /sbin/ldconfig

%files -n libcairomm-1_16-1
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%dir %{_libdir}/cairomm-1.16/
%{_libdir}/cairomm-1.16/include
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%{_datadir}/devhelp/books/cairomm-1.16
%{_datadir}/doc/cairomm-1.16
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
