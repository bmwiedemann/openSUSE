#
# spec file for package cppzmq-devel
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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


Name:           cppzmq-devel
Version:        4.6.0
Release:        0
Summary:        Header-only C++ binding for libzmq
License:        MIT
URL:            https://github.com/zeromq/cppzmq
Source:         https://github.com/zeromq/cppzmq/archive/v%{version}.tar.gz#/cppzmq-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libzmq)
Requires:       pkgconfig(libzmq)

%description
cppzmq is a header-only C++ binding for libzmq.

%prep
%autosetup -n cppzmq-%{version}

%build
%cmake \
    -DCPPZMQ_BUILD_TESTS=OFF \
    -DCPPZMQ_CMAKECONFIG_INSTALL_DIR=%{_libdir}/cmake/cppzmq
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_includedir}/zmq.hpp
%{_includedir}/zmq_addon.hpp
%{_libdir}/cmake/cppzmq/

%changelog
