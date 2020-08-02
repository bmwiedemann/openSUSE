#
# spec file for package jthread
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

%define sover 1_3_3
%define libname libjthread%{sover}
Name:           jthread
Version:        1.3.3
Release:        0
Summary:        A thread wrapper library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://research.edm.uhasselt.be/jori/page/CS/Jthread.html
Source:         http://research.edm.uhasselt.be/jori/jthread/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
The JThread package provides some classes to make use of threads on
different platforms. The classes are actually wrappers around
existing thread implementations.

%package -n %{libname}
Summary:        A thread wrapper library
Group:          System/Libraries

%description -n %{libname}
The JThread package provides some classes to make use of threads on
different platforms. The classes are actually wrappers around
existing thread implementations.

%package devel
Summary:        Development files for libjthread
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The JThread package provides some classes to make use of threads on
different platforms. The classes are actually wrappers around
existing thread implementations.

This subpackage contains libraries and header files for developing
applications that want to make use of libjthread.

%prep
%setup -q

%build
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
%{_libdir}/libjthread.so.%{version}

%files -n jthread-devel
%{_includedir}/jthread
%{_libdir}/libjthread.so
%{_libdir}/pkgconfig/jthread.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/JThread
%{_libdir}/cmake/JThread/JThreadConfig.cmake

%changelog
