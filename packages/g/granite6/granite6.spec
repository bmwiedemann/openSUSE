#
# spec file for package granite6
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


%define         sover 6
%define         soname 6_2_0
%define         appid io.elementary.granite
Name:           granite6
Version:        6.2.0
Release:        0
Summary:        An extension of GTK+ libraries
License:        LGPL-3.0-or-later
URL:            https://github.com/elementary/granite
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-version.patch
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  meson >= 0.48.2
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  vala >= 0.48.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libbrotlicommon)

%description
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in Pantheon applications.

%package -n     libgranite%{sover}
Summary:        Granite is a development library
Requires:       %{name}-common
Provides:       %{name} = %{version}
Provides:       granite = %{version}
Obsoletes:      granite < %{version}

%description -n libgranite%{sover}
This package provides the library files for %{name}

%package        common
Summary:        Common files for the Granite development library
BuildArch:      noarch

%description    common
This package contains the common files needed by the library %{name}

%package        demo
Summary:        Demo binaries for the Granite development library

%description    demo
This package contains a small demo application to show a widget of %{name}

%package -n     typelib-1_0-Granite-1_0
Summary:        Introspection bindings for the Granite development library

%description -n typelib-1_0-Granite-1_0
This package provides the GObject Introspection bindings for lib%{name}.

%package        devel
Summary:        Development files for the Granite development library
Requires:       libgranite%{sover} = %{version}
Requires:       typelib-1_0-Granite-1_0 = %{version}

%description    devel
This package contains the development files for lib%{name}.

%lang_package

%prep
%autosetup -p1 -n granite-%{version}

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson \
  -Ddocumentation=false \
  -Dintrospection=true
%meson_build

%install
%meson_install
%find_lang granite
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n libgranite%{sover}

%files -n libgranite%{sover}
%{_libdir}/libgranite.so.%{sover}*

%files common
%license COPYING
%doc README.md
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/metainfo/granite.appdata.xml

%files demo
%{_bindir}/granite-demo
%{_datadir}/applications/%{appid}.demo.desktop

%files -n typelib-1_0-Granite-1_0
%{_libdir}/girepository-1.0/Granite-1.0.typelib

%files devel
%{_includedir}/granite
%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.{deps,vapi}

%files lang -f granite.lang

%changelog
