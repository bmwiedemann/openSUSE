#
# spec file for package Box2D
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 Adam Mizerski <adam@mizerski.pl>
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


%define major 2
%define libname libbox2d
Name:           Box2D
Version:        2.4.1
Release:        0
Summary:        A 2D Physics Engine for Games
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://box2d.org/
Source0:        https://github.com/erincatto/box2d/archive/v%{version}.tar.gz#/box2d-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake >= 3
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libglfw-devel

%description
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%package -n %{libname}%{major}
Summary:        A 2D Physics Engine for Games
Group:          System/Libraries

%description -n %{libname}%{major}
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%package -n %{libname}-devel
Summary:        A 2D Physics Engine for Games
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{major} = %{version}

%description -n %{libname}-devel
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%prep
%setup -q -n box2d-%{version}

%build
%cmake \
       -DBOX2D_BUILD_UNIT_TESTS=OFF
%make_build

%install
%cmake_install

%post -n %{libname}%{major} -p /sbin/ldconfig
%postun -n %{libname}%{major} -p /sbin/ldconfig

%files -n %{libname}%{major}
%license LICENSE
%doc README.md
%{_libdir}/%{libname}.so.%{major}
%{_libdir}/%{libname}.so.%{version}

%files -n %{libname}-devel
%{_includedir}/box2d
%{_libdir}/%{libname}.so
%{_libdir}/cmake/box2d

%changelog
