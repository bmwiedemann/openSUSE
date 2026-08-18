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

%define major_ver 0.11
%define minor_ver 2
Name:           wayfire-plugins-extra
Version:        %{major_ver}.%{minor_ver}
Release:        0
Summary:        Additional plugins for Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
# meson subprojects vendored from upstream wrap files (git master), pinned by commit
Source2:        wayfire-shadows-4bfdbbf.tar.xz
Source3:        focus-request-b5c5029.tar.xz
Source4:        pixdecor-a9465be.tar.xz
Source5:        filters-8fcaad8.tar.xz
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libboost_atomic-devel
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(wayfire) >= %{major_ver}
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(nlohmann_json)
Requires:       wayfire >= %{major_ver}

%description
Additional plugins for Wayfire
The plugins that come here are plugins that have external dependencies, for ex. giomm.

%lang_package

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1
mkdir -p subprojects
tar -xJf %{SOURCE2} -C subprojects
tar -xJf %{SOURCE3} -C subprojects
tar -xJf %{SOURCE4} -C subprojects
tar -xJf %{SOURCE5} -C subprojects
rm -f subprojects/*.wrap
# upstream ships locale/ro/wf-plugin-fisheye.po outside LC_MESSAGES, which makes
# meson install it to a bogus /usr/share/locale/LC_MESSAGES path
mv locale/ro/wf-plugin-fisheye.po locale/ro/LC_MESSAGES/

%build
%meson \
 -Dpixdecor=true \
 -Dfilters=true \
 -Dwayfire_shadows=true \
 -Dfocus_request=true
%meson_build

%install
%meson_install
%find_lang %{name} --all-name

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/wayfire/*.so
%{_datadir}/wayfire/metadata/*.xml

%files lang -f %{name}.lang

%changelog
