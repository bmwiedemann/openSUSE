#
# spec file for package avfs
#
# Copyright (c) 2023 SUSE LLC
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


Name:           avfs
Version:        1.1.5
Release:        0
Summary:        AVFS - an archive look-inside filesystem
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://avf.sourceforge.net/
Source0:        https://downloads.sf.net/avf/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sf.net/avf/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  emacs-nox
BuildRequires:  help2man
BuildRequires:  lzlib-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(openssl)

%description
AVFS is a filesystem which enables all programs to look inside archived or
compressed files, or access remote files without recompiling the programs
or changing the kernel.

%package devel
Summary:        Development files for AVFS, an archive look-inside filesystem
Requires:       libavfs0 = %{version}

%description devel
This package includes the development file for the package avfs.
AVFS is a filesystem which enables all programs to look inside archived or
compressed files, or access remote files without recompiling the programs
or changing the kernel.

%package -n libavfs0
Summary:        Shared library for AVFS, an archive look-inside filesystem

%description -n libavfs0
This package includes the runtime shared library for the package avfs.
AVFS is a system, which enables all programs to look inside archived or
compressed files, or access remote files without recompiling the programs
or changing the kernel.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --enable-fuse \
  --enable-library \
  --enable-shared \
  --with-system-zlib \
  --with-system-bzlib \
  --with-lzip \
  --with-lzma \
  --with-xz
%make_build

%install
%make_install

pushd %{buildroot}%{_libdir}/%{name}/extfs/
    mv uzip ext-uzip
popd
mkdir -p %{buildroot}/%{_mandir}/man1/
pushd %{buildroot}/%{_mandir}/man1/
    LD_LIBRARY_PATH=%{buildroot}/%{_libdir} \
    PATH=%{buildroot}/%{_bindir}:$PATH \
    help2man -s 1 -N --no-discard-stderr avfsd | \
    sed 's/^FUSE \\- .*/AVFS - A Virtual File System/' > \
    avfsd.1
popd

rm -vf %{buildroot}/%{_libdir}/libavfs.la

%post -n libavfs0 -p /sbin/ldconfig
%postun -n libavfs0 -p /sbin/ldconfig

%files
%doc ChangeLog README NEWS TODO
%license COPYING
%doc doc/api-overview
%doc doc/background
%doc doc/FORMAT
%doc doc/README.avfs-fuse
%{_bindir}/avfsd
%{_bindir}/davpass
%{_bindir}/ftppass
%{_bindir}/mountavfs
%{_bindir}/umountavfs
%dir %{_libdir}/avfs
%dir %{_libdir}/avfs/extfs
%{_libdir}/avfs/extfs/*
%{_mandir}/man1/avfsd.1%{?ext_man}

%files devel
%{_bindir}/avfs-config
%{_includedir}/avfs.h
%{_includedir}/virtual.h
%{_libdir}/libavfs.so
%{_libdir}/pkgconfig/avfs.pc

%files -n libavfs0
%{_libdir}/libavfs.so.0
%{_libdir}/libavfs.so.0.0.2

%changelog
