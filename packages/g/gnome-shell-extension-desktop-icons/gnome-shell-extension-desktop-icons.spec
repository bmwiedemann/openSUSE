#
# spec file for package gnome-shell-extension-desktop-icons
#
# Copyright (c) 2019 SUSE LLC.
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
Version:        19.10.2
Release:        0
Summary:        Desktop icon support for GNOME Shell
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/World/ShellExtensions/desktop-icons
Source:         desktop-icons-%{version}.tar.xz
BuildRequires:  gnome-patch-translation
# Needed for directory ownership
BuildRequires:  gnome-shell >= 3.30
# gobject-introspection is needed for the typelib() rpm magic.
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 0.44.0
BuildRequires:  translation-update-upstream
Requires:       gnome-shell
Requires:       nautilus >= 3.30.4
Requires:       xdg-desktop-portal-gtk
BuildArch:      noarch

%description
This package provides a GNOME Shell extension for showing the contents
of ~/Desktop on the desktop of the Shell. Common file management
operations such as launching, copy/paste, rename and deleting are
supported.

%prep
%setup -q -n desktop-icons-%{version}
translation-update-upstream po %{name}
gnome-patch-translation-prepare po %{name}

%build
%meson \
    --localedir=share/gnome-shell/extensions/desktop-icons@csoriano/locale
%meson_build

%install
%meson_install

%files
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.desktop-icons.gschema.xml
%{_datadir}/gnome-shell/extensions/desktop-icons@csoriano/

%changelog
