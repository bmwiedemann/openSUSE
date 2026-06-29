#
# spec file for package cmark-gfm
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


# Upstream bakes the full release string into the SONAME
# (libcmark-gfm.so.0.29.0.gfm.13).  We keep parity with the upstream
# soname (as Debian/Arch/Gentoo do).  Per the shared-library packaging
# policy, the lib subpackage suffix reflects the FULL soname
# (0_29_0_gfm_13), so that a future .gfm.NN soname bump renames the
# package cleanly.  The alphabetic "gfm" component makes rpmlint's shlib
# detector emit a spurious shlib-policy-missing-lib, which is filtered in
# cmark-gfm.rpmlintrc.
%define sover    0.29.0.gfm.13
%define libcmark libcmark-gfm0_29_0_gfm_13
%define libext   libcmark-gfm-extensions0_29_0_gfm_13
Name:           cmark-gfm
Version:        0.29.0.gfm.13
Release:        0
Summary:        GitHub's fork of cmark, a CommonMark parsing and rendering library
License:        BSD-2-Clause AND MIT
URL:            https://github.com/github/cmark-gfm
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
# PATCH-FIX-UPSTREAM cmark-gfm-0.29.0.gfm.13-cmake4.patch gh#github/cmark-gfm#390 -- build with CMake 4 and switch the test suite to FindPython
Patch0:         %{name}-%{version}-cmake4.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3-base

%description
cmark-gfm is an extended version of the C reference implementation of
CommonMark, a rationalized version of Markdown syntax with a spec. It
adds GitHub Flavored Markdown extensions (tables, strikethrough,
autolinks, task lists and more).

It provides shared libraries with functions for parsing CommonMark
documents to an abstract syntax tree (AST), manipulating the AST, and
rendering the document to HTML, groff man, LaTeX, CommonMark, or an XML
representation of the AST. It also provides a command-line program
(cmark-gfm) for parsing and rendering CommonMark documents.

%package -n %{libcmark}
Summary:        CommonMark parsing and rendering library

%description -n %{libcmark}
cmark-gfm is GitHub's fork of cmark, the C reference implementation of
CommonMark with GitHub Flavored Markdown extensions.

This package provides the shared library for parsing and rendering
CommonMark documents.

%package -n %{libext}
Summary:        GitHub Flavored Markdown extensions for cmark-gfm

%description -n %{libext}
cmark-gfm is GitHub's fork of cmark, the C reference implementation of
CommonMark with GitHub Flavored Markdown extensions.

This package provides the shared library implementing the GitHub
Flavored Markdown extensions (tables, strikethrough, autolinks, task
lists and more).

%package devel
Summary:        Development files for the cmark-gfm libraries
Requires:       %{libcmark} = %{version}
Requires:       %{libext} = %{version}

%description devel
cmark-gfm is GitHub's fork of cmark, the C reference implementation of
CommonMark with GitHub Flavored Markdown extensions.

This package provides the header files, unversioned shared library
symlinks, the pkg-config and CMake support files needed to develop
applications using cmark-gfm.

%prep
%autosetup -p1

%build
%cmake \
  -DLIB_SUFFIX=$(echo %{_lib} | sed 's/^lib//') \
  -DCMARK_SHARED=ON \
  -DCMARK_STATIC=OFF \
  -DCMARK_LIB_FUZZER=OFF \
  -DCMARK_TESTS=ON \
  -DSPEC_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libcmark}
%ldconfig_scriptlets -n %{libext}

%files
%license COPYING
%doc README.md changelog.txt
%{_bindir}/cmark-gfm
%{_mandir}/man1/cmark-gfm.1%{?ext_man}

%files -n %{libcmark}
%license COPYING
%{_libdir}/libcmark-gfm.so.%{sover}*

%files -n %{libext}
%license COPYING
%{_libdir}/libcmark-gfm-extensions.so.%{sover}*

%files devel
%{_includedir}/cmark-gfm*.h
%{_libdir}/libcmark-gfm.so
%{_libdir}/libcmark-gfm-extensions.so
%{_libdir}/pkgconfig/libcmark-gfm.pc
%{_libdir}/cmake/cmark-gfm*.cmake
%{_libdir}/cmake-gfm-extensions/
%{_mandir}/man3/cmark-gfm.3%{?ext_man}

%changelog
