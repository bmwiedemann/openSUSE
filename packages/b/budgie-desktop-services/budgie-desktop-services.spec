#
# spec file for package budgie-desktop-services
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Callum Farmer <gmbr3@opensuse.org>
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

%define org org.buddiesofbudgie.Services
Name:           budgie-desktop-services
Version:        1.0.2+0
Release:        0
Summary:        Wayland-native display configuration for Budgie
License:        MPL-2.0
Group:          System/GUI/Other
URL:            https://forge.moderndesktop.dev/BuddiesOfBudgie/budgie-desktop-services
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  kf6-filesystem
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(toml11)
BuildRequires:  cmake(Qt6WaylandClient)

%description
Budgie Desktop Services is the future central hub and orchestrator for Budgie Desktop (with a focus on Budgie 11).
Today, it primarily provides Wayland-native display configuration for Budgie 10.10; over time it will coordinate broader desktop logic for Budgie 11.

%prep
%autosetup

%build
%cmake_kf6
%kf6_build

%install
%kf6_install

install -Dm0644 %{buildroot}%{_datadir}/dbus-1/system.d/%{org}.conf %{buildroot}%{_datadir}/dbus-1/services/%{org}.conf
rm %{buildroot}%{_datadir}/dbus-1/system.d/%{org}.conf

%files
%license COPYING
%{_bindir}/%{org}
%{_datadir}/dbus-1/services/%{org}.conf

%changelog
