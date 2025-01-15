#
# spec file for package loupe
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


Name:           loupe
Version:        47.3
Release:        0
Summary:        A simple image viewer application
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/loupe
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst

BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4) >= 4.13.6
BuildRequires:  pkgconfig(gweather4) >= 4.0.0
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.0
BuildRequires:  pkgconfig(libheif) >= 1.14.2
BuildRequires:  pkgconfig(libseccomp) >= 2.5.0
Requires:       glycin-loaders

%description
%{summary} written with GTK4 and Rust.

%lang_package

%prep
%autosetup -p1 -a1

%build
export RUSTFLAGS="%{build_rustflags}"
%meson \
	%{nil}
%meson_build

%install
export RUSTFLAGS="%{build_rustflags}"
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
export RUSTFLAGS="%{build_rustflags}"
%cargo_test
# No meson_test exists upstream yet, so run these manually
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Loupe.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Loupe.desktop

%files
%license COPYING.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Loupe.desktop
%{_datadir}/dbus-1/services/org.gnome.Loupe.service
%{_datadir}/glib-2.0/schemas/org.gnome.Loupe.gschema.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Loupe.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Loupe.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Loupe-symbolic.svg
%{_datadir}/metainfo/org.gnome.Loupe.metainfo.xml

%files lang -f %{name}.lang

%changelog
