#
# spec file for package laszip
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Bruno Friedmann, Ioda-Net Sàrl, Charmoille, Switzerland.
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


%define         sover 8
Name:           laszip
Version:        3.4.3
Release:        0
Summary:        Compression library supporting ASPRS LAS format data
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://laszip.org/
Source0:        https://github.com/LASzip/LASzip/releases/download/%{version}/laszip-src-%{version}.tar.gz
Source1:        https://github.com/LASzip/LASzip/releases/download/%{version}/laszip-src-%{version}.tar.gz.sha256sum
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A free product of rapidlasso GmbH - quickly turns bulky LAS files into
compact LAZ files without information loss. LASzip is a compression library that
was developed by Martin Isenburg for compressing ASPRS LAS format data in his
LAStools. It has been provided as an LGPL-licensed stand-alone software library
to allow other softwares that handle LAS data to read and write LASzip-compressed
data. The BSD-licensed libLAS and the LGPL-licensed LASlib can take advantage of
LASzip to read and write compressed data.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
A free product of rapidlasso GmbH - quickly turns bulky LAS files into
compact LAZ files without information loss. LASzip is a compression library that
was developed by Martin Isenburg for compressing ASPRS LAS format data in his
LAStools. It has been provided as an LGPL-licensed stand-alone software library
to allow other softwares that handle LAS data to read and write LASzip-compressed
data. The BSD-licensed libLAS and the LGPL-licensed LASlib can take advantage of
LASzip to read and write compressed data.

This package contain only the dynamic build.

%package -n lib%{name}_api%{sover}
Summary:        API library files for lib%{name}
# Packager comment are we sure this api can live alone ?
#Requires:       lib%%{name}%%{sover} = %%{version}
Group:          System/Libraries

%description -n lib%{name}_api%{sover}
API library for %{name}
This package contain only the dynamic build.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}_api%{sover} = %{version}

%description devel
Headers and development files for %{name} needed to develop
softwares that handle LAS data to read and write LASzip-compressed
data.

%prep
%setup -q -n laszip-src-%{version}

%build
# laszip need dlopen,dlsym,dlclose
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -Wl,--no-as-needed -ldl"

%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover}  -p /sbin/ldconfig
%post -n lib%{name}_api%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_api%{sover}  -p /sbin/ldconfig

%files devel
%license COPYING
%doc ChangeLog AUTHORS
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}_api_version.h
%{_includedir}/%{name}/%{name}_api.h
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_api.so

%files -n lib%{name}%{sover}
%doc ChangeLog AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}_api%{sover}
%doc ChangeLog AUTHORS
%license COPYING
%{_libdir}/lib%{name}_api.so.*

%changelog
