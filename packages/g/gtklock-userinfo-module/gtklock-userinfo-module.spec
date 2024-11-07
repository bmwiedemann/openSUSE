#
# spec file for package gtklock-userinfo-module
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


Name:           gtklock-userinfo-module
Version:        4.0.0
Release:        0
Summary:        Module for gtklock which adds user info to the lockscreen
License:        GPL-3.0-only
URL:            https://github.com/jovanlanik/gtklock-userinfo-module
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM smolsheep@opensuse.org -- Fix crash when unlocking session
Patch0:         fix-unlock-crashing.patch
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(accountsservice)

%description
Adds a user image and user name to the lockscreen.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%dir %{_libdir}/gtklock/
%{_libdir}/gtklock/userinfo-module.so

%changelog
