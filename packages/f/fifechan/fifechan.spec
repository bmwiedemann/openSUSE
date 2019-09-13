#
# spec file for package fifechan
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Matthias Bach <marix@marix.org>.
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


%define sover 0_1_5
Name:           fifechan
Version:        0.1.5
Release:        0
Summary:        A C++ GUI library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://fifengine.github.io/%{name}/
Source:         https://github.com/fifengine/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fifechan is a C++ GUI library designed for games.
It comes with a standard set of widgets and can use several different
objects for displaying graphics and capturing user input.

%package -n lib%{name}%{sover}
Summary:        Main library of the Fifechan GUI toolkit
Group:          System/Libraries

%description -n lib%{name}%{sover}
Main shared library of fifechan.

%package -n lib%{name}_opengl%{sover}
Summary:        OpenGL extension library of the Fifechan GUI toolkit
Group:          System/Libraries

%description -n lib%{name}_opengl%{sover}
OpenGL extension for the fifechan library.

%package -n lib%{name}_sdl%{sover}
Summary:        SDL extension library of the Fifechan GUI toolkit
Group:          System/Libraries

%description -n lib%{name}_sdl%{sover}
SDL extension for the fifechan library.

%package devel
Summary:        Header files for fifechan
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}_opengl%{sover} = %{version}
Requires:       lib%{name}_sdl%{sover} = %{version}

%description devel
Development files, such as headers, needed when building packages using fifechan.

%prep
%setup -q

%build
%cmake \
    -DBUILD_FIFECHAN_SHARED=ON \
    -DENABLE_OPENGL=ON \
    -DENABLE_OPENGL_CONTRIB=OFF \
    -DBUILD_FIFECHAN_OPENGL_SHARED=ON \
    -DENABLE_SDL=ON \
    -DENABLE_SDL_CONTRIB=ON \
    -DBUILD_FIFECHAN_SDL_SHARED=ON
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%post -n lib%{name}%{sover}          -p /sbin/ldconfig
%post -n lib%{name}_opengl%{sover}   -p /sbin/ldconfig
%post -n lib%{name}_sdl%{sover}      -p /sbin/ldconfig
%postun -n lib%{name}%{sover}          -p /sbin/ldconfig
%postun -n lib%{name}_opengl%{sover}   -p /sbin/ldconfig
%postun -n lib%{name}_sdl%{sover}      -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%defattr(-,root,root)
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Leap 42.1 or SLE
%doc LICENSE.md AUTHORS
%else
%license LICENSE.md AUTHORS
%endif
%{_libdir}/libfifechan.so.*

%files -n lib%{name}_opengl%{sover}
%defattr(-,root,root)
%{_libdir}/libfifechan_opengl.so.*

%files -n lib%{name}_sdl%{sover}
%defattr(-,root,root)
%{_libdir}/libfifechan_sdl.so.*

%files devel
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%{_includedir}/fifechan
%{_includedir}/fifechan.hpp
%{_libdir}/libfifechan*.so

%changelog
