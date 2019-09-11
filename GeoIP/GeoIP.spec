#
# spec file for package GeoIP
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


Name:           GeoIP
Version:        1.6.12
Release:        0
Summary:        Library to find the country that any IP address originates from
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.maxmind.com/
Source0:        https://github.com/maxmind/geoip-api-c/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        LICENSE
Source2:        README.SUSE
Source3:        geoip-fetch
Source4:        baselibs.conf
Source5:        geoip-csv-to-dat.cpp
Source6:        geoip-asn-csv-to-dat.cpp
Source7:        v4-to-v6-layout.pl
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
Recommends:     curl

%description
GeoIP is a C library that enables the user to find the country that any
IP address or hostname originates from.  It uses a file based database.
This database simply contains IP blocks as keys, and countries as
values. This database should be more complete and accurate than using
reverse DNS lookups.

MaxMind offers a service where you can have your database updated
automically each month.

%package data
Summary:        GeoLite country data for GeoIP
License:        CC-BY-SA-3.0
Group:          Productivity/Networking/Other
BuildArch:      noarch

%description data
This package does not actually contain any data. It only exists to
give ownership the database files you can fetch using
"geoip-fetch".

%package -n lib%{name}1
Summary:        Shared libraries of the GeoIP C API
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-data
Recommends:     GeoIP

%description -n lib%{name}1
GeoIP is a C library that enables the user to find the country that any
IP address or hostname originates from.  It uses a file based database.
This database simply contains IP blocks as keys, and countries as
values.  This database should be more complete and accurate than using
reverse DNS lookups.

MaxMind offers a service where you can have your database updated
automically each month.

This package holds the shared libraries for GeoIP.

%package -n lib%{name}-devel
Summary:        Development Files for GeoIP
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       lib%{name}1 = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < %{version}

%description -n lib%{name}-devel
GeoIP is a C library that enables the user to find the country that any
IP address or hostname originates from.  It uses a file based database.
This database simply contains IP blocks as keys, and countries as
values.  This database should be more complete and accurate than using
reverse DNS lookups.

MaxMind offers a service where you can have your database updated
automically each month.

This package holds the development files for GeoIP.

%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%configure \
  --disable-static

sed -i -e '/-DGEOIPDATADIR/s,\$(pkgdatadir),%{_localstatedir}/lib/GeoIP,' libGeoIP/Makefile{.am,.in,}
sed -i -e 's,\$(pkgdatadir),%{_localstatedir}/lib/GeoIP,' man/Makefile{.am,.in,}

make %{?_smp_mflags}

%install
%make_install

install -d %{buildroot}%{_localstatedir}/lib/GeoIP %{buildroot}%{_prefix}/lib/geoip/
# can't actually ship stuff in /var anymore boo#1093352
#install data/* %{buildroot}%{_localstatedir}/lib/GeoIP/
#
g++ %{optflags} -I %{buildroot}%{_includedir} -L %{buildroot}%{_libdir} -o %{buildroot}%{_prefix}/lib/geoip/geoip-generator     %{SOURCE5} -lGeoIP
g++ %{optflags} -I %{buildroot}%{_includedir} -L %{buildroot}%{_libdir} -o %{buildroot}%{_prefix}/lib/geoip/geoip-generator-asn %{SOURCE6} -lGeoIP
install -m 0755 %{SOURCE7} %{buildroot}%{_prefix}/lib/geoip/
# do not ship these
rm %{buildroot}%{_libdir}/libGeoIP.la
# install fetcher
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_sbindir}/geoip-fetch

%check
# as tests require a running network OBS can not run it
%if 0%{?with_tests}
LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make %{?_smp_mflags} check
%endif

%post   -n lib%{name}1 -p /sbin/ldconfig
%postun -n lib%{name}1 -p /sbin/ldconfig

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog README.md README.SUSE
%{_bindir}/geoiplookup
%{_bindir}/geoiplookup6
%{_mandir}/man1/geoiplookup6.1%{?ext_man}
%{_mandir}/man1/geoiplookup.1%{?ext_man}
%{_sbindir}/geoip-fetch
%{_prefix}/lib/geoip/

%files data
%dir %{_localstatedir}/lib/%{name}
%ghost %{_localstatedir}/lib/%{name}/GeoIP.dat
%ghost %{_localstatedir}/lib/%{name}/GeoIPASNum.dat
%ghost %{_localstatedir}/lib/%{name}/GeoIPCity.dat
%ghost %{_localstatedir}/lib/%{name}/GeoIPv6.dat

%files -n lib%{name}1
%license COPYING LICENSE
%doc AUTHORS ChangeLog README.md README.SUSE
%{_libdir}/libGeoIP.so.1
%{_libdir}/libGeoIP.so.%{version}

%files -n lib%{name}-devel
%license COPYING LICENSE
%doc AUTHORS ChangeLog README.md README.SUSE
%{_includedir}/GeoIP.h
%{_includedir}/GeoIPCity.h
%{_libdir}/libGeoIP.so
%{_libdir}/pkgconfig/geoip.pc

%changelog
