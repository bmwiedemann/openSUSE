#
# spec file for package cg3
#
# Copyright (c) 2022 SUSE LLC
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


Name:           cg3
%define lname	libcg3-1
Version:        1.3.9
Release:        0
Summary:        VISL Constraint Grammar implementation
License:        BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
# src/icu_uoptions.cpp see license.icu.txt (MIT)
Group:          Productivity/Scientific/Other
URL:            https://visl.sdu.dk/cg3.html
#Git-Clone:     https://github.com/GrammarSoft/cg3

Source:         https://github.com/GrammarSoft/cg3/releases/download/v%version/%name-%version.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(icu-uc)
Requires:       perl(Digest::SHA1)
Requires:       perl(File::Spec)
Requires:       perl(Getopt::Long)

%description
Constraint Grammar (CG) is a methodological paradigm for natural
language processing (NLP). Linguist-written, context dependent rules
are compiled into a grammar that assigns grammatical tags
("readings") to words or other tokens in running text.

%package -n %lname
Summary:        VISL Constraint Grammar shared library
Group:          System/Libraries
License:        GPL-3.0-or-later

%description -n %lname
Constraint Grammar (CG) is a methodological paradigm for natural
language processing (NLP). Linguist-written, context dependent rules
are compiled into a grammar that assigns grammatical tags
("readings") to words or other tokens in running text.

%package devel
Summary:        Development files for the VISL Constraint Grammar library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
License:        GPL-3.0-or-later

%description devel
Constraint Grammar (CG) is a methodological paradigm for natural
language processing (NLP). Linguist-written, context dependent rules
are compiled into a grammar that assigns grammatical tags
("readings") to words or other tokens in running text.

This subpackage contains the files needed to build programs
that want to use VISL CG-3.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
rm -f "%buildroot/%_libdir"/*.a "%buildroot/%_libdir/libcg3-private.so"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/cg*
%_bindir/visl*
%_datadir/emacs/
%_mandir/man1/*.1*
%license COPYING

%files -n %lname
%_libdir/libcg3.so.1*

%files devel
%_includedir/cg3.h
%_libdir/libcg3.so
%_libdir/pkgconfig/*.pc

%changelog
