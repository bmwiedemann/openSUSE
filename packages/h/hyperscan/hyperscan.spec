#
# spec file for package hyperscan
#
# Copyright (c) 2024 SUSE LLC
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


%define _lto_cflags %{nil}
%define sover 5
Name:           hyperscan
Version:        5.4.0
Release:        0
Summary:        Regular expression matching library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.hyperscan.io/
#Git-Clone:     https://github.com/intel/hyperscan.git
Source:         https://github.com/intel/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  boost-devel >= 1.57
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  ragel
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(sqlite3)
ExclusiveArch:  %{ix86} x86_64

%description
Hyperscan is a multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

%package -n libhs%{sover}
Summary:        Regular expression matching library
Group:          System/Libraries

%description -n libhs%{sover}
Hyperscan is a multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

%package devel
Summary:        Libraries and header files for the hyperscan library
Group:          Development/Libraries/C and C++
Requires:       libhs%{sover} = %{version}

%description devel
Hyperscan is a multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

This package provides the libraries, include files and other resources
needed for developing Hyperscan applications.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} \
  -DBUILD_AVX512=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libhs%{sover}

%files -n libhs%{sover}
%license COPYING LICENSE
%{_libdir}/libhs.so.%{sover}*
%{_libdir}/libhs_runtime.so.%{sover}*

%files devel
%{_libdir}/libhs.so
%{_libdir}/libhs_runtime.so
%{_libdir}/pkgconfig/libhs.pc
%{_includedir}/hs/
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/examples/README.md
%doc %{_defaultdocdir}/%{name}/examples/*.cc
%doc %{_defaultdocdir}/%{name}/examples/*.c

%changelog
