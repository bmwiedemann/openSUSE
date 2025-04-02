#
# spec file for package sfsexp
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 1
Name:           sfsexp
Version:        1.4.1
Release:        0
Summary:        Small Fast S-Expression Library
License:        LGPL-2.1-or-later
URL:            https://github.com/mjsottile/sfsexp
Source:         https://github.com/mjsottile/sfsexp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
This library supports manipulation of symbolic expressions "s-expressions".
S-expressions are able to represent complex, structured data without requiring
additional meta-data describing the structure.

%package devel
Summary:        Development files for %{name}
Requires:       libsexp%{sover} = %{version}

%description devel
This library supports manipulation of symbolic expressions "s-expressions".
S-expressions are able to represent complex, structured data without requiring
additional meta-data describing the structure.

This package contains the files needed to build packages with %{name}.

%package -n libsexp%{sover}
Summary:        Small Fast S-Expression Library

%description -n libsexp%{sover}
This library supports manipulation of symbolic expressions "s-expressions".
S-expressions are able to represent complex, structured data without requiring
additional meta-data describing the structure.

This package contains the shared library.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
cd tests
sh dotests.sh

%ldconfig_scriptlets -n libsexp%{sover}

%files -n libsexp%{sover}
%license COPYING LICENSE_LGPL
%{_libdir}/libsexp.so.%{sover}
%{_libdir}/libsexp.so.%{sover}.*

%files devel
%license COPYING LICENSE_LGPL
%doc README.md
%{_includedir}/%{name}
%{_libdir}/libsexp.so
%{_libdir}/pkgconfig/sfsexp.pc

%changelog
