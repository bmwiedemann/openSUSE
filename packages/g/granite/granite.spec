#
# spec file for package granite
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 6
%define soname libgranite
%define _typelibdir %(pkg-config --variable=typelibdir gobject-introspection-1.0)
%define _girdir %(pkg-config --variable=girdir gobject-introspection-1.0)
Name:           granite
Version:        6.2.0
Release:        0
Summary:        An extension of GTK+ libraries
License:        LGPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://elementary.io/
Source:         https://github.com/elementary/granite/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.48.2
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.48.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0

%description
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in Elementary applications.

%package -n     %{soname}%{sover}
Summary:        Granite is a development library
Group:          System/Libraries
Requires:       %{name}-common
Provides:       %{name} = %{version}

%description -n %{soname}%{sover}
Granite is an extension of GTK+. It provides the commonly used widgets
found in Elementary applications.

%package        common
Summary:        Common files for the Granite development library
Group:          System/Libraries
Recommends:     %{name}-lang

%description    common
Granite is an extension of GTK+.

This package contains the common files needed by the library.

%package        demo
Summary:        Demo binaries for the Granite development library
Group:          Development/Libraries/Other

%description    demo
Granite is an extension of GTK+.

This package contains a small demo application to show the %{name} widgets.

%package -n     typelib-1_0-Granite-1_0
Summary:        Introspection bindings for the Granite development library
Group:          Development/Libraries/GNOME

%description -n typelib-1_0-Granite-1_0
Granite is an extension of GTK+.

This package provides the GObject Introspection bindings for %{soname}.

%package        devel
Summary:        Development files for the Granite development library
Group:          Development/Libraries/GNOME
Requires:       %{soname}%{sover} = %{version}

%description    devel
Granite is an extension of GTK+.

This package contains the development files for %{soname}.

%lang_package

%prep
%setup -q

# Fix: invalid-filename-dependency
# Can't install typelib-1_0-Granite nothing provides libgranite.so.*()(64bit)
sed -e "s/\(.\)@PLAINNAME@\(.\)/\1%{soname}.so.%{sover}\2/" \
    -i lib/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes -s %{buildroot}%{_datadir}

%post   -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files common
%license COPYING
%doc README*
%{_datadir}/icons/hicolor/*/actions/appointment.??g
%{_datadir}/icons/hicolor/*/actions/open-menu*.??g
%{_datadir}/metainfo/granite.appdata.xml

%files demo
%{_bindir}/%{name}-demo
%{_datadir}/applications/io.elementary.granite.demo.desktop

%files -n typelib-1_0-Granite-1_0
%{_typelibdir}/Granite-1.0.typelib

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_girdir}/Granite-1.0.gir
%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi

%files lang -f %{name}.lang

%changelog
