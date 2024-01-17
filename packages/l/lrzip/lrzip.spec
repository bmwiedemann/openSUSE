#
# spec file for package lrzip
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           lrzip
Version:        0.651
Release:        0
Summary:        Very High Ratio and Speed Compression Designed for Large Files
License:        GPL-2.0-only
URL:            http://ck.kolivas.org/apps/lrzip/
Source:         http://ck.kolivas.org/apps/lrzip/lrzip-%{version}.tar.xz
# PATCH-FIX-UPSTREAM https://github.com/ckolivas/lrzip/pull/243
Patch0:         fixasmstack.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  lzo-devel
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(zlib)
Conflicts:      rzsz

%description
LRZIP is a compression program that can achieve very high compression
ratios and speed when used with large files. It uses the combined compression
algorithms of lzma for maximum compression, lzo for maximum speed, and the long
range redundancy reduction of rzip. It is designed to scale with increases
with RAM size, improving compression further. A choice of either size or
speed optimizations allows for either better compression than even lzma can
provide, or better speed than gzip, but with bzip2 sized compression levels.

%prep
%autosetup -p1

%build
%configure \
%ifnarch %{ix86} x86_64
  --disable-asm \
%endif

%make_build

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/doc"
rm doc/Makefile*
chmod 0644 README* COPYING doc/README*

%files
%license COPYING
%doc AUTHORS ChangeLog README* TODO WHATS-NEW
%doc doc/*
%{_bindir}/*
%{_mandir}/man?/*.?%{?ext_man}

%changelog
