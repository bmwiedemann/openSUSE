#
# spec file for package uchardet
#
# Copyright (c) 2022 SUSE LLC
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


%define major   0
Name:           uchardet
Version:        0.0.8
Release:        0
Summary:        Universal Charset Detection Library
License:        GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.freedesktop.org/wiki/Software/uchardet/
Source0:        https://www.freedesktop.org/software/%{name}/releases/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
uchardet is a C language binding of the original C++ implementation of
the universal charset detection library by Mozilla.

uchardet is an encoding detector library, which takes a sequence of
bytes in an unknown character encoding without any additional
information, and attempts to determine the encoding of the text.

%package -n libuchardet%{major}
Summary:        Universal Charset Detection Library
Group:          System/Libraries

%description -n libuchardet%{major}
uchardet is a C language binding of the original C++ implementation of
the universal charset detection library by Mozilla.

uchardet is an encoding detector library, which takes a sequence of
bytes in an unknown character encoding without any additional
information, and attempts to determine the encoding of the text.

This package contains the shared library.

%package -n libuchardet-devel
Summary:        Universal Charset Detection Library
Group:          Development/Libraries/C and C++
Requires:       libuchardet%{major} = %{version}

%description -n libuchardet-devel
uchardet is a C language binding of the original C++ implementation of
the universal charset detection library by Mozilla.

uchardet is an encoding detector library, which takes a sequence of
bytes in an unknown character encoding without any additional
information, and attempts to determine the encoding of the text.

This package contains the development files.

%prep
%setup -q

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
%make_install
popd
rm -f %{buildroot}%{_libdir}/libuchardet.a

%post -n libuchardet%{major} -p /sbin/ldconfig

%postun -n libuchardet%{major} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_mandir}/man?/*

%files -n libuchardet%{major}
%{_libdir}/*.so.*

%files -n libuchardet-devel
%license COPYING
%doc AUTHORS
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/uchardet

%changelog
