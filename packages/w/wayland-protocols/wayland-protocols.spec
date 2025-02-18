#
# spec file for package wayland-protocols
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
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


Name:           wayland-protocols
Version:        1.41
Release:        0
Summary:        Wayland protocols that add functionality not available in the core protocol
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://wayland.freedesktop.org
Source:         https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source2:        https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz.sig
Source3:        %{name}.keyring
%if 0%{?suse_version} > 1500
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
%else
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%endif
BuildRequires:  meson >= 0.55.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(wayland-scanner)
BuildArch:      noarch

%description
This package contains Wayland protocols that add functionality not
available in the Wayland core protocol. Such protocols either add
completely new functionality, or extend the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:        Wayland protocols that add functionality not available in the core protocol
Group:          Development/Libraries/C and C++

%description devel
This package contains Wayland protocols that add functionality not
available in the Wayland core protocol. Such protocols either add
completely new functionality, or extend the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-11
export CXX=gcc-11
%endif
%meson
%meson_build

%install
%if 0%{?suse_version} <= 1500
export CC=gcc-11
export CXX=gcc-11
%endif
%meson_install

%check
%meson_test

%files devel
%doc README.md GOVERNANCE.md MEMBERS.md
%license COPYING
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/
%{_includedir}/%{name}/

%changelog
