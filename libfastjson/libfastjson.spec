#
# spec file for package libfastjson
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define somajor 4
Name:           libfastjson
Version:        0.99.8
Release:        0
Summary:        Fast JSON parsing library, a fork of json-c
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/rsyslog/libfastjson
Source:         http://download.rsyslog.com/libfastjson/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A fast JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

%package -n libfastjson%{somajor}
Summary:        Fast JSON parsing library
Group:          System/Libraries

%description -n libfastjson%{somajor}
A fast JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

This package includes the libfastjson library.

%package -n libfastjson-devel
Summary:        Development headers and libraries for libfastjson
Group:          Development/Libraries/C and C++
Requires:       libfastjson%{somajor} = %{version}

%description -n libfastjson-devel
A fast JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

This package includes header files and scripts needed for developers
using the libfastjson library

%prep
%setup -q

%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libfastjson%{somajor} -p /sbin/ldconfig
%postun -n libfastjson%{somajor} -p /sbin/ldconfig

%files -n libfastjson%{somajor}
%defattr(-,root,root)
%license COPYING
%{_libdir}/libfastjson.so.%{somajor}*

%files -n libfastjson-devel
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{_libdir}/libfastjson.so
%{_includedir}/libfastjson
%{_libdir}/pkgconfig/libfastjson.pc

%changelog
