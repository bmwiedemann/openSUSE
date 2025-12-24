#
# spec file for package cryfs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# https://www.cryptopp.com/wiki/Link_Time_Optimization
# see also -DCRYPTOPP_DISABLE_ASM=ON below
#%%define _lto_cflags %%{nil}
%bcond_without  tests
Name:           cryfs
Version:        1.0.3
Release:        0
Summary:        Cryptographic filesystem for the cloud
License:        LGPL-3.0-only
URL:            https://www.cryfs.org/
Source0:        https://github.com/cryfs/cryfs/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/cryfs/cryfs/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# 0x5D5EC7BC6F1443EC2AF7177A9E6C996C991D25E1
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM fix-feature-fuse3.patch -- based on branch feature/fuse3
Patch2:         fix-feature-fuse3.patch
BuildRequires:  cmake >= 3.25
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel-impl >= 1.84.0
BuildRequires:  libboost_chrono-devel-impl >= 1.84.0
BuildRequires:  libboost_filesystem-devel-impl >= 1.84.0
BuildRequires:  libboost_program_options-devel-impl >= 1.84.0
BuildRequires:  libboost_thread-devel-impl >= 1.84.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(fuse3) >= 3.9.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)
# system cryptopp lib cannot currently be used.
# see also https://github.com/cryfs/cryfs/issues/369
Provides:       bundled(libcryptopp) = 8.9.0
%if %{with tests}
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
%endif

%description
CryFS provides a FUSE-based mount that encrypts file contents, file
sizes, metadata and directory structure. It uses encrypted same-size
blocks to store both the files themselves and the blocks' relations
to one another. These blocks are stored as individual files in the
base directory, which can then be synchronized to remote storage
(using an external tool).

%prep
%autosetup -c -p1

# install man pages also with default build type
sed -e '/Release/d' -i doc/CMakeLists.txt

%build
%define __builder ninja
%cmake \
%ifarch %{arm32} %{ix86} ppc64 ppc64le s390x
	-DCRYPTOPP_DISABLE_ASM=ON \
%endif
%if %{with tests}
	-DBUILD_TESTING=ON \
%endif
	-DBUILD_SHARED_LIBS=OFF \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
	-DCRYFS_UPDATE_CHECKS=OFF
%cmake_build

%install
%cmake_install

%check
export PATH=%{buildroot}%{_bindir}:$PATH
cryfs --version
%if %{with tests}
pushd build/test
./blobstore/blobstore-test
./blockstore/blockstore-test
#./cpp-utils/cpp-utils-test
%ifnarch %{ix86} ppc64 ppc64le
./cryfs/cryfs-test --gtest_filter='-CryConfigCompatibilityTest.*'
%endif
%ifnarch riscv64
./cryfs-cli/cryfs-cli-test --gtest_filter='-CliTest.*:CliTest_Unmount.*'
%endif
#./fspp/fspp-test
./gitversion/gitversion-test
./parallelaccessstore/parallelaccessstore-test
popd
%endif

%files
%license LICENSE.txt
%doc README.md ChangeLog.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-unmount
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-unmount.1%{?ext_man}

%changelog
