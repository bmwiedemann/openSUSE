#
# spec file for package xplayer-plparser
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


%define         _sover  18
Name:           xplayer-plparser
Version:        1.0.3
Release:        0
Summary:        Simple GObject-based library to parse playlist formats
License:        LGPL-2.0-or-later
URL:            https://github.com/linuxmint/xplayer-plparser
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libarchive) >= 3.0
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libquvi-0.9) >= 0.9.1
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.43.0
BuildRequires:  pkgconfig(libxml-2.0)

%description
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%lang_package

%package -n lib%{name}%{_sover}
Summary:        A simple GObject-based library to parse playlist formats
# Main package contains libexec files needed for full functionality.
Requires:       %{name} >= %{version}

%description -n lib%{name}%{_sover}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package -n typelib-1_0-XplayerPlParser-1_0
Summary:        Introspection Bindings
# Main package contains libexec files needed for full functionality.
Requires:       %{name} >= %{version}

%description -n typelib-1_0-XplayerPlParser-1_0
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

This package provides the GObject Introspection bindings for the
xplayer-plparser library.

%package -n lib%{name}-mini%{_sover}
Summary:        Mini Version of lib%{name}%{_sover}
# Main package contains libexec files needed for full functionality.
Requires:       %{name} >= %{version}

%description -n lib%{name}-mini%{_sover}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package devel
Summary:        Simple GObject-based library to parse playlist formats
Requires:       lib%{name}%{_sover} = %{version}
Requires:       lib%{name}-mini%{_sover} = %{version}
Requires:       typelib-1_0-XplayerPlParser-1_0 = %{version}

%description devel
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
This package offers you the documentation for %{name}.

%prep
%autosetup

%build
%meson \
  -Ddisable-gmime-i-know-what-im-doing=false \
  -Denable-quvi=yes \
  -Denable-libarchive=yes \
  -Denable-libgcrypt=yes \
  -Denable-uninstalled-tests=false \
  -Denable-gtk-doc=true
%meson_build

%install
%meson_install

%find_lang xplayer-pl-parser %{?no_lang_C}

%ldconfig_scriptlets -n lib%{name}%{_sover}

%ldconfig_scriptlets -n lib%{name}-mini%{_sover}

%files
%license COPYING.LIB
%doc ChangeLog MAINTAINERS NEWS README
%{_libexecdir}/xplayer-pl-parser-videosite

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*

%files -n typelib-1_0-XplayerPlParser-1_0
%{_libdir}/girepository-1.0/XplayerPlParser-1.0.typelib

%files -n lib%{name}-mini%{_sover}
%{_libdir}/lib%{name}-mini.so.%{_sover}*

%files devel
%{_includedir}/xplayer-pl-parser
%{_libdir}/lib%{name}{,-mini}.so
%{_libdir}/pkgconfig/%{name}{,-mini}.pc
%{_datadir}/gir-1.0/*.gir

%files doc
%{_datadir}/gtk-doc/html/xplayer-pl-parser

%files lang -f xplayer-pl-parser.lang

%changelog
