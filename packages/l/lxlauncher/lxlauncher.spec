#
# spec file for package lxlauncher
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           lxlauncher
Version:        0.2.5
Release:        17
License:        GPL-3.0
Summary:        Open source clone of Asus launcher for Netbooks
Url:            http://www.lxde.org
Group:          System/GUI/LXDE
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gnome-menus-devel
BuildRequires:  intltool
BuildRequires:  menu-cache-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LXLauncher is an open source clone of Asus launcher for
EeePC or Netbooks anyway. It's an LXDE project and it's
based on menu-cache library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
%fdupes -s %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/desktop-directories/
%dir %{_sysconfdir}/xdg/lxlauncher/
%config %{_sysconfdir}/xdg/lxlauncher/gtkrc
%config %{_sysconfdir}/xdg/lxlauncher/settings.conf
%config %{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%{_sysconfdir}/xdg/lxlauncher/gtk.css
%{_mandir}/man1/lxlauncher.1.gz

%changelog
