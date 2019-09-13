#
# spec file for package pangomm1_4
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Update baselibs.conf when changing this
%define so_ver -1_4-1
%define _name   pangomm
Name:           pangomm1_4
Version:        2.42.0
Release:        0
Summary:        C++ interface for pango
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gtkmm.org
Source0:        https://download.gnome.org/sources/pangomm/2.42/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairomm-1.0) >= 1.2.2
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.48.0
BuildRequires:  pkgconfig(pangocairo) >= 1.38.0

%description
pangomm provides a C++ interface to the pango library.

%package -n libpangomm%{so_ver}
Summary:        C++ interface for pango
Group:          System/Libraries

%description -n libpangomm%{so_ver}
pangomm provides a C++ interface to the pango library.

%package devel
Summary:        C++ interface for pango -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libpangomm%{so_ver} = %{version}

%description devel
pangomm provides a C++ interface to the pango library.

%package doc
Summary:        C++ interface for pango -- Developer Documentation
Group:          Documentation/HTML

%description doc
pangomm provides a C++ interface to the pango library.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}

%post -n libpangomm%{so_ver} -p /sbin/ldconfig

%postun -n libpangomm%{so_ver} -p /sbin/ldconfig

%files -n libpangomm%{so_ver}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-1.4

%files doc
%{_datadir}/devhelp/books/pangomm-1.4/
%{_datadir}/doc/pangomm-1.4/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
