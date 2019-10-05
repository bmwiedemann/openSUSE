#
# spec file for package xdg-dbus-proxy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Bjørn Lie, Bryne, Norway.
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


Name:           xdg-dbus-proxy
Version:        0.1.2
Release:        0
Summary:        Filtering proxy for D-Bus connections
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://github.com/flatpak/xdg-dbus-proxy
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

%description
xdg-dbus-proxy is a filtering proxy for D-Bus connections. It was
originally part of the flatpak project, but it has been broken out
as a standalone module to facilitate using it in other contexts.

%prep
%autosetup -p1

%build
%configure \
	%{nil}
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS
%{_bindir}/xdg-dbus-proxy
%{_mandir}/man1/xdg-dbus-proxy.1%{ext_man}

%changelog
