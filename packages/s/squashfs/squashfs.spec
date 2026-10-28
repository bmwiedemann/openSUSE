#
# spec file for package squashfs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if %{?suse_version} > 1315
%define _lz4_def LZ4_SUPPORT=1
BuildRequires:  pkgconfig(liblz4)
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
%define _zstd_def ZSTD_SUPPORT=1
BuildRequires:  pkgconfig(libzstd)
%endif
Name:           squashfs
Version:        4.7.5
Release:        0
Summary:        A Read-Only File System with Efficient Compression
License:        GPL-2.0-or-later
URL:            https://github.com/plougher/squashfs-tools
Source0:        https://github.com/plougher/squashfs-tools/archive/refs/tags/%{version}.tar.gz
Patch0:         squashfs-64k.patch
Patch1:         squashfs-thread-limit
BuildRequires:  help2man
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(zlib)
Supplements:    filesystem(squashfs)

%description
This package contains the userland utilities to create and read
squashfs images.

%prep
%autosetup -p1 -n squashfs-tools-%{version}

%build
%define _lto_cflags %{nil}
sed -i -e "s|-O2|%{optflags}|" squashfs-tools/Makefile
%make_build -C squashfs-tools \
	LZMA_XZ_SUPPORT=1 XZ_SUPPORT=1 LZO_SUPPORT=1 %{?_lz4_def} %{?_zstd_def}

%install
make -C squashfs-tools install \
	INSTALL_PREFIX=%{buildroot}%{_prefix} \
	INSTALL_MANPAGES_DIR=%{buildroot}%{_mandir}/man1

%files
%license COPYING
%doc README.md ACKNOWLEDGEMENTS CHANGES.md
%{_bindir}/sqfs*
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
%{_mandir}/man1/*

%changelog
