#
# spec file for package libhtp
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


%define sover   2
%define lname   %{name}%{sover}
Name:           libhtp
Version:        0.5.42
Release:        0
Summary:        HTTP normalizer and parser
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.openinfosecfoundation.org/
Source:         https://github.com/OISF/libhtp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
The HTP Library is an HTTP normalizer and parser written by Ivan Ristic of Mod Security fame for the OISF. This integrates and provides very advanced processing of HTTP streams for Suricata. The HTP library is required by the engine, but may also be used independently in a range of applications and tools.

%package -n %{lname}
Summary:        Library for HTTP normalizer and parser
Group:          System/Libraries

%description -n %{lname}
The HTP Library is an HTTP normalizer and parser written by Ivan Ristic of Mod Security fame for the OISF. This integrates and provides very advanced processing of HTTP streams for Suricata. The HTP library is required by the engine, but may also be used independently in a range of applications and tools.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
sed -i 's/\r$//' ChangeLog

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING LICENSE
%doc AUTHORS ChangeLog README
%{_libdir}/libhtp.so.%{sover}*

%files devel
%{_includedir}/htp
%{_libdir}/libhtp.so
%{_libdir}/pkgconfig/htp.pc

%changelog
