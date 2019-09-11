#
# spec file for package libical
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sonum   3
Name:           libical
Version:        3.0.5
Release:        0
Summary:        An Implementation of Basic iCAL Protocols
License:        MPL-2.0 OR LGPL-2.1-only
Group:          Development/Libraries/C and C++
Url:            http://sourceforge.net/projects/freeassociation/
#Git-Clone:     https://github.com/libical/libical
Source:         https://github.com/libical/libical/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         0001-vcc.y-factor-out-hexdigit-conversion.patch
Patch2:         0002-vcc.y-fix-infinite-loop-with-lower-case-hex-digits.patch
Patch3:         0003-vcc.y-fix-infinite-loop-with-non-hex-digits.patch
Patch4:         0004-vobject.c-vCard-Unicode-reading-support.patch
Patch5:         0005-vcc.y-do-not-ignore-field-separator-in-QUOTED-PRINTA.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(icu-i18n)

%description
Libical is an implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package -n %{name}%{sonum}
Summary:        An Implementation of Basic iCAL Protocols
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{name}%{sonum}
Libical is an implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package devel
Summary:        Development files for libical, an implementation of basic iCAL protocols
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sonum} = %{version}

%description devel
Libical is an implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package doc
Summary:        Example source code for programs to use libical
Group:          Documentation/Other
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
Libical is an implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%prep
%autosetup -p1

%build
%cmake -DICAL_GLIB=false -DSHARED_ONLY=true
make -j1

%install
%cmake_install
rm examples/CMakeLists.txt

%post -n %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig

%files -n %{name}%{sonum}
%license COPYING
%doc AUTHORS ReadMe.txt ReleaseNotes.txt TEST THANKS TODO
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libical.pc
%{_includedir}/libical/
%{_libdir}/cmake/LibIcal/

%files doc
%doc doc/*.txt
%doc examples/

%changelog
