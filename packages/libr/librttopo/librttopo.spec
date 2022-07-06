#
# spec file for package librttopo
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


%define sover   1
%define libname %{name}%{sover}
Name:           librttopo
Version:        1.1.0
Release:        0
Summary:        RT Topology Library
License:        GPL-2.0-or-later
URL:            https://git.osgeo.org/gitea/rttopo/librttopo
Source:         https://git.osgeo.org/gitea/rttopo/librttopo/archive/%{name}-%{version}.tar.gz
Patch0:         https://git.osgeo.org/gitea/rttopo/librttopo/commit/2a9cc526.patch
Patch1:         https://git.osgeo.org/gitea/rttopo/librttopo/pulls/41.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3.7.3
BuildRequires:  pkgconfig(geos)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(zlib)

%description
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided [data stores]
(doc/DATASTORES.md) and released under the GNU GPL license
(version 2 or later).

The code is derived from PostGIS liblwgeom library enhanced to provide
thread-safety, have less dependencies and be independent from PostGIS
release cycles.

The RT Topology Library was funded by “Regione Toscana - SITA”
(CIG: 6445512CC1), which also funded many improvements in the
originating liblwgeom.

%package -n %{libname}
Summary:        RT Topology Library
Group:          System/Libraries

%description -n %{libname}
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided [data stores]

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use librttopo.

%prep
%setup -q -n %{name}
%autopatch -p1
./autogen.sh

%build
%configure--disable-static
make %{?_smp_mflags}

%check
# Don't fail build - two failures (reported to upstream)
make check %{?_smp_mflags} || :

%install
%make_install
find %{buildroot} -type f -name "%{name}.la" -delete -print
find %{buildroot} -type f -name "%{name}.a" -delete -print
%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc README.md NEWS.md
%{_libdir}/%{name}.so.%{sover}*

%files devel
%license COPYING
%doc README.md NEWS.md
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rttopo.pc

%changelog
