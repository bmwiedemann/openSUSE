#
# spec file for package libabigail
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname   libabigail8
Name:           libabigail
Version:        2.9
Release:        0
Summary:        Application Binary Interface Generic Analysis and Instrumentation Library
License:        Apache-2.0 WITH LLVM-exception
Group:          Development/Libraries/C and C++
#Git-Clone:     git://sourceware.org/git/libabigail.git
URL:            https://sourceware.org/libabigail/
Source:         http://mirrors.kernel.org/sourceware/libabigail/%name-%version.tar.xz
BuildRequires:  binutils-devel
BuildRequires:  dpkg
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  libbpf-devel
BuildRequires:  libdw-devel >= 0.170
BuildRequires:  libtool >= 2.2
BuildRequires:  libzip-devel
BuildRequires:  makeinfo
BuildRequires:  pkg-config
BuildRequires:  python3-Sphinx
BuildRequires:  xz
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.22
BuildRequires:  pkgconfig(libxxhash) >= 0.8.0
BuildRequires:  pkgconfig(libzip) >= 0.10

%description
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program.

%package -n %lname
Summary:        Application Binary Interface Generic Analysis and Instrumentation Library
Group:          System/Libraries

%description -n %lname
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program. The
library provides a way to compare two ABI corpuses, provide detailed
information about their differences, and help build tools to infer
interesting conclusions about these differences.

%package devel
Summary:        Development files for the ABI-relevant artifact library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program. The
library provides a way to compare two ABI corpuses, provide detailed
information about their differences.

This subpackage contains the files needed to build programs with ABIGAIL.

%package tools
Summary:        Utilities to inspect ABI-relevant artifacts
Group:          Development/Tools/Other

%description tools
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program.

This subpackage contains the ABIGAIL utilities allowing to infer
interesting conclusions about these differences.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --includedir="%_includedir/%name" --docdir="%_docdir/%name" \
	--disable-static --enable-cxx11 --disable-silent-rules
%make_build
pushd doc/manuals
# generate doc non-parallel to avoid triggering https://github.com/sphinx-doc/sphinx/issues/2946
%make_build man info -j1
popd

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

pushd doc/manuals
make DESTDIR="%buildroot" install-man-and-info-doc
popd

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libabigail.so.*

%files devel
%_includedir/%name/
%_libdir/libabigail.so
%_libdir/pkgconfig/*.pc
%_datadir/aclocal/
%_mandir/man7/libabigail.7*

%files tools
%license LICENSE.txt
%_bindir/abi*
%_bindir/kmidiff
%_mandir/man1/abi*.1*
%_infodir/abigail.info*
%_libdir/%name/

%changelog
