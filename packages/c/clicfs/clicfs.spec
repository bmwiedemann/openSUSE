#
# spec file for package clicfs
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           clicfs
Version:        1.4.6
Release:        0
Summary:        Compressed Loop Image Container
License:        GPL-2.0
Group:          System/Filesystems
Source:         clicfs.tar.bz2
BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  xz-devel
Requires:       fuse
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Clic FS is a FUSE file system to mount a Compressed Loop Image
Container. It has several features that make it a good choice for live
systems. It will compress a Loop Image and export it as read write,
creating a copy on write behaviour.

%prep
%setup -c %{name}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 .

%install
%make_install

%files
%defattr(-,root,root)
%doc LICENCE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
