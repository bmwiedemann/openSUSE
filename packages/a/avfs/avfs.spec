#
# spec file for package avfs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 1
Name:           avfs
Version:        1.2.0
Release:        0
Summary:        AVFS - an archive look-inside filesystem
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://avf.sourceforge.net/
Source0:        https://downloads.sf.net/avf/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sf.net/avf/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Patch0:         %{name}-fuse3-support.patch
BuildRequires:  lzlib-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(zlib)

%description
AVFS is a filesystem which enables all programs to look inside archived or
compressed files, or access remote files without recompiling the programs
or changing the kernel.

%package devel
Summary:        Development files for AVFS, an archive look-inside filesystem
Requires:       libavfs%{sover} = %{version}

%description devel
This package includes the development file for the package avfs.
AVFS is a filesystem which enables all programs to look inside archived or
compressed files, or access remote files without recompiling the programs
or changing the kernel.

%package -n libavfs%{sover}
Summary:        Shared library for AVFS, an archive look-inside filesystem

%description -n libavfs%{sover}
This package includes the runtime shared library for the package avfs.
AVFS is a system, which enables all programs to look inside archived or
compressed files, or access remote files without recompiling the programs
or changing the kernel.

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-shared \
  --enable-library \
  --with-system-zlib \
  --with-system-bzlib \
  --enable-dav \
  --with-lzip \
  --with-xz \
  --with-zstd \
  %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n libavfs%{sover}

%files
%license COPYING
%doc ChangeLog README NEWS TODO
%doc doc/api-overview
%doc doc/background
%doc doc/FORMAT
%{_bindir}/davpass
%{_bindir}/ftppass
%{_bindir}/avfsd
%{_bindir}/mountavfs
%{_bindir}/umountavfs
%dir %{_libdir}/avfs
%dir %{_libdir}/avfs/extfs
%{_libdir}/avfs/extfs/*

%files devel
%license COPYING
%{_bindir}/avfs-config
%{_includedir}/avfs.h
%{_includedir}/virtual.h
%{_libdir}/libavfs.so
%{_libdir}/pkgconfig/avfs.pc

%files -n libavfs%{sover}
%license COPYING
%{_libdir}/libavfs.so.%{sover}{,.*}

%changelog
