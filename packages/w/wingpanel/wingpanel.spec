#
# spec file for package wingpanel
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


%define         sover 8
%define         appid io.elementary.wingpanel
Name:           wingpanel
Version:        8.0.3
Release:        0
Summary:        Stylish top panel that holds indicators
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/wingpanel
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gala)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libmutter-15)
Requires:       notify-osd

%description
This is the GTK-based panel developed by the ElementaryOS team for their
Pantheon desktop environment. It is a replacement for the traditional GNOME
Panel, designed to be a lightweight container for system/application
indicators and notification icons.

%package -n     lib%{name}%{sover}
Summary:        A library for a simple Graphical User Interface

%description -n lib%{name}%{sover}
This is the GTK-based panel developed by the ElementaryOS team for their
Pantheon desktop environment. It is a replacement for the traditional GNOME
Panel, designed to be a lightweight container for system/application
indicators and notification icons.

%package        devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description    devel
Development and Header files for package %{name}.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}
%find_lang %{appid}

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_libdir}/gala/plugins/lib%{name}-interface.so
%dir %{_libdir}/{gala/plugins,gala}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/vala/vapi/%{name}.{deps,vapi}

%files lang -f %{appid}.lang

%changelog
