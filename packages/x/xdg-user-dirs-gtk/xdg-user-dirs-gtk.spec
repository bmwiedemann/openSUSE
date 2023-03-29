#
# spec file for package xdg-user-dirs-gtk
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


Name:           xdg-user-dirs-gtk
Version:        0.11
Release:        0
Summary:        Xdg-user-dir support for Gnome and Gtk+ applications
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://download.gnome.org/sources/xdg-user-dirs-gtk
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM xdg-user-dirs-gtk-XFCE-LXDE-autostart.patch fdo#33107 gber@opensuse.org -- Start xdg-user-dirs-gtk in Xfce sessions as well
Patch1:         %{name}-XFCE-autostart.patch

BuildRequires:  gnome-common
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  xdg-user-dirs
Requires:       xdg-user-dirs

%description
A companion to xdg-user-dirs that integrates it into the Gnome desktop
and Gtk+ applications. Presents a dialog when a user changes locales
to help move they standard user directories to the correct names.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
export CFLAGS='%{optflags} -Wno-error=deprecated-declarations -Wno-error=cast-align'
%configure
%make_build

%install
%make_install
%suse_update_desktop_file user-dirs-update-gtk
%find_lang %{name}

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS README ChangeLog
%{_bindir}/xdg-user-dirs-gtk-update
%{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop

%files lang -f %{name}.lang

%changelog
