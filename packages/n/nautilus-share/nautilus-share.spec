#
# spec file for package nautilus-share
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


%define         nautilus_extdir %(pkg-config --variable=extensiondir libnautilus-extension-4)
Name:           nautilus-share
Version:        0.7.5
Release:        0
Summary:        Nautilus plugin for sharing directories over SMB
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Samba
URL:            https://git.gnome.org/nautilus-share
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM nautilus-share-lang-fix.patch -- Add LINGUAS file to po dir
Patch:          nautilus-share-lang-fix.patch
# PATCH-FIX-UPSTREAM 5.patch dmulder@suse.com bsc#1208375 -- 'Everyone' represented by WKS 'World' S-1-1-0
Patch2:         https://gitlab.gnome.org/coreyberla/nautilus-share/-/merge_requests/5.patch

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.4.0
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(libnautilus-extension-4) >= 43.rc
Requires:       samba-client >= 3.0.23

%description
An application for the GNOME desktop integrated into Nautilus
which allows use of Nautilus shares without signing in as root.

Features:

* A new command in the Nautilus context menu
  (Menu key or right click).

* A dialog to share a directory, which allows choosing a
  name and decide on read-only/read-write status.

* Possibility to access the share settings from the Properties
  tab of a directory.

* Possibility to examine whether a share name already exists by
  typing it.

* Nautilus displays a palm icon to visually show which
  directories are shared.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS README
%{nautilus_extdir}/libnautilus-share.so
%dir %{_datadir}/interfaces
%{_datadir}/interfaces/share-dialog-gtk4.ui
%{_datadir}/interfaces/share-dialog.ui

%files lang -f %{name}.lang

%changelog
