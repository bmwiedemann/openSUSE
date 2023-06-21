#
# spec file for package sexp
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soversion 0
Name:           sexp
Version:        0.8.5
Release:        0
Summary:        S-expressions parser and generator library
License:        MIT
URL:            https://github.com/rnpgp/sexp
Source:         https://github.com/rnpgp/sexp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         sexp-0.8.5-soversion.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.14
BuildRequires:  gtest >= 1.8.1
BuildRequires:  pkgconfig

%description
This is a C++ library for working with S-expressions. S-expressions
are a data structure for representing complex data as a variation on
LISP S-expressions.

%package -n libsexp%{soversion}
Summary:        S-expressions parser and generator library

%description -n libsexp%{soversion}
This is a C++ library for working with S-expressions. S-expressions
are a data structure for representing complex data as a variation on
LISP S-expressions.

This package contains the shared library.

%package devel
Summary:        Development files for sexp
Requires:       libsexp%{soversion} = %{version}

%description devel
This is a C++ library for working with S-expressions. S-expressions
are a data structure for representing complex data as a variation on
LISP S-expressions.

This package contains the files required for developing using sexp.

%prep
%autosetup -p1

%build
%cmake \
	-DDOWNLOAD_GTEST:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libsexp%{soversion}

%files
%license LICENSE.md
%doc README.adoc
%{_bindir}/sexp

%files -n libsexp%{soversion}
%license LICENSE.md
%{_libdir}/libsexp.so.%{soversion}

%files devel
%license LICENSE.md
%{_includedir}/sexp
%{_libdir}/pkgconfig/sexp.pc
%{_libdir}/libsexp.so

%changelog
