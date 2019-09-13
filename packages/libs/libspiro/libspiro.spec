#
# spec file for package libspiro
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libspiro
Version:        0.5.20150702
Release:        0
Summary:        A clothoid to bezier spline converter
License:        GPL-2.0+
Group:          System/Libraries
Source0:        https://github.com/fontforge/libspiro/archive/%{version}.tar.gz
Url:            https://github.com/fontforge/libspiro
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
libspiro contains routines which will convert an array of clothoid
spline control points into an equivalent set of bezier control points.

%package -n %{name}0
Summary:        A clothoid to bezier spline converter
Group:          System/Libraries

%description -n %{name}0
libspiro contains routines which will convert an array of clothoid
spline control points into an equivalent set of bezier control points.

%package devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}0 = %{version} glibc-devel

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use %{name}.


%prep
%setup -q

%build
autoreconf -i
automake --foreign -Wall
%configure --with-pic\
           --disable-static
make %{?smp_mflags}

%install
%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig

%files -n %{name}0
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README* 
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
