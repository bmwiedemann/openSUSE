#
# spec file for package md4c
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


Name:           md4c
Version:        0.5.2
Release:        0
Summary:        C Markdown parser
License:        MIT
URL:            https://github.com/mity/md4c
Source:         https://github.com/mity/md4c/archive/refs/tags/release-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
# For tests
BuildRequires:  python3

%description
MD4C is Markdown parser implementation in C, with the following features:
- Compliance: Generally, MD4C aims to be compliant to the latest version of CommonMark specification.
- Extensions: MD4C supports some commonly requested and accepted extensions.
- Compactness: MD4C parser is implemented in one source file and one header
file.
- Embedding: MD4C parser is easy to reuse in other projects.
- Push model: MD4C parses the complete document and calls few callback
functions provided by the application to inform it about a start/end of every block, a start/end of every span, and with any textual contents.
- Encoding: MD4C by default expects UTF-8 encoding of the input document.

This package provides the md2html utility.

%package -n libmd4c0
Summary:        C Markdown parser

%description -n libmd4c0
MD4C is Markdown parser implementation in C, with the following features:
- Compliance: Generally, MD4C aims to be compliant to the latest version of CommonMark specification.
- Extensions: MD4C supports some commonly requested and accepted extensions.
- Compactness: MD4C parser is implemented in one source file and one header
file.
- Embedding: MD4C parser is easy to reuse in other projects.
- Push model: MD4C parses the complete document and calls few callback
functions provided by the application to inform it about a start/end of every block, a start/end of every span, and with any textual contents.
- Encoding: MD4C by default expects UTF-8 encoding of the input document.

This package provides the md4c library.

%package devel
Summary:        Development files for md4c library
Requires:       libmd4c0 = %{version}

%description devel
This package contains development files needed to use md4c.

%prep
%autosetup -p1 -n md4c-release-%{version}

%build
%cmake

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libmd4c0

%check
pushd %{__builddir}
../scripts/run-tests.sh
popd

%files
%{_mandir}/man1/md2html.1%{?ext_man}
%{_bindir}/md2html

%files -n libmd4c0
%license LICENSE.md
%doc README.md
%{_libdir}/libmd4c-html.so.*
%{_libdir}/libmd4c.so.*

%files devel
%{_includedir}/md4c-html.h
%{_includedir}/md4c.h
%{_libdir}/cmake/md4c/
%{_libdir}/libmd4c-html.so
%{_libdir}/libmd4c.so
%{_libdir}/pkgconfig/md4c-html.pc
%{_libdir}/pkgconfig/md4c.pc

%changelog
