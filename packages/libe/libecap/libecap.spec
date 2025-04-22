#
# spec file for package libecap
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


%define sover 3
Name:           libecap
Version:        1.0.1
Release:        0
Summary:        Library implementing the eCAP interface for application filtering modules
License:        BSD-2-Clause
URL:            https://www.e-cap.org/
Source:         https://www.e-cap.org/archive/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler

%description
eCAP is a software interface that allows a network application, such as an HTTP
proxy or an ICAP server, to outsource content analysis and adaptation to a
loadable module. The functionality is similar to the ICAP protocol (RFC 3507),
but implemented as function calls instead of network interactions.

%package -n %{name}%{sover}
Summary:        Library implementing the eCAP interface for application filtering modules

%description -n %{name}%{sover}
eCAP is a software interface that allows a network application, such as an http
proxy or an icap server, to outsource content analysis and adaptation to a
loadable module. the functionality is similar to the icap protocol (rfc 3507),
but implemented as function calls instead of network interactions.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
ecAP is a software interface that allows a network application, such as an http
proxy or an icap server, to outsource content analysis and adaptation to a
loadable module. the functionality is similar to the icap protocol (rfc 3507),
but implemented as function calls instead of network interactions.

This package contains files needed to build with %{name}.

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
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/libecap.so.%{sover}{,.*}

%files devel
%license LICENSE
%doc NOTICE README CREDITS
%{_includedir}/libecap
%{_libdir}/libecap.so
%{_libdir}/pkgconfig/libecap.pc

%changelog
