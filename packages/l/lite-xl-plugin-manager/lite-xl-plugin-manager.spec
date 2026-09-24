#
# spec file for package lite-xl-plugin-manager
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define baseprogramname lite-xl
Name:           lite-xl-plugin-manager
Version:        1.4.9
Release:        0
Summary:        A %{baseprogramname} plugin manager
# Legal-Review-Notice: v1.4.9 GitHub tarball ships LPM and vendored microtar (both MIT). Previous Apache-2.0/BSD-3-Clause/Zlib/SUSE-GPL-2.0-with-linking-exception covered obs_scm git submodules meson does not link.
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-plugin-manager
Source0:        https://github.com/lite-xl/lite-xl-plugin-manager/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      README.md
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(lua) >= 5.4
BuildRequires:  pkgconfig(zlib)
Requires:       %{baseprogramname}
# TW mbedtls-devel is v4; this code still needs the v3 API (mbedtls-3-devel).
# Leap 16.x mbedtls-devel is still v3.
%if 0%{?suse_version} == 1699
BuildRequires:  mbedtls-3-devel
%else
BuildRequires:  mbedtls-devel
%endif
# This can be managed by 'lite-xl-plugin-manager' (lpm)
#Requires:       lite-xl-widgets

%description
* A standalone binary that provides an easy way of installing, and uninstalling
  plugins from lite-xl, as well as different version of lite-xl.
* Can be used by a package manager plugin that works from inside the editor and
  calls this binary.
* Also contains a plugin_manager.lua plugin to integrate the binary with lite
  in the form of an easy-to-use GUI.
* By default in releases, lpm will automatically consume the manifest.json in
  the latest branch of this repository, which corresponds to the most recent
  versioned release.
* Conforms to SCPS3.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -DLPM_VERSION='\"%{version}\"'"
%meson -Dstatic=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/lpm

%changelog
