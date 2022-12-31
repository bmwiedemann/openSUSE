#
# spec file for package nco
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


Name:           nco
Version:        5.1.3
%define  soname 5_1_3
%define  major  5
Release:        0
Summary:        Suite of programs for manipulating NetCDF/HDF files
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://github.com/nco/nco/
Source0:        https://github.com/nco/nco/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel >= 1.8.8
BuildRequires:  libaec-devel
BuildRequires:  libsz2-devel
BuildRequires:  netcdf
BuildRequires:  pkgconfig
BuildRequires:  texinfo
BuildRequires:  udunits2-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(netcdf) >= 4.1.3
BuildRequires:  pkgconfig(netcdf-cxx4) >= 4.1.3
BuildRequires:  pkgconfig(zlib)
%if 0%{?fedora_version}
%define ext_man .gz
%define ext_info .gz
BuildRequires:  antlr-C++
BuildRequires:  antlr-tool
BuildRequires:  java-headless
BuildRequires:  texinfo-tex
%else
BuildRequires:  antlr-devel
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
%endif

%description
The netCDF Operators, NCO, are a suite of command line programs to
facilitate manipulation and analysis of self-describing data stored
in the netCDF and HDF formats.

%package     -n lib%{name}-%{soname}
Summary:        Libraries for accessing %{name}
Group:          System/Libraries
Provides:       libnco = %{version}-%{release}
Provides:       libnco-%{major} = %{version}-%{release}

%description -n lib%{name}-%{soname}
The netCDF Operators, NCO, are a suite of command line programs to
facilitate manipulation and analysis of self-describing data stored
in the netCDF and HDF formats.

This package contains a shared library for accessing HDF and netCDF
files.

%package     -n lib%{name}_c++-%{soname}
Summary:        Libraries for accessing %{name}
Group:          System/Libraries
Provides:       libnco_c++ = %{version}-%{release}
Provides:       libnco_c++-%{major} = %{version}-%{release}

%description -n lib%{name}_c++-%{soname}
The netCDF Operators, NCO, are a suite of command line programs to
facilitate manipulation and analysis of self-describing data stored
in the netCDF and HDF formats.

This package contains a C++ shared library for accessing HDF and
netCDF files.

%package     -n lib%{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < %{version}-%{release}
Provides:       lib%{name}_c++-devel = %{version}-%{release}
Requires:       lib%{name}-%{soname} = %{version}-%{release}
Requires:       lib%{name}_c++-%{soname} = %{version}-%{release}
Recommends:     %{name} = %{version}-%{release}

%description -n lib%{name}-devel
The netCDF Operators, NCO, are a suite of command line programs to
facilitate manipulation and analysis of self-describing data stored
in the netCDF and HDF formats.

This package contains headers and development libraries needed to
build packages that use the lib%{name} HDF and netCDF library.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
The netCDF Operators, NCO, are a suite of command line programs to
facilitate manipulation and analysis of self-describing data stored
in the netCDF and HDF formats.

This package contains the documentation for %{name}.

%prep
%setup -q
# We need to enable the valarray check, so the c++ binding library gets build
sed -i 's|# AC_CXX_HAVE_VALARRAY|AC_CXX_HAVE_VALARRAY|' configure.ac

%build
autoconf
aclocal
automake --foreign
%configure \
    --disable-static \
    --prefix=%{_prefix} \
    --includedir=%{_includedir}/nco \
    --enable-nco_cplusplus \
    --disable-dependency-tracking USER=abuild HOST=OBS HOSTNAME=OBS

%make_build
pushd doc
    makeinfo --html --no-split nco.texi
    make nco.pdf
popd

%install
export QA_RPATHS=$((0x0001))  # check-rpaths: ignore standard RPATHs, for Fedora
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_infodir}/dir
# Fix shebangs
sed -i '1 s|.*env bash|#!/usr/bin/bash|' %{buildroot}%{_bindir}/{ncclimo,ncremap}

%check
%make_build check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/nco.info

%preun
if [ $1 -eq 0 ]; then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/nco.info
fi

%post -n lib%{name}-%{soname} -p /sbin/ldconfig
%postun -n lib%{name}-%{soname} -p /sbin/ldconfig
%post -n lib%{name}_c++-%{soname} -p /sbin/ldconfig
%postun -n lib%{name}_c++-%{soname} -p /sbin/ldconfig

%files
%license doc/LICENSE COPYING
%{_bindir}/ncap2
%{_bindir}/ncatted
%{_bindir}/ncbo
%{_bindir}/ncclimo
%{_bindir}/ncdiff
%{_bindir}/ncea
%{_bindir}/ncecat
%{_bindir}/nces
%{_bindir}/ncflint
%{_bindir}/ncks
%{_bindir}/ncpdq
%{_bindir}/ncra
%{_bindir}/ncrcat
%{_bindir}/ncremap
%{_bindir}/ncrename
%{_bindir}/ncwa
%{_bindir}/ncz2psx
%{_mandir}/man1/ncap2.1%{?ext_man}
%{_mandir}/man1/ncatted.1%{?ext_man}
%{_mandir}/man1/ncbo.1%{?ext_man}
%{_mandir}/man1/ncclimo.1%{?ext_man}
%{_mandir}/man1/ncecat.1%{?ext_man}
%{_mandir}/man1/nces.1%{?ext_man}
%{_mandir}/man1/ncflint.1%{?ext_man}
%{_mandir}/man1/ncks.1%{?ext_man}
%{_mandir}/man1/nco.1%{?ext_man}
%{_mandir}/man1/ncpdq.1%{?ext_man}
%{_mandir}/man1/ncra.1%{?ext_man}
%{_mandir}/man1/ncrcat.1%{?ext_man}
%{_mandir}/man1/ncremap.1%{?ext_man}
%{_mandir}/man1/ncrename.1%{?ext_man}
%{_mandir}/man1/ncwa.1%{?ext_man}
%{_mandir}/man1/ncz2psx.1%{?ext_man}
%{_infodir}/nco*.info%{?ext_info}
%{_infodir}/nco.info-*%{?ext_info}

%files doc
%license doc/LICENSE COPYING
%doc README doc/ANNOUNCE CITATION doc/TODO doc/ChangeLog doc/rtfm.txt
%doc doc/nco.pdf

%files -n lib%{name}-%{soname}
%license doc/LICENSE COPYING
%{_libdir}/libnco-*.so

%files -n lib%{name}_c++-%{soname}
%license doc/LICENSE COPYING
%{_libdir}/libnco_c++-*.so

%files -n lib%{name}-devel
%license doc/LICENSE COPYING
%{_libdir}/libnco.so
%{_libdir}/libnco_c++.so
%{_includedir}/nco/

%changelog
