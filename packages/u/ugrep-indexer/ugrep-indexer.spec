#
# spec file for package ugrep-indexer
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


Name:           ugrep-indexer
Version:        0.9.1
Release:        0
Summary:        File indexer for accelerated search using ugrep
License:        BSD-3-Clause
URL:            https://github.com/Genivia/ugrep-indexer
Source:         https://github.com/Genivia/ugrep-indexer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Supplements:    ugrep >= 3.12.6

%description
The ugrep-indexer utility recursively indexes files to accelerate recursive
searching on file systems with ugrep.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/ugrep-indexer
%{_mandir}/man1/ugrep-indexer.1%{?ext_man}

%changelog
