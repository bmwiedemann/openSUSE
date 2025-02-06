#
# spec file for package xdg-user-dirs-gtk
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


Name:           xdg-user-dirs-gtk
Version:        0.14
Release:        0
Summary:        Xdg-user-dir support for Gnome and Gtk+ applications
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://download.gnome.org/sources/xdg-user-dirs-gtk
Source0:        %{name}-%{version}.tar.zst
# PATCH-FIX-UPSTREAM xdg-user-dirs-gtk-XFCE-LXDE-autostart.patch fdo#33107 gber@opensuse.org -- Start xdg-user-dirs-gtk in Xfce sessions as well
Patch1:         %{name}-XFCE-autostart.patch

BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 1.0
BuildRequires:  pkgconfig
BuildRequires:  xdg-user-dirs
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       xdg-user-dirs

%description
A companion to xdg-user-dirs that integrates it into the Gnome desktop
and Gtk+ applications. Presents a dialog when a user changes locales
to help move they standard user directories to the correct names.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/user-dirs-update-gtk.desktop

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_bindir}/xdg-user-dirs-gtk-update
%config(noreplace) %{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
%{_datadir}/applications/user-dirs-update-gtk.desktop

%files lang -f %{name}.lang

%changelog
