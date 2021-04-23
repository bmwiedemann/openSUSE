#
# spec file for package squashfs
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.4
Release:        0
Summary:        A Read-Only File System with Efficient Compression
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            http://squashfs.sourceforge.net/
Source0:        http://sourceforge.net/projects/squashfs/files/squashfs/%{name}%{version}/%{name}%{version}.tar.gz
Patch0:         squashfs-64k.patch
Patch1:         squashfs-thread-limit
%if %{?suse_version} > 1315
BuildRequires:  liblz4-devel
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
BuildRequires:  libzstd-devel
%endif
BuildRequires:  lzma-devel
BuildRequires:  lzo-devel
BuildRequires:  zlib-devel
Supplements:    filesystem(squashfs)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the userland utilities to create and read
squashfs images.

%prep
%setup -q -n squashfs%{version}
%patch0 -p1
%patch1 -p1

%build
%define _lto_cflags %{nil}
sed -i -e "s|-O2|%{optflags} -fcommon|" squashfs-tools/Makefile
make %{?_smp_mflags} -C squashfs-tools XZ_SUPPORT=1 LZO_SUPPORT=1 \
%if %{?suse_version} > 1315
   LZ4_SUPPORT=1 \
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
   ZSTD_SUPPORT=1
%endif

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 squashfs-tools/{un,mk}squashfs %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc README-%{version} ACKNOWLEDGEMENTS CHANGES COPYING USAGE
%{_bindir}/*squashfs

%changelog
