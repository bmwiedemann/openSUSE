#
# spec file for package systemd-ui
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


Name:           systemd-ui
Url:            http://www.freedesktop.org/wiki/Software/systemd
Version:        3
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  vala-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(dbus-1) >= 1.3.2
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) > 2.26
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
Summary:        Graphical front-end for systemd
License:        GPL-2.0+
Group:          System/Base
Requires:       systemd
Obsoletes:      systemd-gtk <= 44
Provides:       systemd-gtk
Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz

# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.
# PATCH-FIX-UPSTREAM systemd-ui-notification-clarification.patch dimstar@opensuse.org -- Fix ambiguity between `GLib.Notification' and `Notify.Notification'
Patch0:         systemd-ui-notification-clarification.patch

%description
Graphical front-end for systemd system and service manager.

%prep
%setup -q
%patch0 -p1

%build
export V=1
%configure \
  CFLAGS="%{optflags}"

make %{?_smp_mflags}

%install
%makeinstall
%suse_update_desktop_file systemadm -r System Monitor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.1*
%{_datadir}/applications/*.desktop

%changelog
