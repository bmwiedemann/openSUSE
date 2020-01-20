#
# spec file for package libfsapfs
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define experimental_tag experimental-
Name:           libfsapfs
Version:        20191221
Release:        0
Summary:        Library and tools to access the Apple File System (APFS)
License:        LGPL-3.0
Group:          System/Filesystems
Url:            https://github.com/libyal/libfsapfs
Source0:        https://github.com/libyal/%{name}/releases/download/%{version}/%{name}-%{?experimental_tag}%{version}.tar.gz
Source1:        https://github.com/libyal/%{name}/releases/download/%{version}/%{name}-%{?experimental_tag}%{version}.tar.gz.asc
BuildRequires:  git autoconf automake gettext-tools libtool pkg-config
BuildRequires:  fuse-devel
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib) >= 1.2.5
BuildRequires:  pkgconfig(libbfio)
BuildRequires:  pkgconfig(libcaes) >= 20120425
BuildRequires:  pkgconfig(libcdata)
BuildRequires:  pkgconfig(libcerror) >= 20120526
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath)
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache)
BuildRequires:  pkgconfig(libfdata)
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libhmac) >= 20120425
BuildRequires:  pkgconfig(libuna) >= 20120425

%description
libfsapfs is a library to access the Apple File System (APFS).

Read-only supported APFS formats:

* version 2

Supported APFS format features:

* ZLIB (DEFLATE) compression
* LZVN compression
* encryption

Unsupported APFS format features:

* APFS version 1
* Fusion drive (NX_INCOMPAT_FUSION)
* snapshots
* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10
* T2 encryption

%package devel
Summary:        Development files for libfsapfs
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for %{name}.


%package -n libfsapfs1
Summary: Library for access the Apple File System (APFS)
Group:          System/Libraries

%description -n libfsapfs1
libfsapfs1 is a library for access the Apple File System (APFS).

%package -n python3-libfsapfs
Summary: Python bindings for %{name}
Requires: libfsapfs1

%description -n python3-libfsapfs
Python bindings for %{name}, a library for access the Apple File System
(APFS).

%prep
%setup -q -n %{name}-%{version}

%build
%define _lto_cflags -ffat-lto-objects
export LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS="%{optflags}"
%configure --disable-static \
  --enable-wide-character-type \
  --enable-verbose-output \
  --enable-debug-output \
  --enable-python3


%make_build %{?_smp_mflags}


%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%check
make check || /bin/true

%post -n libfsapfs1 -p /sbin/ldconfig
%postun -n libfsapfs1 -p /sbin/ldconfig

%files
%license COPYING COPYING.LESSER
%doc ChangeLog README
%{_bindir}/fsapfsinfo
%{_bindir}/fsapfsmount
%{_mandir}/man*/*

%files devel
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/*

%files -n libfsapfs1
%{_libdir}/%{name}*so.*

%files -n python3-libfsapfs
%{python3_sitearch}/pyfsapfs*

%changelog

