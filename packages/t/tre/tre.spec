#
# spec file for package tre
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 5
Name:           tre
Version:        0.9.0
Release:        0
Summary:        POSIX-compatible regexp library with approximate matching
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://laurikari.net/tre/
Source0:        https://github.com/laurikari/tre/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  glibc-locale
%lang_package -n libtre%{sover}

%description
TRE is a POSIX-compatible regexp matching library with approximate
(fuzzy) matching.

%package -n libtre%{sover}
Summary:        POSIX-compatible regexp library with approximate matching
Group:          System/Libraries

%description -n libtre%{sover}
TRE is a POSIX-compatible regexp matching library with approximate
(fuzzy) matching. TRE's algorithm has linear worst-case time in the
length of the text being searched, and quadratic worst-case time in
the length of the used regular expression.

%package devel
Summary:        Header files for the TRE regex library
Group:          Development/Libraries/C and C++
Requires:       libtre%{sover} = %{version}

%description devel
TRE is a POSIX-compatible regexp matching library with approximate
This package contains the headers.

%package -n agrep
Summary:        Another grep with approximate matching and block search
Group:          Productivity/Text/Utilities

%description -n agrep
agrep is a grep utility which has the ability to search for
approximate patterns as well as block oriented search.

%prep
%autosetup -p1

%build
%configure --disable-static --enable-shared
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
%make_build check

%ldconfig_scriptlets -n libtre%{sover}

%files -n libtre%{sover}
%license LICENSE
%{_libdir}/libtre.so.*

%files devel
%license LICENSE
%doc doc/default.css doc/tre-api.html doc/tre-syntax.html
%{_includedir}/*
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/*

%files -n agrep
%license LICENSE
%{_bindir}/agrep
%{_mandir}/man1/agrep.1%{?ext_man}

%files -n libtre%{sover}-lang -f %{name}.lang
%license LICENSE

%changelog
