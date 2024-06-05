#
# spec file for package lite-xl-plugin-manager
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

%define baseprogramname lite-xl
Name:           lite-xl-plugin-manager
Version:        1.2.9+git20240603.5343f48
Release:        0
Summary:        A %{baseprogramname} plugin manager
%if 0%{?suse_version} > 1500
%else
Group:          Productivity/Text/Editors
%endif
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND Zlib AND SUSE-GPL-2.0-with-linking-exception
URL:            https://github.com/lite-xl/lite-xl-plugin-manager
Source:         %{name}-%{version}.tar.gz
Patch0:         lpm.c.diff
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150600
BuildRequires:  mbedtls-2-devel
%else
BuildRequires:  mbedtls-devel
%endif
BuildRequires:  meson
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(lua) >= 5.4
BuildRequires:  pkgconfig(zlib)
Requires:       %{baseprogramname}
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
  the latest branch of this repository, which corresponds to the most recent versioned release.
* Conforms to SCPS3.

%prep
%autosetup -p 0

%build
%meson -Dstatic=true
%meson_build

%install
%ifarch i586
install -D -m 0755 "i586-suse-linux/lpm" "%{buildroot}/%{_bindir}/lpm"
%else
install -D -m 0755 "%{_arch}-suse-linux/lpm" "%{buildroot}/%{_bindir}/lpm"
%endif

%files
%{_bindir}/lpm
%license LICENSE
%doc README.md CHANGELOG.md

%changelog

