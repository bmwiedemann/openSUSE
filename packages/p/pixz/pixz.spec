#
# spec file for package pixz
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


Name:           pixz
Version:        1.0.6
Release:        0
Summary:        Parallel, indexing version of XZ
License:        BSD-2-Clause
Group:          Productivity/Archiving/Compression
URL:            https://github.com/vasi/pixz
Source:         https://github.com/vasi/pixz/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
# compatibility tests run classic xz
BuildRequires:  xz
BuildRequires:  pkgconfig(libarchive) >= 2.8
BuildRequires:  pkgconfig(liblzma) >= 4.999.9-beta-212

%description
The existing XZ Utils provide great compression in the .xz file format, but
they produce just one big block of compressed data. Pixz instead produces a
collection of smaller blocks which makes random access to the original data
possible. This is especially useful for large tarballs.

Pixz supports automatic indexing and parallel compression and decompression
using all available CPU cores.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fcommon"
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%doc NEWS TODO README.md
%{_bindir}/pixz
%{_mandir}/man1/pixz.1%{?ext_man}

%changelog
