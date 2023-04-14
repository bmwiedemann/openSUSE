#
# spec file for package cryfs
#
# Copyright (c) 2023 SUSE LLC
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


# disable lto for ppc64
%ifarch ppc64
%define _lto_cflags %{nil}
%endif
Name:           cryfs
Version:        0.11.3
Release:        0
Summary:        Cryptographic filesystem for the cloud
License:        LGPL-3.0-only
URL:            https://www.cryfs.org/
Source:         https://github.com/cryfs/cryfs/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/cryfs/cryfs/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# 0x5D5EC7BC6F1443EC2AF7177A9E6C996C991D25E1
Source2:        %{name}.keyring
Patch:          https://github.com/cryfs/cryfs/commit/38849c22aa34c5fad10091e066a520dd831462b3.patch
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel >= 1.65.1
BuildRequires:  libboost_chrono-devel >= 1.65.1
BuildRequires:  libboost_filesystem-devel >= 1.65.1
BuildRequires:  libboost_program_options-devel >= 1.65.1
BuildRequires:  libboost_system-devel >= 1.65.1
BuildRequires:  libboost_thread-devel >= 1.65.1
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(fuse) >= 2.8.6
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)

%description
CryFS provides a FUSE-based mount that encrypts file contents, file
sizes, metadata and directory structure. It uses encrypted same-size
blocks to store both the files themselves and the blocks' relations
to one another. These blocks are stored as individual files in the
base directory, which can then be synchronized to remote storage
(using an external tool).

%prep
%autosetup -c -p1

%build
mkdir build
cd build
# FIXME: you should use the %%cmake macros
cmake .. \
	-DDEPENDENCY_CONFIG=../cmake-utils/DependenciesFromLocalSystem.cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_CXX_FLAGS="%{optflags} -fPIC" \
	-DCMAKE_C_FLAGS="%{optflags} -fPIC" \
	-DBoost_USE_STATIC_LIBS=OFF \
	-DBUILD_TESTING=OFF \
	-DCRYFS_UPDATE_CHECKS=OFF \
%ifarch %{ix86} x86_64
 	-DCMAKE_CXX_FLAGS="-msse4.1" \
%endif
	-DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md ChangeLog.txt
%{_bindir}/cryfs*
%{_mandir}/man?/cryfs*

%changelog
