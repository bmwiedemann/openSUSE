#
# spec file for package tepl
#
# Copyright (c) 2019 SUSE LLC
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


%define api_ver 4
%define lib_ver %{api_ver}-0
Name:           tepl
Version:        4.2.1
Release:        0
Summary:        Text Editor Product Line
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Projects/Tepl
Source:         https://download.gnome.org/sources/tepl/4.2/%{name}-%{version}.tar.xz
BuildRequires:  gobject-introspection-devel >= 1.42.0
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(amtk-5) >= 5.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.52
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5
BuildRequires:  pkgconfig(uchardet)

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. It is a continuation/rename of Gtef.

%package -n libtepl-%{lib_ver}
Summary:        A text editor framework
Group:          System/Libraries
Recommends:     %{name}-%{api_ver}-lang
Provides:       tepl-%{api_ver} = %{version}

%description -n libtepl-%{lib_ver}
Tepl (Text Editor Product Line) is a library that eases the
development of GtkSourceView-based text editors and IDEs. It is a
continuation / rename of Gtef

%package -n typelib-1_0-Tepl-%{api_ver}
Summary:        GObject introspection bindings for libtepl
Group:          System/Libraries

%description -n typelib-1_0-Tepl-%{api_ver}
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. It is a continuation/rename of Gtef.

This package provides the GObject Introspection bindings for tepl.

%package devel
Summary:        Development files for Tepl, a text editor framework
Group:          Development/Libraries/GNOME
Requires:       libtepl-%{lib_ver} >= %{version}
Requires:       typelib-1_0-Tepl-%{api_ver} >= %{version}

%description devel
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. It is a continuation/rename of Gtef.

This subpackage contains the header files for developing
applications that want to make use of tepl.

%lang_package -n %{name}-%{api_ver}

%prep
%setup -q

%build
%configure \
    --enable-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-%{api_ver}

%post   -n libtepl-%{lib_ver} -p /sbin/ldconfig
%postun -n libtepl-%{lib_ver} -p /sbin/ldconfig

%files -n libtepl-%{lib_ver}
%license COPYING
%doc NEWS
%{_libdir}/libtepl-%{api_ver}.so.*

%files -n typelib-1_0-Tepl-%{api_ver}
%{_libdir}/girepository-1.0/Tepl-%{api_ver}.typelib

%files devel
%doc ABOUT-NLS AUTHORS ChangeLog HACKING README
%doc %{_datadir}/gtk-doc/html/%{name}-4.0
%{_datadir}/gir-1.0/Tepl-%{api_ver}.gir
%{_includedir}/tepl-%{api_ver}/
%{_libdir}/pkgconfig/tepl-%{api_ver}.pc
%{_libdir}/*.so

%files -n %{name}-%{api_ver}-lang -f %{name}-%{api_ver}.lang

%changelog
