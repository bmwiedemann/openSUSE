#
# spec file for package rtrlib
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2019-2021, Martin Hauke <mardnh@gmx.de>
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


%define sover 0
Name:           rtrlib
Version:        0.8.0
Release:        0
Summary:        Extensible RPKI-RTR-Client C library
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://rpki.realmv6.org/
Source:         https://github.com/rtrlib/rtrlib/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         rtrlib-disable-tests-that-require-network-connections.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssh) >= 0.5.0

%description
RTRlib is a C implementation of the RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is extensible.

%package -n librtr%{sover}
Summary:        Extensible RPKI-RTR-Client C library
Group:          System/Libraries

%description -n librtr%{sover}
RTRlib is a C implementation of the RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is extensible.

%package -n rtr-tools
Summary:        RPKI-RTR command line tools
Group:          Productivity/Networking/Routing

%description -n rtr-tools
rtrclient is command line that connects to an RPKI-RTR server and prints
protocol information and information about the fetched ROAs to the console.
rpki-rov is a command line tool that connects to an RPKI-RTR server and
allows one to validate given IP prefixes and origin ASes.

%package devel
Summary:        Header files for librtr
Group:          Development/Libraries/C and C++
Requires:       librtr%{sover} = %{version}

%description devel
Development and header files for librtr.

%package devel-doc
Summary:        API documentation of the RTRlib
Group:          Documentation/Other
BuildArch:      noarch

%description devel-doc
This is the API documentation of the RTRlib, a C implementation of
the RPKI/Router Protocol client.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{optflags} -Wno-return-type"
%cmake
make %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/%{name}/docs/html %{buildroot}%{_docdir}/%{name}/html
%fdupes -s %{buildroot}/%{_docdir}/%{name}/html

%check
%ctest

%post   -n librtr%{sover} -p /sbin/ldconfig
%postun -n librtr%{sover} -p /sbin/ldconfig

%files -n librtr%{sover}
%license LICENSE
%doc CHANGELOG README.md
%{_libdir}/librtr.so.%{sover}*

%files -n rtr-tools
%{_bindir}/rpki-rov
%{_bindir}/rtrclient
%{_mandir}/man1/rpki-rov.1%{?ext_man}
%{_mandir}/man1/rtrclient.1%{?ext_man}

%files devel
%{_includedir}/rtrlib
%{_libdir}/librtr.so
%{_libdir}/pkgconfig/rtrlib.pc

%files devel-doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%changelog
