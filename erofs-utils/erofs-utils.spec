#
# spec file for package erofs-utils
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


Name:           erofs-utils
Version:        0.0.1~23
Release:        0
Summary:        Utilities for the Extendable Read-Only Filesystem (EROFS)
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git/
Source:         %name-%version.tar.xz
Source2:        https://github.com/lz4/lz4/archive/v1.8.3.tar.gz#/lz4-1.8.3.tar.gz
Patch1:         no-date.diff
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Supplements:    filesystem(erofs)
# erofs depends on an unstable nonexported API
Provides:       bundled(lz4) = 1.8.3

%description
mkfs.erofs is a user-space tool to create erofs filesystem images. It
can create two main types of erofs images, compressed and
uncompressed:

 * For compressed images, it is able to integrate several compression
   algorithms, LZ4 is supported according to the current erofs kernel
   implementation.
 * For uncompressed images, it can decide whether the last page of a
   file should be inlined or not properly.

%prep
%setup -qa2
%patch -P 1 -p1

%build
pushd lz4-1.8.3/
make %{?_smp_mflags} CFLAGS="%{optflags}" V=1
popd
autoreconf -fiv
export CPPFLAGS="-I$PWD/lz4-1.8.3/lib"
%configure --disable-static --with-lz4-include="$PWD/lz4-1.8.3/lib" \
	--with-lz4-lib="$PWD/lz4-1.8.3/lib" --bindir="%_sbindir"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%_sbindir/mkfs*

%changelog
