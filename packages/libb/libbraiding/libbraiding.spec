#
# spec file for package libbraiding
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libbraiding
%define lname	libbraiding0
Version:        1.1
Release:        0
Summary:        Library for computations on braid groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/miguelmarco/libbraiding
Source:         https://github.com/miguelmarco/libbraiding/releases/download/1.1/%name-%version.tar.gz
BuildRequires:  gcc-c++

%description
CBraid is a C++ library for various computations on braid groups,
such as normal forms.

%package -n %lname
Summary:        Library for computations on braid groups
Group:          System/Libraries

%description -n %lname
CBraid is a C++ library for various computations on braid groups,
such as normal forms.

%package devel
Summary:        Development files for the CBraid library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
CBraid is a C++ library for various computations on braid groups,
such as normal forms.

This subpackage provides the development headers for it.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libbraiding.so.0*

%files devel
%_libdir/libbraiding.so
%_includedir/*braid*.h

%changelog
