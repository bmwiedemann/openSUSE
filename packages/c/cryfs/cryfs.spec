#
# spec file for package cryfs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.10.2
Release:        0
Summary:        CryFS encryption
License:        LGPL-3.0-only
Source:         %{name}-%{version}.tar.xz
URL:            https://github.com/cryfs/cryfs

#=================================
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python

%if 0%{?suse_version} < 1500
BuildRequires:  boost-devel => 1.56.0
%else
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%endif

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)
# BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  libcryptopp-devel
BuildRequires:  libopenssl-devel

#=================================

%description
CryFS provides a FUSE-based mount that encrypts file contents, file
sizes, metadata and directory structure. It uses encrypted same-size
blocks to store both the files themselves and the blocks' relations
to one another. These blocks are stored as individual files in the
base directory, which can then be synchronized to remote storage
(using an external tool).

%prep
%setup -c -q

%build
mkdir build
cd build
cmake .. \
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

%make_jobs

%install
%cmake_install

%files
%defattr(0755,root,root)
%{_bindir}/cryfs*
%defattr(0644,root,root)
%{_mandir}/man?/cryfs*
%doc README.md ChangeLog.txt
%license LICENSE.txt

%changelog
