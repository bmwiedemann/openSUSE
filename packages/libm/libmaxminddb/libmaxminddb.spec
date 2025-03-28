#
# spec file for package libmaxminddb
#
# Copyright (c) 2024 SUSE LLC
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


%define lname	libmaxminddb0
Name:           libmaxminddb
Version:        1.12.2
Release:        0
Summary:        C library for the MaxMind DB file format
License:        Apache-2.0
URL:            https://dev.maxmind.com/
Source:         https://github.com/maxmind/libmaxminddb/releases/download/%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig

%description
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a
custom binary format designed to facilitate fast lookups of IP
addresses while allowing for great flexibility in the type of
data associated with an address.

%package -n %{lname}
Summary:        C library for the MaxMind DB file format

%description -n %{lname}
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a
custom binary format designed to facilitate fast lookups of IP
addresses while allowing for great flexibility in the type of
data associated with an address.

%package -n mmdblookup
Summary:        An utility to look up an IP address in a MaxMind DB file

%description -n mmdblookup
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a
custom binary format designed to facilitate fast lookups of IP
addresses while allowing for great flexibility in the type of
data associated with an address.

This package contains the mmdblookup binary.

%package devel
Summary:        Development files for the MaxMind DB file format library
Requires:       %{lname} = %{version}

%description devel
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a
custom binary format designed to facilitate fast lookups of IP
addresses while allowing for great flexibility in the type of
data associated with an address.

This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}/%{_prefix}

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSE
%{_libdir}/%{name}.so.*

%files -n mmdblookup
%license LICENSE
%doc doc/mmdblookup.md
%{_bindir}/mmdblookup
%{_mandir}/man1/*.1%{?ext_man}

%files devel
%doc Changes.md NOTICE README.md doc/mmdblookup.md doc/libmaxminddb.md
%license LICENSE
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3%{?ext_man}

%changelog
