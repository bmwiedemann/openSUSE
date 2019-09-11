#
# spec file for package jrtplib
#
# # Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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

%define sover 3_11_1
%define libname libjrtp%{sover}
Name:           jrtplib
Version:        3.11.1
Release:        0
Summary:        An object-oriented RTP library written in C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://research.edm.uhasselt.be/jori/page/CS/Jrtplib.html
Source:         http://research.edm.uhasselt.be/jori/jrtplib/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jthread)
BuildRequires:  pkgconfig(libsrtp)

%description
JRTPLIB is an object-oriented library written in C++ for making use of
the Real-time Transport Protocol (RTP) as described in RFC 3550.

%package -n %{libname}
Summary:        An object-oriented RTP library written in C++
Group:          System/Libraries

%description -n %{libname}
JRTPLIB is an object-oriented library written in C++ for making use of
the Real-time Transport Protocol (RTP) as described in RFC 3550.

%package devel
Summary:        Development files for libjrtp
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
JRTPLIB is an object-oriented library written in C++ for making use of
the Real-time Transport Protocol (RTP) as described in RFC 3550.

This subpackage contains libraries and header files for developing
applications that want to make use of libjrtp.

%prep
%setup -q

%build
export CXXFLAGS='%{optflags} -Wno-unused-result'
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm -f "%{buildroot}/%{_libdir}"/*.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.MIT
%doc ChangeLog README.md
%{_libdir}/libjrtp.so.%{version}

%files -n jrtplib-devel
%{_includedir}/jrtplib3
%{_libdir}/libjrtp.so
%{_libdir}/pkgconfig/jrtplib.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/JRTPLIB
%{_libdir}/cmake/JRTPLIB/JRTPLIBConfig.cmake

%changelog
