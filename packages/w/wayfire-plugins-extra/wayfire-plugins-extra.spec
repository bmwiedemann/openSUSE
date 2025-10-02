#
# spec file for package wayfire-plugins-extra
#
# Copyright (c) 2025 SUSE LLC
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

%define major_ver 0.10
%define minor_ver 0
Name:           wayfire-plugins-extra
Version:        %{major_ver}.%{minor_ver}
Release:        0
Summary:        Additional plugins for Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(wayfire) >= %{major_ver}
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  wlroots-devel >= 0.19.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(nlohmann_json)
Requires:       wayfire >= %{major_ver}

%description
Additional plugins for Wayfire
The plugins that come here are plugins that have external dependencies, for ex. giomm.

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1

%build
%meson \
 -Denable_pixdecor=true \
 -Denable_filters=true \
 -Denable_wayfire_shadows=true \
 -Denable_focus_request=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/wayfire/*.so
%{_datadir}/wayfire/metadata/*.xml

%changelog
