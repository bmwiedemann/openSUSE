#
# spec file for package zix
#
# Copyright (c) 2025 SUSE LLC
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
Name:           zix
Version:        0.6.2
Release:        0
Summary:        A lightweight C library of portability wrappers and data structures
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://gitlab.com/drobilla/zix
Source0:        https://gitlab.com/drobilla/zix/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
Zix is a lightweight C library of portability wrappers and data structures, such as:
Allocation
Algorithms
Data Structures
Threading
File System

%package        -n libzix-0-%{sover}
Summary:        A lightweight C library of portability wrappers and data structures
Group:          Development/Libraries/C and C++

%description    -n libzix-0-%{sover}
Zix is a lightweight C library of portability wrappers and data structures, such as:
Allocation
Algorithms
Data Structures
Threading
File System

%package        devel
Summary:        Development files for zix library
Group:          Development/Libraries/C and C++
Requires:       libzix-0-%{sover} = %{version}

%description    devel
Zix is a lightweight C library of portability wrappers and data structures, such as:
Allocation
Algorithms
Data Structures
Threading
File System

%prep
%setup -q -n %{name}-v%{version}

%build
%meson -Ddocs=disabled
%meson_build

%install
%meson_install

%post -n libzix-0-%{sover} -p /sbin/ldconfig
%postun -n libzix-0-%{sover} -p /sbin/ldconfig

%files -n libzix-0-%{sover}
%{_libdir}/libzix-0.so.%{sover}
%{_libdir}/libzix-0.so.%{version}
%license COPYING
%doc README.md

%files devel
%{_includedir}/zix-0
%{_libdir}/libzix-0.so
%{_libdir}/pkgconfig/zix-0.pc

%changelog
