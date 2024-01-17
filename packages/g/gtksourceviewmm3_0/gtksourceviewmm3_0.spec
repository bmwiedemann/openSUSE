#
# spec file for package gtksourceviewmm3_0
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _name gtksourceviewmm

Name:           gtksourceviewmm3_0
Version:        3.21.3
Release:        0
Summary:        C++ interface for gtksourceview
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://projects.gnome.org/gtksourceviewmm/
Source0:        https://download.gnome.org/sources/gtksourceviewmm/3.21/%{_name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46.1
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.18.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.18.0

%description
gtksourceviewmm provides a C++ interface to the gtksourceview library.

%package -n libgtksourceviewmm-3_0-0
Summary:        C++ interface for gtksourceview
Group:          System/Libraries

%description -n libgtksourceviewmm-3_0-0
gtksourceviewmm provides a C++ interface to the gtksourceview library.

%package devel
Summary:        Development files for the gtksourceview C++ interface
Group:          Development/Libraries/C and C++
Requires:       libgtksourceviewmm-3_0-0 = %{version}

%description devel
gtksourceviewmm provides a C++ interface to the gtksourceview library.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgtksourceviewmm-3_0-0 -p /sbin/ldconfig
%postun -n libgtksourceviewmm-3_0-0 -p /sbin/ldconfig

%files -n libgtksourceviewmm-3_0-0
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/gtksourceviewmm-3.0/
%{_libdir}/gtksourceviewmm-3.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gtksourceviewmm-3.0.pc
%doc %{_datadir}/devhelp/books/gtksourceviewmm-3.0/
%doc %{_datadir}/doc/gtksourceviewmm-3.0/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
