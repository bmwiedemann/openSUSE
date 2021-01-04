#
# spec file for package raylib
#
# Copyright (c) 2021 SUSE LLC
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


Name:           raylib
Version:        3.5.0
Release:        0
Summary:        C library for learning video game programming
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.raylib.com
Source:         https://github.com/raysan5/raylib/releases/download/%{version}/raylib-noexamples-%{version}.tar.gz
Patch0:         raylib-3.0.0-noexamples.patch
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
Requires:       libraylib351 = %{version}
Requires:       openal-soft-devel

%description -n raylib-devel
Development files and headers for %{name}.

%package -n libraylib351
Summary:        C library for learning video game programming
Group:          System/Libraries

%description -n libraylib351
A C library for learning video game programming.

%prep
%setup -q -n raylib-3.5.0
%patch0 -p1

%build
%cmake \
    -DPLATFORM=Desktop \
	-DSHARED=ON

%install
%cmake_install
for f in build/src/*.h; do
    install -Dm 644 "$f" "$RPM_BUILD_ROOT/usr/include/$(basename $f)"
done

%post -n libraylib351 -p /sbin/ldconfig
%postun -n libraylib351 -p /sbin/ldconfig

%files -n libraylib351
%{_libdir}/libraylib.so.*

%files -n raylib-devel
%license LICENSE
%doc CHANGELOG README.md
%{_includedir}/raylib.h
%{_includedir}/raudio.h
%{_includedir}/physac.h
%{_includedir}/raymath.h
%{_includedir}/rlgl.h
%{_libdir}/libraylib.so
%{_libdir}/pkgconfig/raylib.pc
%{_libdir}/cmake/raylib/

%changelog
