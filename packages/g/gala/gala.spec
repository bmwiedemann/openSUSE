#
# spec file for package gala
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


%define         sover 0
%define         appid io.elementary.desktop.wm
Name:           gala
Version:        8.0.1
Release:        0
Summary:        The Pantheon window manager
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/gala
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/elementary/gala/pull/2090
Patch0:         support-libmutter15.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  valadoc-doclet-html
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libhandy-1)
%if 0%{?suse_version} <= 1600
BuildRequires:  pkgconfig(libmutter-13)
%else
BuildRequires:  pkgconfig(libmutter-15)
%endif
BuildRequires:  pkgconfig(sqlite3)

%description
Gala is a window and compositing manager based on libmutter. It manages the
various windows a user has open.

It takes care of behaviors such as moving windows around, window switching,
window overview, animating windows, maximization, multiple workspaces,
providing accessibility features like zoom, and more.

%package -n     lib%{name}%{sover}
Summary:        Gala is a library for Elementary development
Group:          System/Libraries

%description -n lib%{name}%{sover}
Gala is a window and compositing manager based on libmutter. It manages the
various windows a user has open.

%package        plugins
Summary:        A collection of plugins for %{name}
Requires:       %{name} = %{version}

%description    plugins
Gala is a window and compositing manager based on libmutter. It manages the
various windows a user has open.

This package contains a collection of plugins: zoom, notify, maskcorners etc.

%package        devel
Summary:        Gala development library -- Development files
Requires:       lib%{name}%{sover} = %{version}

%description    devel
Gala is a window and compositing manager based on libmutter. It manages the
various windows a user has open.

This package contains the development files for %{name}

%lang_package

%prep
%autosetup -N
%if 0%{?suse_version} == 1699
%autopatch -p1
%endif

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson \
  -Ddocumentation=false \
  -Dsystemd=true
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license COPYING
%doc AUTHORS README.md
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.%{name}.gschema.xml
%{_datadir}/applications/%{name}{,-multitaskingview,-other,-wayland}.desktop
%{_bindir}/%{name}{,-daemon,-daemon-gtk3}
%{_userunitdir}/io.elementary.gala.target
%{_userunitdir}/io.elementary.gala@wayland.service
%{_userunitdir}/io.elementary.gala@x11.service
%{_sysconfdir}/xdg/%{appid}.shell

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files plugins
%{_libdir}/%{name}

%files devel
%{_datadir}/vala/vapi/%{name}.{deps,vapi}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%files lang -f %{name}.lang

%changelog
