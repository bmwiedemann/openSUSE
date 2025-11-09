#
# spec file for package gearlever
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


%define appid it.mijorus.gearlever
Name:           gearlever
Version:        3.4.7
Release:        0
Summary:        Manage AppImages
License:        GPL-3.0-or-later
URL:            https://gearlever.mijorus.it/
Source:         https://github.com/mijorus/gearlever/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Group:          System/X11/Utilities
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  gtk4-tools
BuildRequires:  meson
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0)
Requires:       7zip
Requires:       dwarfs
Requires:       flatpak-spawn
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       python3-requests
Requires:       squashfs
Requires:       typelib(Adw) = 1
Requires:       typelib(GLib)
Requires:       typelib(Gio)
Requires:       typelib(Gtk) = 4.0

%description
An utility to manage AppImages with ease! Gear lever will organize and manage
AppImage files for you, generate desktop entries and app metadata, update apps
in-place or keep multiple versions side-by-side.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name --all-name
%suse_update_desktop_file %{appid}
%fdupes %{buildroot}/%{_prefix}
rm %{buildroot}/%{_datadir}/gearlever/gearlever/assets/demo.AppImage
find %{buildroot} -iname 'meson.build' -delete
%ifpycache
%py3_compile %{buildroot}%{_datadir}/%{name}
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%pycache_only %{_datadir}/%{name}/%{name}/__pycache__
%pycache_only %{_datadir}/%{name}/%{name}/**/__pycache__
%{_datadir}/appdata/%{appid}.appdata.xml
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg

%files lang -f %{name}.lang

%changelog
