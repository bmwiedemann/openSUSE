#
# spec file for package gnome-shell-extension-desktop-icons
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


Name:           gnome-shell-extension-desktop-icons
Version:        47.0.12+3
Release:        0
Summary:        Desktop icon support for GNOME Shell
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.com/rastersoft/desktop-icons-ng
# Source url disabled as we are using a git checkout via source service
#Source:         https://gitlab.com/rastersoft/desktop-icons-ng/uploads/eaa0b5e8e61258bd108897fc2fbd2da2/ding-%{version}.tar.rst
Source:         ding-%{version}.tar.zst

# Needed for directory ownership
BuildRequires:  gnome-shell >= 45
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 0.44.0
Requires:       gnome-shell
Requires:       nautilus >= 45

%description
This package provides a GNOME Shell extension for showing the contents
of ~/Desktop on the desktop of the Shell. Common file management
operations such as launching, copy/paste, rename and deleting are
supported.

%prep
%autosetup -n ding-%{version}

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
%config %{_sysconfdir}/apparmor.d/desktop-icons-ng

%changelog
