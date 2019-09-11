#
# spec file for package babl
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define debug_package_requires libbabl-0_1-0 = %{version}-%{release}

Name:           babl
Version:        0.1.66
Release:        0
Summary:        Dynamic Pixel Format Translation Library
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://gegl.org/babl/

Source0:        https://download.gimp.org/pub/babl/0.1/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf

BuildRequires:  pkgconfig
# None of these is needed for standard build:
#BuildRequires:  inkscape ruby w3m

%description
babl is a dynamic, any to any, pixel format translation library.

It allows converting between different methods of storing pixels known
as pixel formats that have with different bitdepths and other data
representations, color models and component permutations.

A vocabulary to formulate new pixel formats from existing primitives is
provided as well as the framework to add new color models and data
types.

%package -n libbabl-0_1-0
Summary:        Dynamic Pixel Format Translation Library
Group:          System/Libraries

%description -n libbabl-0_1-0
babl is a dynamic, any to any, pixel format translation library.

It allows converting between different methods of storing pixels known
as pixel formats that have with different bitdepths and other data
representations, color models and component permutations.

A vocabulary to formulate new pixel formats from existing primitives is
provided as well as the framework to add new color models and data
types.

%package devel
Summary:        Dynamic Pixel Format Translation Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libbabl-0_1-0 = %{version}

%description devel
babl is a dynamic, any to any, pixel format translation library.

It allows converting between different methods of storing pixels known
as pixel formats that have with different bitdepths and other data
representations, color models and component permutations.

A vocabulary to formulate new pixel formats from existing primitives is
provided as well as the framework to add new color models and data
types.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libbabl-0_1-0 -p /sbin/ldconfig
%postun -n libbabl-0_1-0 -p /sbin/ldconfig

%files -n libbabl-0_1-0
%license COPYING
%doc NEWS
%{_libdir}/*.so.*
%{_libdir}/babl-0.1/

%files devel
%doc AUTHORS README TODO
%{_includedir}/babl-0.1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
