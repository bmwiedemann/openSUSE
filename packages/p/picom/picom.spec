#
# spec file for package picom
#
# Copyright (c) 2022 SUSE LLC
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


Name:           picom
Version:        10.1
Release:        0
Summary:        Stand-alone compositor for X11
License:        MIT AND MPL-2.0
Group:          System/X11/Utilities
URL:            https://github.com/yshui/picom
Source0:        https://github.com/yshui/picom/archive/v%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  c_compiler
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  uthash-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xext)
Obsoletes:      compton <= 0.1.0
Provides:       compton = %{version}

%description
Picom is a stand-alone compositor for X11. It supports both GLX and
XRender backends and has various options to control shadows, blur
and fade animations.

%prep
%setup -q

%build
%meson -Dwith_docs=true -Dcompton=false -Dvsync_drm=true
%meson_build

%install
%meson_install
install -d %{buildroot}%{_datadir}/icons/hicolor/{48x48,scalable}/apps
install -m644 media/icons/48x48/compton.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m644 media/compton.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%check
%meson --reconfigure -Dunittest=true
%meson_test

%files
%license LICENSES/MPL-2.0 LICENSES/MIT COPYING
%doc CONTRIBUTORS README.md picom.sample.conf
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/applications/%{name}.desktop
%config %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-trans.1%{?ext_man}

%changelog
