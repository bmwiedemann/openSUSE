#
# spec file for package rk
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


%define soname lib%{name}0

Name:           rk
Version:        1.7
Release:        0
Summary:        A C++ library for relativistic kinematics
License:        X11
Group:          Development/Libraries/C and C++ 
Url:            https://rk.hepforge.org/
Source:         http://www.hepforge.org/archive/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} provides a C++ double precision implementation of several
basic geometric entities and transformations: points in 3d,
directions in 3d (unit vectors), 3-vectors, points in 4d,
4-vectors, rotations, linear transformations, and boosts. The main
purpose of the package is representing 4-momenta of relativistic
particles and related formulae.

%package -n %{soname}
Summary:        A C++ library for relativistic kinematics
Group:          Development/Libraries/C and C++ 

%description -n %{soname}
%{name} provides a C++ double precision implementation of several
basic geometric entities and transformations: points in 3d,
directions in 3d (unit vectors), 3-vectors, points in 4d,
4-vectors, rotations, linear transformations, and boosts. The main
purpose of the package is representing 4-momenta of relativistic
particles and related formulae.

This package provides the shared libraries required for %{name}.

%package devel
Summary:        A C++ library for relativistic kinematics
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}

%description devel
%{name} provides a C++ double precision implementation of several
basic geometric entities and transformations: points in 3d,
directions in 3d (unit vectors), 3-vectors, points in 4d,
4-vectors, rotations, linear transformations, and boosts. The main
purpose of the package is representing 4-momenta of relativistic
particles and related formulae.

This package provides the source files required for development
with %{name}.

%prep
%setup -q

%build
%configure --with-pic --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_libdir}/*.la

%post -n %{soname}
/sbin/ldconfig

%postun -n %{soname}
/sbin/ldconfig

%files devel
%defattr(-,root,root)
%doc AUTHORS LICENSE NEWS
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{soname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%changelog
