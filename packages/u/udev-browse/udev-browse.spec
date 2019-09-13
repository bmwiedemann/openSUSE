#
# spec file for package udev-browse
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           udev-browse
Version:        0.3
Release:        0
Summary:        A Udev browsing tool
License:        LGPL-2.1+
Group:          System/GUI/GNOME
Url:            http://0pointer.de/blog/projects/udev-browse.html
Source:         http://0pointer.de/public/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix-gee.patch fcrozat@suse.com -- fix build with latest vala/libgee
Patch0:         fix-gee.patch
# PATCH-FIX-UPSTREAM udev-browse-ListStore.patch dimstar@opensuse.org -- `ListStore' is an ambiguous reference between `GLib.ListStore' and `Gtk.ListStore'
Patch1:         udev-browse-ListStore.patch
BuildRequires:  gtk3-devel
BuildRequires:  libgee-devel
BuildRequires:  libgudev-1_0-devel
BuildRequires:  vala
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
It's easy to get lost in /sys and not much fun typing long udevadm info command lines all the time. 
This is a little UI for exploring the udev/sysfs tree: udev-browse. 
This provides a little bit simpler access to the device tree


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make udev-browse

%install
install -D -m755 udev-browse %buildroot/usr/bin/udev-browse

%files
%defattr(-,root,root)
/usr/bin/udev-browse

%doc LGPL

%changelog
