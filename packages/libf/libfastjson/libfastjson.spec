#
# spec file for package libfastjson
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


%define somajor 4
Name:           libfastjson
Version:        1.2304.0+ga630254
%define gitrev  a63025493539a11607ed6ab49a54f91a6b8d4e2a
Release:        0
Summary:        JSON parsing library, a fork of json-c
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/rsyslog/libfastjson
Source:         https://github.com/rsyslog/libfastjson/archive/%{gitrev}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
A JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

%package -n libfastjson%{somajor}
Summary:        JSON parsing library
Group:          System/Libraries

%description -n libfastjson%{somajor}
A JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

This package includes the libfastjson library.

%package devel
Summary:        Development headers and libraries for libfastjson
Group:          Development/Libraries/C and C++
Requires:       libfastjson%{somajor} = %{version}

%description devel
A JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

This package includes header files and scripts needed for developers
using the libfastjson library

%prep
%autosetup -p1 -n %{name}-%{gitrev}

%build
./autogen.sh
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libfastjson%{somajor}

%files -n libfastjson%{somajor}
%license COPYING
%{_libdir}/libfastjson.so.%{somajor}*

%files devel
%doc AUTHORS
%license COPYING
%{_libdir}/libfastjson.so
%{_includedir}/libfastjson
%{_libdir}/pkgconfig/libfastjson.pc

%changelog
