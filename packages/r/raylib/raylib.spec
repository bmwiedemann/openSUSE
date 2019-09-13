#
# spec file for package raylib
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


Name:           raylib
Version:        2.5.0
Release:        0
Summary:        C library for learning video game programming
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.raylib.com
Source:         https://github.com/raysan5/raylib/archive/%{version}.tar.gz
BuildRequires:  Mesa-libGL-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel

%description
A C library for learning video game programming.
raylib is inspired by the Borland BGI graphics library and by the XNA framework.

%package -n raylib-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libraylib2 = %{version}
Requires:       openal-soft-devel

%description -n raylib-devel
Development files and headers for %{name}.

%package -n libraylib2
Summary:        C library for learning video game programming
Group:          System/Libraries

%description -n libraylib2
A C library for learning video game programming.

%prep
%setup -q -n raylib-2.5.0

%build
%cmake \
    -DPLATFORM=Desktop \
	-DSHARED=ON

%install
%cmake_install
#rm %{buildroot}%{_libdir}/libraylib.a

%post -n libraylib2 -p /sbin/ldconfig
%postun -n libraylib2 -p /sbin/ldconfig

%files -n libraylib2
%{_libdir}/libraylib.so.2
%{_libdir}/libraylib.so.2.5.0

%files -n raylib-devel
%license LICENSE.md
%doc CHANGELOG README.md
%{_includedir}/raylib.h
%{_libdir}/libraylib.so
%{_libdir}/pkgconfig/raylib.pc
%{_libdir}/cmake/raylib/

%changelog
