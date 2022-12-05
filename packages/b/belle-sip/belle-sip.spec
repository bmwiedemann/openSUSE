#
# spec file for package belle-sip
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Mariusz Fik <fisiu@opensuse.org>.
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


%define soname  libbellesip
%define sover   1
Name:           belle-sip
Version:        5.1.72
Release:        0
Summary:        C object-oriented SIP Stack
License:        GPL-3.0-or-later
Group:          Productivity/Telephony/SIP/Utilities
URL:            https://linphone.org/technical-corner/belle-sip/
Source:         https://gitlab.linphone.org/BC/public/belle-sip/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  belr-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 5.0.0
BuildRequires:  pkgconfig(zlib)

%description
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

%package -n %{soname}%{sover}
Summary:        C object-oriented SIP Stack
Group:          Productivity/Telephony/SIP/Utilities
Requires:       %{name}-data >= %{version}

%description -n %{soname}%{sover}
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

%package data
Summary:        Belle-sip data files
Group:          Productivity/Telephony/SIP/Utilities
Requires:       %{soname}%{sover} = %{version}
BuildArch:      noarch

%description data
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

This package contains data files such as belr grammar.

%package devel
Summary:        Headers and libraries for the belle-sip library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       pkgconfig(bctoolbox)
Requires:       pkgconfig(zlib)

%description devel
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

This package contains header files and development libraries needed
to develop applications using the belle-sip library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STRICT=OFF            \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

chrpath -d %{buildroot}%{_bindir}/belle_sip_tester %{buildroot}%{_libdir}/%{soname}.so.%{sover}*

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license LICENSE.txt
%{_libdir}/%{soname}.so.%{sover}*

%files data
%dir %{_datadir}/belr/
%{_datadir}/belr/grammars/

%files devel
%license LICENSE.txt
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/belle_sip_tester
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_libdir}/cmake/BelleSIP/
%{_datadir}/belle_sip_tester/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
