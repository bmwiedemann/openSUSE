#
# spec file for package tre
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


Name:           tre
Version:        0.8.0_git201402282055
Release:        0
Summary:        POSIX compatible regexp library with approximate matching
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://laurikari.net/tre/
# This source comes from https://github.com/laurikari/tre/, revision
# c2f5d130c91b1696385a6ae0b5bcfd5214bcc9ca. The previously released
# version 0.8.0 is old (2009) and no new released have been made by
# the author, so I'm terming this 0.8.0_git201402282055.
Source0:        tre-%{version}.tar.bz2
Patch0:         %{name}.diff
# Update the python build to fix wrong include and lib paths.
# See https://github.com/laurikari/tre/pull/19.
Patch1:         %{name}-chicken.patch
Patch2:         CVE-2016-8859.patch
# https://github.com/laurikari/tre/pull/87
Patch3:         0001-Remove-broken-agrep-test-entry.patch
BuildRequires:  gettext-devel
BuildRequires:  glibc-locale
BuildRequires:  libtool

%description
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%package -n libtre5
Summary:        POSIX compatible regexp library with approximate matching
Group:          System/Libraries
Requires:       %{name} = %{version}
Recommends:     %{name}-lang = %{version}
Obsoletes:      libtre
Provides:       libtre

%description -n libtre5
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%post -n libtre5 -p /sbin/ldconfig
%postun -n libtre5 -p /sbin/ldconfig

%package devel
Summary:        POSIX compatible regexp library with approximate matching
Group:          Development/Libraries/C and C++
Requires:       libtre5 = %{version}
Obsoletes:      libtre-devel
Provides:       libtre-devel

%description devel
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%package -n agrep
Summary:        Another powerful grep with interesting features
Group:          Productivity/Text/Utilities

%description -n agrep
agrep is another powerful grep which has the  ability to search for
approximate patterns as well as block oriented search.

%lang_package

%prep
%autosetup -p1
./utils/autogen.sh

%build
%configure --disable-static --enable-shared
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} || echo -n >> %{name}.lang

%check
%make_build check

%files
%license LICENSE
%doc ABOUT-NLS AUTHORS NEWS README THANKS TODO

%files -n libtre5
%{_libdir}/libtre.so.*

%files devel
%doc doc/default.css doc/tre-api.html doc/tre-syntax.html
%{_includedir}/*
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/*

%files -n agrep
%{_bindir}/agrep
%{_mandir}/man1/agrep.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
