#
# spec file for package libgtkdatabox
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libver 0_9_3-0

Name:           libgtkdatabox
Version:        0.9.3.0
Release:        0
Summary:        GTK+ widget for fast data display
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://sourceforge.net/projects/gtkdatabox
Source0:        http://sourceforge.net/projects/gtkdatabox/files/gtkdatabox/%{version}/gtkdatabox-%{version}.tar.gz
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GtkDatabox is a widget for the Gtk+ library designed to display large
amounts of numerical data fast and easy.

%package devel
Summary:        Development files for GtkDatabox
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The libgtkdatabox-devel package contains libraries, header files and
documentation for developing applications that use libgtkdatabox.

%package -n %{name}-%{libver}
Summary:        GTK+ widget for fast data display
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      %{name}-%{libver} < %{version}

%description -n %{name}-%{libver}
GtkDatabox is a widget for the Gtk+ library designed to display large
amounts of numerical data fast and easy.

%prep
%setup -q -n gtkdatabox-%{version}

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -n %{name}-%{libver} -p /sbin/ldconfig

%postun -n %{name}-%{libver} -p /sbin/ldconfig

%files -n %{name}-%{libver}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/%{name}-*.so.*

%files devel
%defattr(-,root,root)
%doc examples/*.c
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/gtkdatabox.pc

%changelog
