#
# spec file for package libspiro
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


%define sonum   1
Name:           libspiro
Version:        20221101
Release:        0
Summary:        A clothoid to bezier spline converter
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://github.com/fontforge/libspiro
Source0:        https://github.com/fontforge/libspiro/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libspiro contains routines which will convert an array of clothoid
spline control points into an equivalent set of bezier control points.

%package -n %{name}%{sonum}
Summary:        A clothoid to bezier spline converter
Group:          System/Libraries

%description -n %{name}%{sonum}
libspiro contains routines which will convert an array of clothoid
spline control points into an equivalent set of bezier control points.

%package devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}1 = %{version}
Requires:       glibc-devel

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
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig

%files -n %{name}%{sonum}
%license COPYING
%doc ChangeLog README*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/libspiro.3%{?ext_man}
%{_libdir}/pkgconfig/*.pc

%changelog
