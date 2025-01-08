#
# spec file for package fractal
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


%define _lto_cflags %{nil}

%define         appname org.gnome.Fractal
%define         glib_version       2.72
%define         gstreamer_version  1.20
%define         is_beta            %(if echo %{version}|grep -q beta;then echo 1;fi)
%{?is_beta:%bcond_without beta_build}%{!?is_beta:%bcond_with beta_build}

Name:           fractal
Version:        9
Release:        0
Summary:        Matrix group messaging app
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://gitlab.gnome.org/World/fractal/-/tags
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst

BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  desktop-file-utils
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
#BuildRequires:  pkgconfig(glycin-gtk4-1)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gstreamer-play-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.0.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.0
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(shumate-1.0) >= 1.0.0
BuildRequires:  pkgconfig(sqlite3) >= 3.24.0
BuildRequires:  pkgconfig(xdg-desktop-portal) >= 1.14.1
Requires:       glycin-loaders
Requires:       gstreamer-plugins-good-gtk
ExclusiveArch:  %{rust_tier1_arches}

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its
interface is tuned for collaboration in large groups, such as
free software projects.

%lang_package

%prep
%autosetup -p1 -a1

%build
export RUSTFLAGS="%{build_rustflags}"
%meson \
    -Dprofile=%{?with_beta_build:beta}%{!?with_beta_build:default} \
    ;
%meson_build

%install
export RUSTFLAGS="%{build_rustflags}"
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/{ui-,}resources.gresource
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}*.*
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/dbus-1/services/%{appname}.service

%files lang -f %{name}.lang

%changelog
