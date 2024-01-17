#
# spec file for package squashfuse
#
# Copyright (c) 2021 SUSE LLC
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


%define so_version 0
Name:           squashfuse
Version:        0.5.0
Release:        0
Summary:        FUSE module to mount squashfs images
License:        BSD-2-Clause
Group:          System/Filesystems
URL:            https://github.com/vasi/squashfuse
Source:         https://github.com/vasi/squashfuse/releases/download/v%{version}/squashfuse-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(fuse)
BuildRequires:  gcc
BuildRequires:  libattr-devel
#BuildRequires:  liblzma5
BuildRequires:  libtool
BuildRequires:  pkgconfig(fuse)
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(zlib)
Requires:       fuse

%description
Squashfuse is a FUSE filesystem that allows a
squashfs archive to be mounted in user-space.
It is designed to be fast and memory-efficient,
and supports most of the features of the squashfs format.

%package -n libsquashfuse%{so_version}
Summary:        FUSE module to mount squashfs images

%description -n libsquashfuse%{so_version}
Squashfuse is a FUSE filesystem that allows a
squashfs archive to be mounted in user-space.
It is designed to be fast and memory-efficient,
and supports most of the features of the squashfs format.

%package tools
Summary:        Squafs Tools for squashfsfuse

%description tools
Demo tools from squashfsfuse package to list and extract files from a
squashfs file system (no man pages).

%package devel
Summary:        FUSE module to mount squashfs images
Group:          Development/Languages/C and C++
Requires:       libsquashfuse%{so_version} = %{version}

%description devel
Squashfuse is a FUSE filesystem that allows a
squashfs archive to be mounted in user-space.
It is designed to be fast and memory-efficient,
and supports most of the features of the squashfs format.

This package contains development files.

%prep
%setup -q

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_includedir}/squashfuse
cp *.h -v %{buildroot}%{_includedir}/squashfuse
sed -e 's,^#include ",#include "squashfuse/,' \
    %{buildroot}%{_includedir}/squashfuse/squashfuse.h \
  > %{buildroot}%{_includedir}/squashfuse.h
sed -i 's,^Libs: \(.*\),Libs: \1 -llzo2,' \
    %{buildroot}%{_libdir}/pkgconfig/squashfuse.pc
find %{buildroot} -type f \( -name "*.a" -o -name "*.la" \) -delete -print
pwd
install -m 0755 .libs/squashfuse_ls .libs/squashfuse_extract %{buildroot}/%{_bindir}

%fdupes %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_libdir}

%post -n libsquashfuse%{so_version} -p /sbin/ldconfig
%postun -n libsquashfuse%{so_version} -p /sbin/ldconfig

%files
%{_mandir}/*/*
%license LICENSE
%{_bindir}/squashfuse
%{_bindir}/squashfuse_ll

%files tools
%{_bindir}/squashfuse_ls
%{_bindir}/squashfuse_extract

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/squashfuse
%{_includedir}/squashfuse.h

%files -n libsquashfuse%{so_version}
%{_libdir}/libsquashfuse.so.%{so_version}
%{_libdir}/libsquashfuse.so.%{so_version}.*
%{_libdir}/libsquashfuse_ll.so.%{so_version}
%{_libdir}/libsquashfuse_ll.so.%{so_version}.*

%changelog
