#
# spec file for package unionfs-fuse
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           unionfs-fuse
Version:        3.6
Release:        0
Summary:        Userspace Unionfs File System
License:        BSD-3-Clause
URL:            https://github.com/rpodgorny/unionfs-fuse
Source:         https://github.com/rpodgorny/unionfs-fuse/archive/v%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)
Requires:       fuse3
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libattr)
%else
BuildRequires:  libattr-devel
%endif

%description
unionfs-fuse overlays several directory into one single mount point

It  first  tries to access the file on the top branch and if the file
does not exist there, it continues on lower level branches. If the user
tries to modify a file on a lower level read-only branch the file is
copied to to a higher level read-write branch if the copy-on-write
(cow) mode was enabled.

%prep
%autosetup -p1

%build
%cmake -DWITH_XATTR=1
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc CREDITS NEWS
%{_mandir}/man8/unionfs.8%{?ext_man}
%{_bindir}/unionfs
%{_bindir}/unionfsctl
%{_sbindir}/mount.unionfs

%changelog
