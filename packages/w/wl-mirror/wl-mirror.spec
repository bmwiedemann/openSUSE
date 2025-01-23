#
# spec file for package wl-mirror
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Lorenz Holzbauer
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


Name:           wl-mirror
Version:        0.17.0
Release:        0
Summary:        A Wayland output mirror client
License:        GPL-3.0-or-later
URL:            https://github.com/Ferdi265/wl-mirror
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gpg2
BuildRequires:  pkg-config
BuildRequires:  wayland-protocols-devel >= 1.31
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)

%description
A Wayland output mirror client.
It mirrors (in the sense of copying, not swapping left↔right) an
output onto a new resizable window.

%prep
%autosetup
rm -rf proto/wayland-protocols

%build
%cmake \
    -DFORCE_SYSTEM_WL_PROTOCOLS:BOOL=ON \
    -DINSTALL_DOCUMENTATION:BOOL=ON \
    -DINSTALL_EXAMPLE_SCRIPTS:BOOL=ON \
    -DWITH_LIBDECOR:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wl-mirror
%{_bindir}/wl-present
%{_mandir}/man1/wl-mirror.1%{?ext_man}
%{_mandir}/man1/wl-present.1%{?ext_man}

%changelog
