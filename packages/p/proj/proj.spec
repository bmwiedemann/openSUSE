#
# spec file for package proj
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define data_version 1.23
%define sover   25
%define libname lib%{name}%{sover}
Name:           proj
Version:        9.7.0
Release:        0
Summary:        Cartographic projection software
License:        MIT
URL:            https://proj.org/
# Download from GitHub, osgeo.org appears to be slow and flaky at the moment
Source0:        https://github.com/OSGeo/PROJ/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/OSGeo/PROJ-data/releases/download/%{data_version}.0/%{name}-data-%{data_version}.tar.gz
BuildRequires:  cmake >= 3.16
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  sqlite3
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(sqlite3) >= 3.11
Provides:       libproj = %{version}

%description
This package offers the commandline tools for performing respective
forward and inverse transformation of cartographic data to or from cartesian
data with a wide range of selectable projection functions.

%package -n %{libname}
Summary:        Cartographic projection software
License:        MIT

%description -n %{libname}
This package the library for performing respective
forward and inverse transformation of cartographic data to or from cartesian
data with a wide range of selectable projection functions.

%package devel
Summary:        Development files for PROJ
License:        MIT
Requires:       %{libname} = %{version}
Provides:       libproj-devel = %{version}
Obsoletes:      libproj-devel < %{version}

%description devel
This package contains libproj and the appropriate header files and man pages.

%define data_subpkg(c:n:e:s:) \
%define countrycode %{-c:%{-c*}}%{!-c:%{error:Country code not defined}} \
%define countryname %{-n:%{-n*}}%{!-n:%{error:Country name not defined}} \
%define extrafile %{-e:%{_datadir}/%{name}/%{-e*}} \
%define wildcard %{!-s:%{_datadir}/%{name}/%{countrycode}_*} \
\
%package data-%{countrycode}\
Summary:      %{countryname} datum grids for Proj\
BuildArch:    noarch\
# See README.DATA \
License:      BSD-2-Clause AND CC0-1.0 AND CC-BY-4.0 AND CC-BY-SA-4.0 AND SUSE-Public-Domain \
Supplements:  proj\
\
%description data-%{countrycode}\
%{countryname} datum grids for Proj.\
\
%files data-%{countrycode}\
%{wildcard}\
%{extrafile}
License:        MIT
%data_subpkg -c ar -n Argentina
%data_subpkg -c at -n Austria
%data_subpkg -c au -n Australia
%data_subpkg -c be -n Belgium
%data_subpkg -c br -n Brasil
%data_subpkg -c ca -n Canada
%data_subpkg -c ch -n Switzerland
%data_subpkg -c de -n Germany
%data_subpkg -c dk -n Denmark -e DK
%data_subpkg -c es -n Spain
%data_subpkg -c eur -n %{quote:Nordic + Baltic} -e NKG
%data_subpkg -c fi -n Finland
%data_subpkg -c fo -n %{quote:Faroe Island} -e FO -s 1
%data_subpkg -c fr -n France
%data_subpkg -c hu -n Hungary
%data_subpkg -c is -n Island -e ISL
%data_subpkg -c lv -n Latvia
%data_subpkg -c jp -n Japan
%data_subpkg -c mx -n Mexico
%data_subpkg -c nc -n %{quote:New Caledonia}
%data_subpkg -c nl -n Netherlands
%data_subpkg -c no -n Norway
%data_subpkg -c nz -n %{quote:New Zealand}
%data_subpkg -c pl -n Poland
%data_subpkg -c pt -n Portugal
%data_subpkg -c se -n Sweden
%data_subpkg -c sk -n Slovakia
%data_subpkg -c uk -n %{quote:United Kingdom}
%data_subpkg -c us -n %{quote:United States}
%data_subpkg -c za -n %{quote:South Africa}

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=gcc-13
export CXX=g++-13
%endif
# c++14 needed to build tests using gtest >= 1.14
%cmake \
%if 0%{?suse_version} >= 1600
  -DCMAKE_CXX_STANDARD=14 \
%endif
  %{nil}
%cmake_build

%install
%cmake_install
tar -C %{buildroot}%{_datadir}/%{name} -xf %{SOURCE1}
find %{buildroot} -type f -name "*.la" -delete -print
# It would be good to find out where these extra files
# come from:
rm -rf %{buildroot}%{_datadir}/doc/${name}

%check
# Tests dont work on i586 and noone cares
%ifnarch %{ix86}
%ctest
%endif

%ldconfig_scriptlets -n %{libname}

%files
%doc NEWS.md AUTHORS.md README.md ChangeLog
%defattr(0755,root,root)
%{_bindir}/cs2cs
%{_bindir}/cct
%{_bindir}/gie
%{_bindir}/geod
%{_bindir}/invgeod
%{_bindir}/invproj
%{_bindir}/proj
%{_bindir}/projsync
%{_bindir}/projinfo
%defattr(0644,root,root)
%{_mandir}/man1/cs2cs.1%{?ext_man}
%{_mandir}/man1/geod.1%{?ext_man}
%{_mandir}/man1/proj.1%{?ext_man}
%{_mandir}/man1/cct.1%{?ext_man}
%{_mandir}/man1/gie.1%{?ext_man}
%{_mandir}/man1/projinfo.1%{?ext_man}
%{_mandir}/man1/projsync.1%{?ext_man}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/proj.ini
%{_datadir}/%{name}/copyright_and_licenses.csv
%{_datadir}/%{name}/CH
%{_datadir}/%{name}/GL27
%{_datadir}/%{name}/ITRF2000
%{_datadir}/%{name}/ITRF2008
%{_datadir}/%{name}/ITRF2014
%{_datadir}/%{name}/ITRF2020
%{_datadir}/%{name}/README.DATA
%{_datadir}/%{name}/cz_cuzk_CR-2005.tif
%{_datadir}/%{name}/cz_cuzk_README.txt
%{_datadir}/%{name}/deformation_model.schema.json
%{_datadir}/%{name}/nad.lst
%{_datadir}/%{name}/nad27
%{_datadir}/%{name}/nad83
%{_datadir}/%{name}/other.extra
%{_datadir}/%{name}/proj.db
%{_datadir}/%{name}/projjson.schema.json
%{_datadir}/%{name}/triangulation.schema.json
%{_datadir}/%{name}/world
%{_datadir}/%{name}/si_gurs_README.txt
%{_datadir}/%{name}/si_gurs_SLO-VRP2016-Koper.tif
%{_datadir}/%{name}/si_gurs_SLO-VTP2024.tif
%{_datadir}/bash-completion/completions/projinfo

%files -n %{libname}
%license COPYING
%{_libdir}/libproj.so.%{sover}*

%files devel
%{_includedir}/*.h
%{_includedir}/proj
%{_libdir}/libproj.so
%dir %{_libdir}/cmake/proj/
%{_libdir}/cmake/proj/*.cmake
%dir %{_libdir}/cmake/proj4/
%{_libdir}/cmake/proj4/*.cmake
%{_libdir}/pkgconfig/proj.pc

%changelog
