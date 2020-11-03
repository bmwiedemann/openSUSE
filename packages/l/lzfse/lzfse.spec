#
# spec file for package lzfse
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


Name:           lzfse
Version:        1.0
Release:        0
Summary:        Reference C implementation of the LZFSE compressor
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
URL:            https://github.com/lzfse/lzfse
Source:         https://github.com/lzfse/lzfse/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
LZFSE is a Lempel-Ziv style data compression algorithm using Finite State
Entropy coding. It targets similar compression rates at higher compression
and decompression speed compared to deflate using zlib.

%package devel
Summary:        Reference C implementation of the LZFSE compressor
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
LZFSE is a Lempel-Ziv style data compression algorithm using Finite State
Entropy coding. It targets similar compression rates at higher compression
and decompression speed compared to deflate using zlib.

This package contains devel files.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%cmake \
  -Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/lzfse
%{_libdir}/liblzfse.so

%files devel
%{_includedir}/lzfse.h

%changelog
