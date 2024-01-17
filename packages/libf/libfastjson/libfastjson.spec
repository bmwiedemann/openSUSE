#
# spec file for package libfastjson
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.2304.0
Release:        0
Summary:        JSON parsing library, a fork of json-c
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/rsyslog/libfastjson
Source:         https://download.rsyslog.com/libfastjson/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

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

%package -n libfastjson-devel
Summary:        Development headers and libraries for libfastjson
Group:          Development/Libraries/C and C++
Requires:       libfastjson%{somajor} = %{version}

%description -n libfastjson-devel
A JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

This package includes header files and scripts needed for developers
using the libfastjson library

%prep
%autosetup

%build
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libfastjson%{somajor} -p /sbin/ldconfig
%postun -n libfastjson%{somajor} -p /sbin/ldconfig

%files -n libfastjson%{somajor}
%license COPYING
%{_libdir}/libfastjson.so.%{somajor}*

%files -n libfastjson-devel
%doc AUTHORS
%license COPYING
%{_libdir}/libfastjson.so
%{_includedir}/libfastjson
%{_libdir}/pkgconfig/libfastjson.pc

%changelog
