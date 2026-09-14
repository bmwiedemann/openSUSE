#
# spec file for package lrzip
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# Upstream renumbered 0.660 -> 0.7.2, which sorts older in rpmvercmp;
# Epoch is forbidden per review, so map upstream 0.7.2 -> 0.702
# (7*100+2): sorts above 0.660, stays ordered for 0.7.x/0.8.x/0.10.x.
Version:        0.702
Release:        0
Summary:        Very High Ratio and Speed Compression Designed for Large Files
License:        GPL-2.0-only
URL:            http://ck.kolivas.org/apps/lrzip/
Source:         https://github.com/ckolivas/lrzip/releases/download/v0.7.2/lrzip-0.7.2.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(lzo2)
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
%autosetup -p1 -n lrzip-0.7.2

%build
%configure
%make_build

%check
# SKIP_SLOW drops the 1 GiB parallel/sort cases, too heavy for builders
SKIP_SLOW=1 %make_build check

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/doc"
chmod 0644 README* COPYING doc/README* doc/magic.header.txt doc/lrzip.conf.example

%files
%license COPYING
%doc AUTHORS ChangeLog README* TODO WHATS-NEW
%doc doc/README.benchmarks doc/README.lzo_compresses.test.txt
%doc doc/lrzip.conf.example doc/magic.header.txt
%{_bindir}/lrzip
%{_bindir}/lrunzip
%{_bindir}/lrzcat
%{_bindir}/lrztar
%{_bindir}/lrzuntar
%{_bindir}/lrz
%{_mandir}/man?/*.?%{?ext_man}

%changelog
