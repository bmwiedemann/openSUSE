#
# spec file for package geos
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


%define uver	3_8_1
Name:           geos
Version:        3.8.1
Release:        0
Summary:        Geometry Engine - Open Source
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://trac.osgeo.org/geos/
Source0:        https://download.osgeo.org/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}-config.1
Patch0:         libruby.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  ruby-devel
BuildRequires:  swig

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of JTS
in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid().

%package -n libgeos-%{uver}
Summary:        Geometry Engine library
Group:          System/Libraries

%description -n libgeos-%{uver}
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of JTS
in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid().

%package -n libgeos_c1
Summary:        C language interface for the GEOS library
Group:          System/Libraries
Provides:       geos = %{version}-%{release}
Obsoletes:      geos < %{version}-%{release}

%description -n libgeos_c1
This subpackage contains a shared library providing a C linkage
interface for the (C++) GEOS library.

%package -n ruby-%{name}
Summary:        Ruby bindings for Geometry Engine
Group:          Development/Languages/Ruby
Requires:       ruby(abi) >= %{rb_ver}

%description -n ruby-%{name}
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of
JTS in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid()

This package contains ruby bindings for Geometry Engine.

%package devel
Summary:        Development files for GEOS
Group:          Development/Libraries/C and C++
Requires:       libgeos-%{uver} = %{version}
Requires:       libgeos_c1 = %{version}
Provides:       lib%{name}-devel = %{version}

%description devel
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of
JTS in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid()

This package contains the development files to build applications that
use GEOS.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --disable-static \
  --enable-ruby

make %{?_smp_mflags}

# tests fail with older releases and non-intel architectures
# while this was reported to upstream, there has been no reply
%ifarch %{ix86} x86_64
%check
make %{?_smp_mflags} check
%endif

%install
%make_install
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_mandir}/man1/geos-config.1
# do not ship static libraries or la files
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
%fdupes %{buildroot}%{python_sitelib}

%post   -n libgeos-%{uver} -p /sbin/ldconfig
%postun -n libgeos-%{uver} -p /sbin/ldconfig
%post   -n libgeos_c1 -p /sbin/ldconfig
%postun -n libgeos_c1 -p /sbin/ldconfig

%files -n libgeos-%{uver}
%license COPYING
%{_libdir}/libgeos-%{version}.so

%files -n libgeos_c1
%license COPYING
%{_libdir}/libgeos_c.so.*

%files -n ruby-%{name}
%license COPYING
%{rb_vendorarchdir}/%{name}.so

%files devel
%license COPYING
%doc AUTHORS NEWS README.md ChangeLog
%{_mandir}/man1/%{name}-config.1%{ext_man}
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_c.so

%changelog
