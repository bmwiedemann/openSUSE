#
# spec file for package doxygen
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


# build with "--with libclang" to enable libclang support
%bcond_with libclang
Name:           doxygen
Version:        1.8.16
Release:        0
Summary:        Automated C, C++, and Java Documentation Generator
# qtools are used for building and they are GPL-3.0 licensed
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Tools/Doc Generators
URL:            http://www.doxygen.nl/
Source0:        http://doxygen.nl/files/doxygen-%{version}.src.tar.gz
# suse specific
Patch0:         %{name}-modify_footer.patch
# suse specific
Patch1:         %{name}-no-lowercase-man-names.patch
# PATCH-FIX-UPSTREAM: add missing returns to non-void functions
Patch3:         vhdlparser-no-return.patch
# really do not require git executable
Patch5:         doxygen-git-not-required.patch
Patch6:         doxygen-llvm-libs.patch
# PATCH-FIX-UPSTREAM: Populate FILE_PATTERN default if not set (issue#7190)
Patch7:         PR_7193_fix_blank_file_patterns.patch
# PATCH-FIX-UPSTREAM Including external tag files with TOC produces a broken index.qhp
Patch8:         0001-issue-7248-Including-external-tag-files-with-TOC-pro.patch
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.12
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  python3-base
BuildRequires:  python3-xml
# Do not bother building documentation with latex since it is present on the
# web trivialy for all versions of doxygen
Obsoletes:      doxygen-doc
%if %{with libclang}
BuildRequires:  llvm-clang-devel
%endif

%description
Doxygen is a documentation system for C, C++, Java, and IDL. It can
generate an online class browser (in HTML) and an offline reference
manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen is
developed on a Linux platform, but it runs on most other UNIX flavors
as well.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch5 -p1
%if %{with libclang}
%patch6
%endif
%patch7 -p1
%patch8 -p1

%build
%cmake \
    -Dbuild_doc=OFF \
    -Dbuild_xmlparser=ON \
    -Dbuild_search=OFF \
    -Dbuild_wizard=OFF \
%if %{with libclang}
    -Duse_libclang=ON \
%endif
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_STATIC_LIBS=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 doc/doxygen.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%attr(644,root,root) %{_mandir}/man1/doxygen.1%{?ext_man}
%attr(755,root,root) %{_bindir}/*

%changelog
