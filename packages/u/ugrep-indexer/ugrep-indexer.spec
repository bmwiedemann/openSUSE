#
# spec file for package ugrep-indexer
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ugrep-indexer
Version:        0.9.5
Release:        0
Summary:        File indexer for accelerated search using ugrep
License:        BSD-3-Clause
URL:            https://github.com/Genivia/ugrep-indexer
Source:         https://github.com/Genivia/ugrep-indexer/archive/refs/tags/v%{version}-2.tar.gz#/%{name}-%{version}-2.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Supplements:    ugrep >= 3.12.6
# the bzip3 version seems to old, the tests break with decompression errors
%if 0%{?suse_version} > 1599
BuildRequires:  pkgconfig(bzip3)
%endif

%description
The ugrep-indexer utility recursively indexes files to accelerate recursive
searching on file systems with ugrep.

%prep
%setup -q -n %{name}-%{version}-2

%build
%configure \
%if 0%{?suse_version} > 1599
	--with-bzip3 \
%endif
	%{nil}
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/ugrep-indexer
%{_mandir}/man1/ugrep-indexer.1%{?ext_man}

%changelog
