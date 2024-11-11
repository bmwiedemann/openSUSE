#
# spec file for package sexpp
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Name:           sexpp
Version:        0.9.0
Release:        0
Summary:        S-expressions parser and generator library
License:        MIT
URL:            https://github.com/rnpgp/sexpp
Source:         https://github.com/rnpgp/sexpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.14
BuildRequires:  gtest >= 1.8.1
BuildRequires:  pkgconfig

%description
This is a C++ library for working with S-expressions. S-expressions
are a data structure for representing complex data as a variation on
LISP S-expressions.

%package -n libsexpp%{soversion}
Summary:        S-expressions parser and generator library

%description -n libsexpp%{soversion}
This is a C++ library for working with S-expressions. S-expressions
are a data structure for representing complex data as a variation on
LISP S-expressions.

This package contains the shared library.

%package devel
Summary:        Development files for sexpp
Requires:       libsexpp%{soversion} = %{version}

%description devel
This is a C++ library for working with S-expressions. S-expressions
are a data structure for representing complex data as a variation on
LISP S-expressions.

This package contains the files required for developing using sexpp.

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

%ldconfig_scriptlets -n libsexpp%{soversion}

%files
%license LICENSE.md
%doc README.adoc
%{_bindir}/sexpp
%{_mandir}/man1/*.1%{?ext_man}

%files -n libsexpp%{soversion}
%license LICENSE.md
%{_libdir}/libsexpp.so.%{soversion}
%{_libdir}/libsexpp.so.%{soversion}.*

%files devel
%license LICENSE.md
%{_includedir}/sexpp
%{_libdir}/pkgconfig/sexpp.pc
%{_libdir}/libsexpp.so

%changelog
