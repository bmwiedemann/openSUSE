#
# spec file for package gnome-shell-extension-desktop-icons
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gnome-shell-extension-desktop-icons
Version:        51.1.1
Release:        0
Summary:        Desktop icon NG support for GNOME Shell
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.com/rastersoft/desktop-icons-ng
Source:         desktop-icons-ng-%{version}.tar.xz

# Needed for directory ownership
BuildRequires:  gnome-shell >= 3.30
# gobject-introspection is needed for the typelib() rpm magic.
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 1.1
Requires:       gnome-shell
Requires:       nautilus >= 3.30.4
Requires:       xdg-desktop-portal-gtk
BuildArch:      noarch

%description
What  is it
Desktop Icons NG for GNOME Shell. It is a fork/rewrite of the official 'Desktop Icons' extension,
with these advantages:

Drag'n'Drop, both inside the desktop, between desktop and applications, and nautilus windows
Allows to use "Open with..." option with several files
When hovering or clicking on an icon with a name too large to fit, it shows the full name
Doesn't hang the compositor when there is too much activity in the desktop folder
And much more...

%prep
%autosetup -n desktop-icons-ng-%{version}

%build
%meson \
    --localedir=share/gnome-shell/extensions/ding@rastersoft.com/locale
%meson_build

%install
%meson_install

%files
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.ding.gschema.xml
%{_datadir}/gnome-shell/extensions/ding@rastersoft.com/
%dir %{_sysconfdir}/apparmor.d/
%config %{_sysconfdir}/apparmor.d/ding@rastersoft.com

%changelog
