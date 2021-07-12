#
# spec file for package metaio
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


%define shlib libmetaio1
Name:           metaio
Version:        8.5.1
Release:        0
Summary:        LIGO Light-Weight XML library
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
URL:            https://www.lsc-group.phys.uwm.edu/daswg/projects/metaio.html
Source:         https://software.igwn.org/lscsoft/source/metaio-%{version}.tar.gz
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
%setup -q

%build
%configure --without-matlab --disable-static
%make_build

%install
%make_install

# REMOVE LIBTOOL ARCHIVE
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/libmetaio.so.*

%files devel
%doc AUTHORS README
%license COPYING
%{_libdir}/libmetaio.so
%{_libdir}/pkgconfig/libmetaio.pc
%{_includedir}/*

%files utils
%{_bindir}/*

%changelog
