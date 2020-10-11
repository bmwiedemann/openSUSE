#
# spec file for package fuse3
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


Name:           fuse3
Version:        3.10.0
Release:        0
Summary:        Reference implementation of the "Filesystem in Userspace"
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause
Group:          System/Filesystems
URL:            https://github.com/libfuse/libfuse
Source:         https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.xz
Source1:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.xz.asc
Source2:        fuse.keyring
Source1000:     baselibs.conf
Patch1:         conf-rename.patch
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
Requires:       util-linux >= 2.18
Requires(pre):  group(trusted)
Requires(pre):  permissions
Supplements:    filesystem(fuse)

%description
With FUSE, a user space program can export a file system to the
Linux kernel.

After installing fuse-devel, administrators can compile and install
other user space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%package -n libfuse3-3
Summary:        Library of FUSE, the User space File System for GNU/Linux and BSD
Group:          System/Filesystems

%description -n libfuse3-3
With FUSE, a user space program can export a file system to the
Linux kernel.

After installing fuse-devel, administrators can compile and install
other user space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%package doc
Summary:        Documentation for the FUSE library version 3
Group:          Documentation/HTML

%description doc
This package contains the documentation for FUSE (userspace filesystem).

%package devel
Summary:        Development package for FUSE (userspace filesystem) modules
Group:          Development/Languages/C and C++
Requires:       fuse3 = %{version}
Requires:       glibc-devel
Requires:       libfuse3-3 = %{version}

%description devel
This package contains all include files, libraries and configuration
files needed to develop programs that use the fuse (FUSE) library to
implement file systems in user space.

With fuse-devel, administrators can compile and install other user
space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%prep
%setup -q -n fuse-%{version}
%patch1 -p1

%build
%define _lto_cflags %{nil}
%meson -Duseroot=false
%meson_build

%install
%meson_install

find %{buildroot} -type f -name "*.la" -delete -print

mkdir %{buildroot}/sbin
mkdir %{buildroot}/%{_lib}
ln -s -v %{_sbindir}/mount.fuse3 %{buildroot}/sbin
pushd %{buildroot}/%{_libdir}
for libname in $(ls *.so.*);do
ln -s -v /%{_libdir}/$libname %{buildroot}/%{_lib}
done
popd

# Remove unneeded stuff
rm -r %{buildroot}%{_prefix}/lib/udev
rm -r %{buildroot}%{_initddir}

%fdupes -s doc

%post
%set_permissions %{_bindir}/fusermount3

%verifyscript
%verify_permissions -e %{_bindir}/fusermount3

%post -n libfuse3-3 -p /sbin/ldconfig
%postun -n libfuse3-3 -p /sbin/ldconfig

%files
%license LICENSE GPL2.txt LGPL2.txt
%doc AUTHORS ChangeLog.rst
%verify(not mode) %attr(4750,root,trusted) %{_bindir}/fusermount3
/sbin/mount.fuse3
%{_sbindir}/mount.fuse3
%config %{_sysconfdir}/fuse3.conf
%{_mandir}/man1/fusermount3.1%{?ext_man}
%{_mandir}/man8/mount.fuse3.8%{?ext_man}

%files -n libfuse3-3
/%{_lib}/libfuse3.so.3*
%{_libdir}/libfuse3.so.3*

%files doc
%doc example doc

%files devel
%{_libdir}/libfuse3.so
%{_includedir}/fuse3/*.h
%{_includedir}/fuse3
%{_libdir}/pkgconfig/*.pc

%changelog
