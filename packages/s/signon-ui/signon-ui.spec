#
# spec file for package signon-ui
#
# Copyright (c) 2024 SUSE LLC
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


Name:           signon-ui
Version:        0.17.20231016T221200~eef943f
Release:        0
Summary:        Single Sign On UI
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://gitlab.com/accounts-sso/signon-ui
Source:         %{name}-%{version}.tar.xz
# Patches for upstream, but upstream is dead
Patch0:         0001-Fix-WebEngine-cache-directory-path.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6WebEngineQuick)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(accounts-qt6)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libsignon-qt6)
BuildRequires:  pkgconfig(signon-plugins-common)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires:       qt6-webchannel-imports
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 aarch64 riscv64

%description
This package contains the user interface for the signond Single Sign On service.

%prep
%autosetup -p1

# Don't build tests
sed -i '/tests/d' signon-ui.pro

# Fix libdir
sed -i 's#/lib#/%{_lib}#g' common-installs-config.pri

%build
%qmake6

%qmake6_build

%install
%qmake6_install

# The .desktop file is useless
rm -r %{buildroot}%{_datadir}/applications

%files
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/com.canonical.indicators.webcredentials.service
%{_datadir}/dbus-1/services/com.nokia.singlesignonui.service

%changelog
