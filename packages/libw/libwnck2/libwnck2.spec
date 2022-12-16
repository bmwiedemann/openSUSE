#
# spec file for package libwnck2
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


%define _name   libwnck
# WARNING: After changing versions please call Re or rpmbuild to auto-update spec file:
#%(sh %{_sourcedir}/%{name}_spec-update.sh %{_sourcedir} %{name} libwnck-1)
%define libwnck-1_name 22
Name:           libwnck2
Version:        2.31.0
Release:        0
Summary:        Window Navigator Construction Kit (Library Package)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Source:         http://download.gnome.org/sources/libwnck/2.31/%{_name}-%{version}.tar.xz
Source1:        %{name}_spec-update.sh
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)

%description
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

%package -n libwnck-1-22
Summary:        Window Navigator Construction Kit (Library Package)
Group:          Development/Libraries/GNOME
# To make lang package installable
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libwnck-1-22
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

%package -n typelib-1_0-Wnck-1_0
Summary:        Window Navigator Construction Kit (Library Package) -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Wnck-1_0
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

This package provides the GObject Introspection bindings for libwnck.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/GNOME
Requires:       libwnck-1-22 = %{version}
Requires:       typelib-1_0-Wnck-1_0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%setup -q -n %{_name}-%{version}

%build
# needed for libwnck-2.19.4:
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure\
	--disable-static
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
rm %{buildroot}%{_libdir}/*.*a
# Those are provided by the GTK+ 3 version of libwnck now
rm %{buildroot}%{_bindir}/wnck-urgency-monitor
rm %{buildroot}%{_bindir}/wnckprop
%find_lang %{_name}
%fdupes %{buildroot}

%post -n libwnck-1-22 -p /sbin/ldconfig
%postun -n libwnck-1-22 -p /sbin/ldconfig

%files -n libwnck-1-22
%license COPYING
%doc AUTHORS README NEWS ChangeLog
%{_libdir}/*.so.*

%files -n typelib-1_0-Wnck-1_0
%{_libdir}/girepository-1.0/Wnck-1.0.typelib

%files devel
%{_includedir}/libwnck-1.0/
%{_libdir}/pkgconfig/libwnck-1.0.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Wnck-1.0.gir
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libwnck/

%files lang -f %{_name}.lang

%changelog
