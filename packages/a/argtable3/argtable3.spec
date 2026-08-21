#
# spec file for package argtable3
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 3
Name:           argtable3
Version:        3.3.1
Release:        0
Summary:        Command-line parsing library that parses GNU-style command-line options
License:        BSD-3-Clause
URL:            https://www.argtable.org/
Source:         https://github.com/argtable/argtable3/releases/download/v%{version}/argtable-v%{version}.tar.gz
BuildRequires:  cmake

%description
A single-file, ANSI C, command-line parsing library that parses GNU-style
command-line options.

%package -n lib%{name}-%{sover}
Summary:        Command-line parsing library that parses GNU-style command-line options

%description -n lib%{name}-%{sover}
A single-file, ANSI C, command-line parsing library that parses GNU-style
command-line options.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}-%{sover} = %{version}

%description devel
A single-file, ANSI C, command-line parsing library that parses GNU-style
command-line options.

This package contains the files needed to build using %{name}.

%prep
%autosetup -p1 -n argtable-v%{version}
chmod -x LICENSE

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n lib%{name}-%{sover}

%files -n lib%{name}-%{sover}
%license LICENSE
%{_libdir}/libargtable3.so.%{sover}{,.*}

%files devel
%license LICENSE
%{_includedir}/argtable3.h
%{_libdir}/cmake/argtable3
%{_libdir}/libargtable3.so
%{_libdir}/pkgconfig/argtable3.pc

%changelog
