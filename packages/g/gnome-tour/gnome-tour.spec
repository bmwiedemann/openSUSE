#
# spec file for package gnome-tour
#
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           gnome-tour
Version:        44.0
Release:        0
Summary:        GNOME Tour & Greeter
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        %{name}-%{version}.tar.xz
Source2:        vendor.tar.zst
Source3:        cargo_config

BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(glib-2.0) >= 2.64
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1

%description
A guided tour and greeter for GNOME.

%lang_package

%prep
%autosetup -p1 -a2
mkdir .cargo
cp %{SOURCE3} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
%meson \
	-D profile=default \
	%{nil}
%meson_build

%install
export RUSTFLAGS=%{rustflags}
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test
%cargo_test

%files
%license LICENSE.md
%doc README.md
%{_bindir}/gnome-tour
%{_datadir}/applications/org.gnome.Tour.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/symbolic/apps/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources.gresource
%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml

%files lang -f %{name}.lang

%changelog
