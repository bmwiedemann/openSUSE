#
# spec file for package fastfetch
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


Name:           fastfetch
Version:        1.7.5
Release:        0
Summary:        Neofetch-like tool written in C
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/LinusDierheimer/fastfetch
Source:         https://github.com/LinusDierheimer/fastfetch/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
Recommends:     ImageMagick
Recommends:     Mesa
Recommends:     chafa
Recommends:     dbus-1
Recommends:     dconf
Recommends:     glib2-tools
Recommends:     pciutils
Recommends:     rpm
Recommends:     sqlite3
Recommends:     vulkan-tools
Recommends:     xfconf
Recommends:     xrandr
Recommends:     zlib

%description
Fastfetch is a neofetch-like tool for fetching system information and displaying them in a pretty way.
It is written in pure c, with performance and customizability in mind. Currently Linux, Android, FreeBSD,
MacOS and Windows 7+ are supported.

%prep
%setup -q

sed -i "s|\#\!\/usr\/bin\/env bash||g" completions/bash

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/flashfetch
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.conf
%{_datadir}/%{name}/
%{_datadir}/bash-completion/

%changelog
