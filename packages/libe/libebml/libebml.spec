#
# spec file for package libebml
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname 4
Name:           libebml
Version:        1.3.9
Release:        0
Summary:        Library to parse EBML (Extensible Binary Markup Language) files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://www.matroska.org/
#Git-Clone:     git://github.com/Matroska-Org/libebml
#Git-Web:       https://github.com/Matroska-Org/libebml
Source:         https://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.xz
Source100:      baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
libebml is a C++ library to parse EBML files. See the EBML RFC at
http://www.matroska.org/technical/specs/rfc/index.html .

%package -n libebml%{soname}
Summary:        Library to parse EBML files
Group:          System/Libraries

%description -n libebml%{soname}
libebml is a C++ library to parse EBML files. See the EBML RFC at
http://www.matroska.org/technical/specs/rfc/index.html .

%package devel
Summary:        Development files for the EBML file parser library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libebml%{soname} = %{version}
Requires:       libstdc++-devel

%description devel
libebml is a C++ library to parse EBML files. See the EBML RFC at
http://www.matroska.org/technical/specs/rfc/index.html .

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n libebml%{soname} -p /sbin/ldconfig
%postun -n libebml%{soname} -p /sbin/ldconfig

%files -n libebml%{soname}
%{_libdir}/libebml.so.%{soname}*

%files devel
%{_libdir}/libebml.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/EBML
%{_includedir}/ebml/

%changelog
