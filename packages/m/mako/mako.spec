#
# spec file for package mako
#
# Copyright (c) 2022 SUSE LLC
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


Name:           mako
Version:        1.7.1
Release:        0
Summary:        A Wayland notification daemon
License:        MIT
Group:          System/GUI/Other
URL:            https://mako-project.org/
Source:         https://github.com/emersion/mako/archive/v%{version}.tar.gz
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.21

%description
A notification daemon for Wayland. Intended to be used with sway.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%meson \
  -Dsd-bus-provider=libsystemd

%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/fr.emersion.mako.service
%{_bindir}/%{name}*
%{_mandir}/man?/%{name}*

%changelog
