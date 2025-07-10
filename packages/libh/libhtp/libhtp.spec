#
# spec file for package libhtp
#
# Copyright (c) 2025 SUSE LLC
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


%define sover   2
%define lname   %{name}%{sover}
%bcond_without tests
Name:           libhtp
Version:        0.5.50
Release:        0
Summary:        HTTP normalizer and parser
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.openinfosecfoundation.org/
Source:         https://github.com/OISF/libhtp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
%if %{with tests}
BuildRequires:  c++_compiler
%endif

%description
LibHTP is a security-aware parser for the HTTP protocol and the related bits
and pieces. The goal of the project is mainly to support the Suricata use case.
Other use cases might not fully be supported, and we encourage you to cover these.

%package -n %{lname}
Summary:        Library for HTTP normalizer and parser
Group:          System/Libraries

%description -n %{lname}
LibHTP is a security-aware parser for the HTTP protocol and the related bits
and pieces. The goal of the project is mainly to support the Suricata use case.
Other use cases might not fully be supported, and we encourage you to cover these.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
sed -i 's/\r$//' ChangeLog

%build
autoreconf -fiv
%configure \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if %{with tests}
%make_build test
%endif

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license COPYING LICENSE
%doc AUTHORS ChangeLog README
%{_libdir}/libhtp.so.%{sover}
%{_libdir}/libhtp.so.%{sover}.*

%files devel
%license COPYING LICENSE
%{_includedir}/htp
%{_libdir}/libhtp.so
%{_libdir}/pkgconfig/htp.pc

%changelog
