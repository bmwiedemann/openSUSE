#
# spec file for package libxklavier
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libxklavier
Version:        5.4
Release:        0
Summary:        Library with X keyboard related functions
License:        LGPL-2.0-or-later
Group:          Development/Libraries/X11
URL:            http://www.freedesktop.org/Software/LibXklavier
#Source:         http://download.gnome.org/sources/libxklavier/5.4/%%{name}-%%{version}.tar.xz
Source:         http://people.freedesktop.org/~svu/libxklavier-5.4.tar.bz2

BuildRequires:  doxygen
BuildRequires:  gobject-introspection-devel >= 1.30
BuildRequires:  gtk-doc
BuildRequires:  iso-codes-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
Requires:       xkbcomp

%description
This library allows you to simplify XKB-related development.

%package devel
Summary:        Development files for libxklavier
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libxklavier16 = %{version}
Requires:       typelib-1_0-Xkl-1_0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libxklavier16
Summary:        Library with X keyboard related functions
Group:          System/Libraries
Requires:       iso-codes
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libxklavier16
This library allows you to simplify XKB-related development.

%package -n typelib-1_0-Xkl-1_0
Summary:        Introspection bindings for libxklavier
Group:          System/Libraries

%description -n typelib-1_0-Xkl-1_0
This library allows you to simplify XKB-related development.

This package provides the GObject Introspection bindings for
libxklavier.

%package doc
Summary:        Additional Package Documentation for libxklavier
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This library allows you to simplify XKB-related development.

%prep
%autosetup -p1

%build
%configure \
	--with-xkb-base=%{_datadir}/X11/xkb \
	--with-xkb-bin-base=%{_bindir} \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libxklavier16

%files -n libxklavier16
%license COPYING.LIB
%doc AUTHORS CREDITS ChangeLog NEWS README
%{_libdir}/libxklavier.so.*

%files -n typelib-1_0-Xkl-1_0
%{_libdir}/girepository-1.0/Xkl-1.0.typelib

%files devel
%{_includedir}/libxklavier/
%{_libdir}/libxklavier.so
%{_libdir}/pkgconfig/libxklavier.pc
%{_datadir}/gir-1.0/Xkl-1.0.gir

%files doc
%{_datadir}/gtk-doc/html/libxklavier

%changelog
