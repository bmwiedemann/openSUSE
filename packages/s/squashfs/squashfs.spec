#
# spec file for package squashfs
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


Name:           squashfs
Version:        4.6.1
Release:        0
Summary:        A Read-Only File System with Efficient Compression
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/plougher/squashfs-tools
Source0:        https://github.com/plougher/squashfs-tools/archive/refs/tags/%{version}.tar.gz
Patch0:         squashfs-64k.patch
Patch1:         squashfs-thread-limit
BuildRequires:  help2man
BuildRequires:  lzma-devel
BuildRequires:  lzo-devel
BuildRequires:  zlib-devel
Supplements:    filesystem(squashfs)
%if %{?suse_version} > 1315
BuildRequires:  liblz4-devel
%define _lz4_def LZ4_SUPPORT=1
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
BuildRequires:  libzstd-devel
%define _zstd_def ZSTD_SUPPORT=1
%endif

%description
This package contains the userland utilities to create and read
squashfs images.

%prep
%autosetup -p1 -n squashfs-tools-%{version}

%build
%define _lto_cflags %{nil}
sed -i -e "s|-O2|%{optflags}|" squashfs-tools/Makefile
make %{?_smp_mflags} -C squashfs-tools \
	LZMA_XZ_SUPPORT=1 XZ_SUPPORT=1 LZO_SUPPORT=1 %{?_lz4_def} %{?_zstd_def}

%install
make -C squashfs-tools install \
	INSTALL_PREFIX=%{buildroot}%{_prefix} \
	INSTALL_MANPAGES_DIR=%{buildroot}%{_mandir}/man1

%files
%license COPYING
%doc README-%{version} ACKNOWLEDGEMENTS CHANGES USAGE-4.6
%{_bindir}/sqfs*
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
%{_mandir}/man1/*

%changelog
