#
# spec file for package libmseed
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
Name:           libmseed
Version:        3.1.3
Release:        0
Summary:        MiniSEED data format library
License:        Apache-2.0
URL:            https://earthscope.github.io/libmseed/
Source:         https://github.com/EarthScope/libmseed/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
The miniSEED library provides a framework for manipulation of miniSEED records,
a format commonly used for seismological time series and related data. The
library includes the functionality to read and write data records, in addition
to reconstructing time series from multiple records.

%package -n %{name}%{sover}
Summary:        MiniSEED data format library

%description -n %{name}%{sover}
The miniSEED library provides a framework for manipulation of miniSEED records,
a format commonly used for seismological time series and related data. The
library includes the functionality to read and write data records, in addition
to reconstructing time series from multiple records.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
The miniSEED library provides a framework for manipulation of miniSEED records,
a format commonly used for seismological time series and related data. The
library includes the functionality to read and write data records, in addition
to reconstructing time series from multiple records.

This package contains files required for building using %{name}.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	DOCDIR=%{_docdir}/%{name} \
	install

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE
%doc ChangeLog README*
%{_libdir}/libmseed.so.%{sover}
%{_libdir}/libmseed.so.%{sover}.*

%files devel
%license LICENSE
%{_docdir}/libmseed
%{_includedir}/libmseed.h
%{_libdir}/libmseed.so
%{_libdir}/pkgconfig/mseed.pc

%changelog
