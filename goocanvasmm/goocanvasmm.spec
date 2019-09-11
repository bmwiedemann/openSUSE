#
# spec file for package goocanvasmm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009-2011 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           goocanvasmm
Version:        1.90.11
Release:        0
Summary:        C++ interface for goocanvas
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://gtkmm.sourceforge.net/
Source0:        http://download.gnome.org/sources/goocanvasmm/1.90/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46.1
BuildRequires:  pkgconfig(goocanvas-2.0) >= 2.0.1
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.18.0

%description
This package provides a C++ interface for goocanvas. It is a
subpackage of the gtkmm project. The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.

%package -n libgoocanvasmm-2_0-6
Summary:        C++ interface for goocanvas
Group:          System/Libraries

%description -n libgoocanvasmm-2_0-6
This package provides a C++ interface for goocanvas. It is a
subpackage of the gtkmm project. The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.

%package -n libgoocanvasmm-devel
Summary:        C++ interface for goocanvas
Group:          Development/Libraries/GNOME
Requires:       libgoocanvasmm-2_0-6 = %{version}

%description -n libgoocanvasmm-devel
This package provides a C++ interface for goocanvas. It is a
subpackage of the gtkmm project. The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.

This package contains the libraries and header files needed for
developing applications.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgoocanvasmm-2_0-6 -p /sbin/ldconfig
%postun -n libgoocanvasmm-2_0-6 -p /sbin/ldconfig

%files -n libgoocanvasmm-2_0-6
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgoocanvasmm-2.0.so.*

%files -n libgoocanvasmm-devel
%{_includedir}/goocanvasmm-2.0/
%{_libdir}/libgoocanvasmm-2.0.so
%{_libdir}/pkgconfig/goocanvasmm-2.0.pc
%{_libdir}/goocanvasmm-2.0/
%doc %{_datadir}/devhelp/books/goocanvasmm-2.0
%doc %{_datadir}/doc/goocanvasmm-2.0
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
