#
# spec file for package c++utilities
#
# Copyright (c) 2026 SUSE LLC
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


%define reponame c++utilities
%define soname 5

Name:           %{reponame}
Version:        5.34.2
Release:        0
Summary:        Common C++ classes and routines
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/Martchus/cpp-utilities
Source:         https://github.com/Martchus/cpp-utilities/archive/v%{version}/cpp-utilities-%{version}.tar.gz
BuildRequires:  cmake >= 3.17
%if 0%{?fedora}
%else
BuildRequires:  ninja
%endif
BuildRequires:  cppunit-devel >= 1.14.0
%if 0%{?sle_version} && 0%{?sle_version} < 160000
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package -n lib%{reponame}%{soname}
Summary:        Common C++ classes and routines
Group:          System/Libraries

%description -n lib%{reponame}%{soname}
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package devel
Summary:        Devel files for %{reponame}
Group:          Development/Libraries/C and C++
Requires:       cmake >= 3.9
Requires:       glibc-devel
Requires:       lib%{reponame}%{soname} = %{version}
Requires:       libstdc++-devel
Requires:       doxygen
Requires:       pkg-config

%description devel
Development files for %{reponame}

%prep
%setup -q -n cpp-utilities-%{version}

%build
%if 0%{?sle_version} && 0%{?sle_version} < 160000
export CC=gcc-9
export CXX=g++-9
%endif
%if 0%{?fedora}
%else
%define __builder ninja
%endif
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON
%if 0%{?fedora} && 0%{?fedora_version} < 33
make %{?_smp_mflags}
%else
%cmake_build
%endif

%check
%if 0%{?fedora}
%if 0%{?fedora_version} < 33
make %{?_smp_mflags} check
%else
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check
%endif
%else
%if (0%{?sle_version} == 150200 || 0%{?sle_version} == 150300) && 0%{?is_opensuse}
# FIXME: fix tests under Leap 15.2 which fail at some point with "1/1 Test #1: ...........***Exception: SegFault  0.02 sec"
%else
cd "%{__builddir}"
export LD_LIBRARY_PATH="$PWD:$LD_LIBRARY_PATH"
%cmake_build check
%endif
%endif

%install
%if 0%{?fedora} && 0%{?fedora_version} < 33
DESTDIR=%{buildroot} make %{?_smp_mflags} install
%else
%cmake_install
%endif

%post -n lib%{reponame}%{soname} -p /sbin/ldconfig
%postun -n lib%{reponame}%{soname} -p /sbin/ldconfig

%files -n lib%{reponame}%{soname}
%license LICENSE
%{_libdir}/lib%{reponame}.so.%{soname}*

%files devel
%doc README.md
%{_includedir}/%{reponame}
%{_datadir}/%{reponame}
%{_libdir}/pkgconfig/%{reponame}.pc
%{_libdir}/lib%{reponame}.so

%changelog
