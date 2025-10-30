#
# spec file for package gnome-console
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


Name:           gnome-console
Version:        49.1
Release:        0
Summary:        A minimal terminal for GNOME
License:        GPL-3.0-only
URL:            https://gitlab.gnome.org/GNOME/console
Source:         %{name}-%{version}.tar.zst

BuildRequires:  AppStream
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.59.0
BuildRequires:  mutter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.76
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4) >= 4.12.2
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.alpha
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libpcre2-8) >= 10.32
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.77.0

Obsoletes:      nautilus-extension-console < %{version}
Provides:       console = %{version}
Provides:       nautilus-extension-console = %{version}
Obsoletes:      console < 45.0

%description
Console is supposed to be a simple terminal emulator for the average
user to carry out simple cli tasks.
However, it is not trying to replace GNOME Terminal/Tilix; these
advanced tools are great for developers and administrators.
GNOME console rather aims to serve the casual linux user who rarely
needs a terminal.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D tests=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang kgx %{?no_lang_C} %{name}.lang

%ifnarch s390x
%check
export XDG_RUNTIME_DIR="$(mktemp -p $(pwd) -d xdg-runtime-XXXXXX)"
dbus-run-session -- mutter --headless --wayland --no-x11 --virtual-monitor 1024x768 -- %{shrink:%meson_test}
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/kgx
%{_datadir}/applications/org.gnome.Console.desktop
%{_datadir}/dbus-1/services/org.gnome.Console.service
%{_datadir}/glib-2.0/schemas/org.gnome.Console.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Console.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Console-symbolic.svg
%{_datadir}/metainfo/org.gnome.Console.metainfo.xml

%files lang -f %{name}.lang

%changelog
