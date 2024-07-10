#
# spec file for package gdl
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


Name:           gdl
Version:        3.40.0
Release:        0
Summary:        Gnome Devtool Libraries
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/GNOME/gdl
Source:         https://download.gnome.org/sources/gdl/3.40/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool >= 0.40.4
BuildRequires:  libxml2-devel

%description
Gnome Devtool Libraries contains components and libraries that are
intended to be shared between GNOME development tools, including
gnome-debug, gnome-build, and anjuta2.

%package -n libgdl-3-5
Summary:        Gnome Devtool Libraries
Group:          System/Libraries
Provides:       gdl = %{version}
Obsoletes:      gdl < %{version}

%description -n libgdl-3-5
Gnome Devtool Libraries contains components and libraries that are
intended to be shared between GNOME development tools, including
gnome-debug, gnome-build, and anjuta2.

%package -n typelib-1_0-Gdl-3
Summary:        Introspection bindings for the Gnome Devtool libraries
Group:          System/Libraries

%description -n typelib-1_0-Gdl-3
Gnome Devtool Libraries contains components and libraries that are
intended to be shared between GNOME development tools, including
gnome-debug, gnome-build, and anjuta2.

This package provides the GObject Introspection bindings for GDL.

%package devel
Summary:        Development files for the Gnome Devtool libraries
Group:          Development/Libraries/GNOME
Requires:       libgdl-3-5 = %{version}
Requires:       typelib-1_0-Gdl-3 = %{version}

%description devel
Gnome Devtool Libraries contains components and libraries that are
intended to be shared between GNOME development tools, including
gnome-debug, gnome-build, and anjuta2.

%lang_package

%prep
%autosetup -p1

%build
%global optflags %{optflags} -Wno-error=incompatible-pointer-types
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-3
%fdupes -s %{buildroot}

%post -n libgdl-3-5 -p /sbin/ldconfig
%postun -n libgdl-3-5 -p /sbin/ldconfig

%files -n libgdl-3-5
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-Gdl-3
%{_libdir}/girepository-1.0/Gdl-3.typelib

%files devel
%{_includedir}/libgdl*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Gdl-3.gir
%{_datadir}/gtk-doc/

%files lang -f %{name}-3.lang

%changelog
