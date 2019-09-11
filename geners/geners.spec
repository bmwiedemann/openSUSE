#
# spec file for package geners
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define shlib lib%{name}0
Name:           geners
Version:        1.11.1
Release:        0
Summary:        Generic Serialization for C++
License:        X11
Group:          Development/Libraries/C and C++
Url:            http://geners.hepforge.org/
Source:         http://www.hepforge.org/archive/geners/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)

%description
The "geners" package is designed to address the problem of C++ object persistence in situations where the most typical data access pattern is "write once read many" (WORM). This access pattern is very common in scientific projects — a data recording device or a simulation program creates the original set of objects which is later reused (typically, for the purposes of data analysis and presentation of results) by other programs. "Geners" is, more or less, a set of tools and conventions which allows its users to develop C++ classes that can be converted to and from a storable stream of bytes in a well-organized and type-safe manner. Serialization of STL containers is supported, including the ones added in the C++11 standard. Independent versioning of each class definition is allowed.

%package -n %{shlib}
Summary:        Shared libraries for Geners
Group:          System/Libraries

%description -n %{shlib}
The "geners" package is designed to address the problem of C++ object persistence in situations where the most typical data access pattern is "write once read many" (WORM). This access pattern is very common in scientific projects — a data recording device or a simulation program creates the original set of objects which is later reused (typically, for the purposes of data analysis and presentation of results) by other programs. "Geners" is, more or less, a set of tools and conventions which allows its users to develop C++ classes that can be converted to and from a storable stream of bytes in a well-organized and type-safe manner. Serialization of STL containers is supported, including the ones added in the C++11 standard. Independent versioning of each class definition is allowed.

This package provides the shared libraries for Geners.

%package devel
Summary:        Sources and header files for Geners
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

%description devel
The "geners" package is designed to address the problem of C++ object persistence in situations where the most typical data access pattern is "write once read many" (WORM). This access pattern is very common in scientific projects — a data recording device or a simulation program creates the original set of objects which is later reused (typically, for the purposes of data analysis and presentation of results) by other programs. "Geners" is, more or less, a set of tools and conventions which allows its users to develop C++ classes that can be converted to and from a storable stream of bytes in a well-organized and type-safe manner. Serialization of STL containers is supported, including the ones added in the C++11 standard. Independent versioning of each class definition is allowed.

This package provides the sources and header files required for developing apps using geners.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name "*.la" -delete -print

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files devel
%doc AUTHORS LICENSE NEWS README
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
