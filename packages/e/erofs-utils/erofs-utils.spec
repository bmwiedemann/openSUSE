#
# spec file for package erofs-utils
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


Name:           erofs-utils
Version:        1.1
Release:        0
Summary:        Utilities for the Extendable Read-Only Filesystem (EROFS)
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git/

Source:         %name-%version.tar.xz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
Supplements:    filesystem(erofs)
BuildRequires:  liblz4-devel >= 1.9
BuildRequires:  libuuid-devel

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
%autosetup -p1

%build
autoreconf -fiv
%configure --bindir="%_sbindir"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%_sbindir/mkfs*
%_mandir/man1/mkfs*

%changelog
