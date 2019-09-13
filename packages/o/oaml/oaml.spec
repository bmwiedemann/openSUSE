#
# spec file for package oaml
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


%define lname lib%{name}_shared1
Name:           oaml
Version:        1.2
Release:        0
Summary:        Open Adaptive Music Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/marcelofg55/oaml/
Source:         https://github.com/marcelofg55/oaml/archive/v%{version}/oaml-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OAML is a library for implementing adaptive music in games.

%package devel
Summary:        Development files for OAML, the Open Adaptive Music library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
OAML is a library for implementing adaptive music in games.
This package contains the development files for oaml.

%package -n %{lname}
Summary:        Open Adaptive Music library
Group:          System/Libraries

%description -n %{lname}
OAML is a library for implementing adaptive music in games.
This package contains the shared library.

%prep
%setup -q

%build
%cmake -DENABLE_STATIC=OFF
make %{?_smp_mflags}

%install
%cmake_install

%post -n %{lname}   -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc LICENSE.md
%{_libdir}/lib%{name}_shared.so.*

%files devel
%defattr(-,root,root)
%doc README.md
%{_includedir}/oaml.h
%{_libdir}/lib%{name}_shared.so

%changelog
