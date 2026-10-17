#
# spec file for package noctalia
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           noctalia
Version:        5.3.0
Release:        0
Summary:        A sleek and minimal desktop shell thoughtfully crafted for Wayland.
License:        MIT
URL:            https://github.com/noctalia-dev/noctalia
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(md4c)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sdbus-c++) >= 2.0.0
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(stb)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       git
Requires:       qalculate

Recommends:     upower

Conflicts:      noctalia-git

%description
A lightweight Wayland shell and bar built directly on Wayland + OpenGL ES, with no Qt or GTK dependency.

Noctalia is in early development. Expect breaking configuration and behavior changes while the project is still taking shape.

%prep
%autosetup

%build
%meson -Dtests=disabled
%meson_build

%install
%meson_install

find %{buildroot}%{_datadir}/noctalia/assets/templates \
	-type f -name '*.sh' \
	-exec sed -i '1s|^#!/usr/bin/env bash$|#!/usr/bin/bash|' {} +

find %{buildroot}%{_datadir}/noctalia/assets/templates \
	-type f -name '*.py' \
	-exec sed -i '1s|^#!/usr/bin/env python3$|#!/usr/bin/python3|' {} +

find %{buildroot}%{_datadir}/noctalia/assets/templates \
	-type f \( -name '*.sh' -o -name '*.py' \) \
	-exec chmod 0755 {} +

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc README.md
%{_bindir}/noctalia
%{_datadir}/noctalia
%{_datadir}/applications/dev.noctalia.Noctalia.desktop
%{_datadir}/icons/hicolor/scalable/apps/noctalia.svg

%changelog
