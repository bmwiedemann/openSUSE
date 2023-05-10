#
# spec file for package libcap-ng
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


%define sover  0
%define ambient_sover 0

Name:           libcap-ng
Version:        0.8.3
Release:        0
Summary:        An alternate Linux/POSIX capabilities library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://people.redhat.com/sgrubb/libcap-ng
Source0:        https://people.redhat.com/sgrubb/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source99:       libcap-ng.rpmlintrc
BuildRequires:  kernel-headers >= 2.6.11
BuildRequires:  pkgconfig

%description
libcap-ng is a library providing an alternate mechanism to libcap to
make use of Linux process and file capabilities.

%package -n %{name}%{sover}
Summary:        An alternate Linux/POSIX capabilities library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{name}%{sover}
libcap-ng is a library providing an alternate mechanism to libcap to
inspect and set Linux process and file capabilities (modeled upon a
withdrawn POSIX.1e draft).

%package devel
Summary:        Header files for the libcap-ng library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       kernel-headers >= 2.6.11
Requires:       pkgconfig

%description devel
The libcap-ng-devel package contains the files needed for developing
applications that need to use the libcap-ng library.

%package utils
Summary:        Utilities for analysing and setting file capabilities
License:        GPL-2.0-or-later
Group:          System/Base

%description utils
The libcap-ng-utils package contains applications to analyse the
Linux process capabilities of programs running on a system. It also
lets you set the filesystem-based capabilities.

%package -n libdrop_ambient%{ambient_sover}
Summary:        Library for dropping ambient capabilities
License:        LGPL-2.1-or-later
Requires:       %{name}%{sover} = %{version}

%description -n libdrop_ambient%{ambient_sover}
This library can be used via LD_PRELOAD to force an application started with ambient capabilities to drop them.
It leaves other capabilities intact. This can also be linked against and automatically does the right thing.
You do not need to make any calls into the library because all the work is done in the constructor which runs before main() is called.

%package -n libdrop_ambient-devel
Summary:        Devel package for libdrop_ambient%{ambient_sover}
License:        LGPL-2.1-or-later
Requires:       libdrop_ambient%{ambient_sover}

%description -n libdrop_ambient-devel
This package contains the files needed for developing
applications that need to use the libdrop_ambient library.

%prep
%setup -q

%build
export LDFLAGS="$LDFLAGS -lpthread"
%configure \
	--disable-static \
	--without-python
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%post -n libdrop_ambient%{ambient_sover} -p /sbin/ldconfig
%postun -n libdrop_ambient%{ambient_sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING.LIB
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{sover}.*

%files -n libdrop_ambient%{ambient_sover}
%{_libdir}/libdrop_ambient.so.%{ambient_sover}
%{_libdir}/libdrop_ambient.so.%{ambient_sover}.*

%files -n libdrop_ambient-devel
%{_libdir}/libdrop_ambient.so
%{_mandir}/man7/libdrop_ambient.7%{ext_man}

%files devel
%{_mandir}/man3/*.3%{ext_man}
%{_includedir}/cap-ng.h
%{_libdir}/%{name}.so
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/cap-ng.m4
%{_libdir}/pkgconfig/%{name}.pc

%files utils
%license COPYING
%{_bindir}/captest
%{_bindir}/filecap
%{_bindir}/netcap
%{_bindir}/pscap
%{_mandir}/man8/*.8%{ext_man}

%changelog
