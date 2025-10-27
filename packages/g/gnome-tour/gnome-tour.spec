#
# spec file for package gnome-tour
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        49.0.openSUSE+git20251020.478f3eb
Release:        0
Summary:        GNOME Tour & Greeter
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://github.com/openSUSE/gnome-tour
Source0:        %{name}-%{version}.tar.zst
Source2:        vendor.tar.zst

BuildRequires:  AppStream
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(glib-2.0) >= 2.64
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1
Requires:       %{name}-data = %{version}

%description
A guided tour and greeter for GNOME.

%package data
Summary:        GNOME Tour data
BuildArch:      noarch

%description data
GNOME Tour & Greeter data files

%lang_package

%package -n opensuse-welcome
Summary:        Welcome utility for openSUSE
Requires:       %{name}-data = %{version}

%description -n opensuse-welcome
A welcome utility built to welcome new users to openSUSE.

%lang_package -n opensuse-welcome

%prep
%autosetup -p1 -a2

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
%find_lang opensuse-welcome %{?no_lang_C}

%check
%meson_test
%cargo_test

%files
%license LICENSE.md
%doc README.md
%{_bindir}/gnome-tour
%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml
%{_datadir}/applications/org.gnome.Tour.desktop
%{_datadir}/dbus-1/services/org.gnome.Tour.service

%files data
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/symbolic/apps/*
%{_datadir}/%{name}/resources.gresource
%dir %{_datadir}/%{name}

%files lang -f %{name}.lang

%files -n opensuse-welcome
%{_bindir}/opensuse-welcome
%{_datadir}/applications/org.opensuse.Welcome.desktop
%{_datadir}/dbus-1/services/org.opensuse.Welcome.service

%files -n opensuse-welcome-lang -f opensuse-welcome.lang

%changelog
