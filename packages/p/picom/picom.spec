#
# spec file for package picom
#
# Copyright (c) 2020 SUSE LLC
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
Version:        8
Release:        0
Summary:        Stand-alone compositor for X11
License:        MPL-2.0 AND MIT
Group:          System/X11/Utilities
URL:            https://github.com/yshui/picom
Source0:        https://github.com/yshui/picom/archive/v8.tar.gz
Source1:        picom.desktop
BuildRequires:  asciidoc
BuildRequires:  c_compiler
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  uthash-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
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
Requires:       hicolor-icon-theme
Obsoletes:      compton <= 0.1.0
Provides:       compton = %{version}

%description
Picom is a stand-alone compositor for X11. It supports both GLX and
XRender backends and has various options to control shadows, blur
and fade animations.

%prep
%setup -q

%build
%meson -Dwith_docs=true
%meson_build

%install
%meson_install
mv %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/compton.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/compton.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
rm %{buildroot}%{_datadir}/applications/compton.desktop

cp %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSES/MPL-2.0 LICENSES/MIT COPYING
%doc CONTRIBUTORS README.md README_orig.md picom.sample.conf
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-trans.1%{?ext_man}

%changelog
