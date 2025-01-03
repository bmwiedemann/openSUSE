#
# spec file for package granite
#
# Copyright (c) 2025 SUSE LLC
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


%define         sover 7
%define         soname 7_6_0
%define         appid io.elementary.granite-%{sover}
Name:           granite
Version:        7.6.0
Release:        0
Summary:        An extension of GTK+ libraries
License:        LGPL-3.0-or-later
URL:            https://github.com/elementary/granite
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-version.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.57.0
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  vala >= 0.48.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.4

%description
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in Pantheon applications.

%package -n     lib%{name}-%{sover}-%{sover}
Summary:        Granite is a development library
Requires:       %{name}-common
Provides:       %{name} = %{version}

%description -n lib%{name}-%{sover}-%{sover}
This package ships the library parts of %{name}.

%package        common
Summary:        Common files for the Granite development library
BuildArch:      noarch

%description    common
This package contains the common files needed by the library.

%package        demo
Summary:        Demo binaries for the Granite development library

%description    demo
This package contains a small demo application to show the %{name} widgets.

%package -n     typelib-1_0-Granite-7_0
Summary:        Introspection bindings for the Granite development library

%description -n typelib-1_0-Granite-7_0
This package provides the GObject Introspection bindings for libgranite.

%package        devel
Summary:        Development files for the Granite development library
Requires:       lib%{name}-%{sover}-%{sover} = %{version}
Requires:       typelib-1_0-Granite-%{sover}_0 = %{version}

%description    devel
Granite is an extension of GTK+.

This package contains the development files for libgranite.

%lang_package

%prep
%autosetup -p1

%build
%meson \
  -Ddocumentation=false \
  -Dintrospection=true \
  -Ddemo=true
%meson_build

%install
%meson_install
%find_lang %{name}-%{sover}
%fdupes -s %{buildroot}%{_datadir}

%ldconfig_scriptlets -n lib%{name}-%{sover}-%{sover}

%files -n lib%{name}-%{sover}-%{sover}
%{_libdir}/lib%{name}-%{sover}.so.*

%files common
%license COPYING
%doc README.md
%dir %{_datadir}/icons/hicolor/{48x48@2,48x48@2/apps}
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{name}-%{sover}.metainfo.xml
%{_datadir}/themes/Granite

%files demo
%{_bindir}/%{name}-%{sover}-demo
%{_datadir}/applications/%{appid}.demo.desktop

%files -n typelib-1_0-Granite-7_0
%{_libdir}/girepository-1.0/Granite-7.0.typelib

%files devel
%{_includedir}/%{name}-%{sover}
%{_libdir}/lib%{name}-%{sover}.so
%{_libdir}/pkgconfig/%{name}-%{sover}.pc
%{_datadir}/gir-1.0/Granite-*.0.gir
%{_datadir}/vala/vapi/%{name}-%{sover}.{deps,vapi}

%files lang -f %{name}-%{sover}.lang

%changelog
