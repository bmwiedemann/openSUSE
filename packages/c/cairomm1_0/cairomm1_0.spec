#
# spec file for package cairomm1_0
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


%define _name   cairomm
Name:           cairomm1_0
Version:        1.12.2
Release:        0
Summary:        C++ Interface for Cairo
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://cairographics.org
Source:         http://cairographics.org/releases/%{_name}-%{version}.tar.gz
# needs doxygen for the documentation
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.5.1

%description
This package provides a C++ interface for Cairo.

%package -n libcairomm-1_0-1
Summary:        C++ interface for Cairo
Group:          System/Libraries

%description -n libcairomm-1_0-1
This package provides a C++ interface for Cairo.

%package devel
Summary:        Header files for the Cairo C++ interface
Group:          Development/Libraries/GNOME
Requires:       libcairomm-1_0-1 = %{version}

%description devel
This package contains the header files for developing
applications that want to make use of cairomm1_0.

%package doc
Summary:        Documentation for the Cairo C++ interface
Group:          Documentation/HTML

%description doc
This package provides documentation for the Cairo C++ interface.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libcairomm-1_0-1 -p /sbin/ldconfig
%postun -n libcairomm-1_0-1 -p /sbin/ldconfig

%files -n libcairomm-1_0-1
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%dir %{_libdir}/cairomm-1.0/
%{_libdir}/cairomm-1.0/include
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%{_datadir}/devhelp/books/cairomm-1.0
%{_datadir}/doc/cairomm-1.0
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
