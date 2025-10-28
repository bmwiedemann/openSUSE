#
# spec file for package identity
#
# Copyright (c) 2025 mantarimay
# Copyright (c) 2023 SUSE LLC
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


%define _lto_cflags %{nil}
%define appid org.gnome.gitlab.YaLTeR.Identity
%define rurl 5e547a55dfcabeefe187e342e7040091
Name:           identity
Version:        25.10
Release:        0
Summary:        Compare images and videos
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/YaLTeR/identity
Source:         https://gitlab.gnome.org/-/project/12785/uploads/%{rurl}/%{name}-%{version}.tar.xz
BuildRequires:  blueprint-compiler
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6.0
BuildRequires:  pkgconfig(libwebpdemux)
Requires:       glycin-loaders

%description
A program for comparing multiple versions of an image or video.

%lang_package

%prep
%autosetup

sed -i "s/output: meson.project_name()/output: 'identity-compare'/g" src/meson.build
sed -i "s/Exec=identity/Exec=identity-compare/g" data/org.gnome.gitlab.YaLTeR.Identity.desktop.in.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}-compare
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{name}.lang

%changelog
