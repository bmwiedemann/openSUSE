#
# spec file for package cerbere
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Mihai Petracovici <petracvv@cloverleaf-linux.org>.
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


Name:           cerbere
Version:        2.5.0
Release:        0
Summary:        A service to relaunch Pantheon apps
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://elementary.io/
Source:         https://github.com/elementary/cerbere/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libgee-devel
BuildRequires:  meson >= 0.44.4
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28.0

%description
Cerbere is a sort of a watchdog designed for Pantheon. It monitors a
predefined list of processes (configurable through dconf) and relaunches
them if they end. This is helpful to keep the panel, dock, and wallpaper
running, even if they crash or are killed by another process.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r io.elementary.cerbere System Utility

%files
%license COPYING
%doc README.md
%{_libexecdir}/io.elementary.cerbere
%{_datadir}/glib-2.0/schemas/io.elementary.cerbere.gschema.xml
%{_sysconfdir}/xdg/autostart/io.elementary.cerbere.desktop

%changelog
