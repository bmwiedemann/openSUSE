#
# spec file for package wlcs
#
# Copyright (c) 2024 mantarimay
# Copyright (c) 2024 Shawn W Dunn
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


Name:           wlcs
Version:        1.7.0
Release:        0
Summary:        Wayland Conformance Test Suite
License:        GPL-3.0-only AND GPL-2.0-only
URL:            https://github.com/canonical/wlcs
Source:         %{url}/releases/download/v%{version}/wlcs-%{version}.tar.xz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock
BuildRequires:  pkg-config
BuildRequires:  gtest
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

%description
wlcs is a protocol conformance verifying test suite usable by Wayland
compositor implementors.

wlcs relies on compositors providing an integration module, providing
wlcs with API hooks to start a compositor, connect a client, move a
window, and so on.

Tests (generally) run in the same address space as the compositor, so
there is a consistent global clock available, it is convenient to
poke around in compositor internals, and standard debugging tools can
follow control flow from the test client to the compositor and back
again.

%package        devel
Summary:        Development files for wlcs
Requires:       wlcs = %{version}

%description    devel
wlcs is a protocol conformance verifying test suite usable by Wayland
compositor implementors.

The wlcs-devel package contains header files for developing
Wayland compositor tests that use wlcs.

%prep
%autosetup -p1
# -Werror makes sense for upstream CI, but is too strict for packaging
sed -r -i 's/-Werror //' CMakeLists.txt
echo 'include_directories("/usr/include/wayland")' >> CMakeLists.txt

%build
%cmake %ifarch %{ix86} -DWLCS_BUILD_TSAN=OFF %endif

%install
%cmake_install

%check
%ctest

%files
%license COPYING.*
%doc README.rst
%{_libexecdir}/wlcs/

%files devel
%doc README.rst
%doc example/
%{_includedir}/wlcs/
%{_libdir}/pkgconfig/wlcs.pc

%changelog
