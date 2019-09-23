#
# spec file for package unionfs-fuse
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           unionfs-fuse
BuildRequires:  cmake
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  libattr-devel
Requires:       fuse
Summary:        Userspace Unionfs File System
License:        BSD-3-Clause
Group:          System/Filesystems
Version:        1.0
Release:        0
Source:         https://github.com/rpodgorny/unionfs-fuse/archive/v%{version}.tar.gz
Url:            https://github.com/rpodgorny/unionfs-fuse
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
unionfs-fuse overlays several directory into one single mount point

It  first  tries to access the file on the top branch and if the file
does not exist there, it continues on lower level branches. If the user
tries to modify a file on a lower level read-only branch the file is
copied to to a higher level read-write branch if the copy-on-write
(cow) mode was enabled.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS=$CFLAGS 
cmake -DCMAKE_INSTALL_PREFIX=/usr -DWITH_XATTR=1 .
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc LICENSE CREDITS NEWS
%{_mandir}/man?/*
%{_bindir}/unionfs
%{_bindir}/unionfsctl

%changelog
