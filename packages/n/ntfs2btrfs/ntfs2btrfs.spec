#
# spec file for package ntfs2btrfs
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ntfs2btrfs
Version:        20240115
Release:        0
Summary:        In-place conversion tool from NTFS to BTRFS
License:        GPL-2.0-only
URL:            https://github.com/maharmstone/ntfs2btrfs
Source:         https://github.com/maharmstone/ntfs2btrfs/archive/refs/tags/%{version}.tar.gz
Patch1:         0001-ntfs.h-include-memory.patch
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  zlib-devel

%description
Ntfs2btrfs is a tool which does in-place conversion of Microsoft's NTFS
filesystem to the open-source filesystem Btrfs, much as btrfs-convert does for
ext2. The original image is saved as a reflink copy at image/ntfs.img, and if
you want to keep the conversion you can delete this to free up space.

%prep
%setup -q
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENCE
%doc README.md
%{_sbindir}/ntfs2btrfs
%{_mandir}/man8/ntfs2btrfs.8%{?ext_man}

%changelog
