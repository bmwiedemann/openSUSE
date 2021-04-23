#
# spec file for package metaio
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


%define shlib libmetaio1
# SECTION Adapt weird upstream versioning (8.5.0-v1) into something more RPM friendly
%define ver 8.5.0
%define rel 1
# /SECTION
Name:           metaio
Version:        %{ver}.%{rel}
Release:        0
Summary:        LIGO Light-Weight XML library
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
URL:            http://www.lsc-group.phys.uwm.edu/daswg/projects/metaio.html
Source:         https://git.ligo.org/lscsoft/metaio/-/archive/release-%{ver}-v%{rel}/metaio-release-%{ver}-v%{rel}.tar.bz2
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
This code implements a simple recursive-descent parsing scheme for LIGO_LW
files.

%package -n %{shlib}
Summary:        Shared library for libmetaio - LIGO Light-Weight XML library
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package contains the shared libraries needed for running libmetaio
applications.

%package devel
Summary:        Development files for libmetaio
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(zlib)

%description devel
This package contains the sources and header files needed for developing applications using libmetaio.

%package utils
Summary:        Command line tools for libmetaio
Group:          Productivity/Scientific/Physics

%description utils
This package contains command-line utilities such as lwtprint to be used with libmetaio.

%prep
%setup -q -n metaio-release-%{ver}-v%{rel}

%build
autoreconf -fvi
%configure --without-matlab
make %{?_smp_mflags}

%install
%make_install

# REMOVE STATIC LIB AND LIBTOOL ARCHIVE
find %{buildroot}%{_libdir}/ -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files devel
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files utils
%{_bindir}/*

%changelog
