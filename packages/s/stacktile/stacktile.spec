#
# spec file for package stacktile
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

Name:           stacktile
Version:        1.0.0+git26
Release:        0
Summary:        A layour generator for the river Wayland compositor
License:        GPL-3.0-only
URL:            https://git.sr.ht/~uncomfy/stacktile
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  zig >= 0.13.0
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  zstd
Recommends:     river

%description
stacktile is a layout generator for the river Wayland compositor.

It divides the screen into three areas, the primary area, the secondary area and
the remainder area. The primary and secondary areas are populated by a
configurable amount of windows from the top of the window stack. All remaining
windows will be placed in the remainder area. The windows in these areas are
arranged into a configurable sublayout.

stacktile's layout configuration is individual per tag set. If the
layout values are changed, the change only applies to the currently
focused tag set.

%prep
%autosetup -p1 -a1

# Disable the getVersion function that uses git.
sed -i 's|try getVersion(b)|"%{version}"|g' build.zig

%build
%{zig_build} -Dpie --global-cache-dir vendor/

%install
%{zig_install} -Dpie --global-cache-dir vendor/

%check
%{zig_test}  -Dpie --global-cache-dir vendor/

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
