#
# spec file for package Rivet
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


%define so_name lib%{name}-3_1_1
Name:           Rivet
Version:        3.1.1
Release:        0
Summary:        A toolkit for validation of Monte Carlo event generators
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
URL:            https://rivet.hepforge.org/
Source:         http://www.hepforge.org/archive/rivet/%{name}-%{version}.tar.gz
Patch0:         sover.diff
BuildRequires:  HepMC-devel >= 3.0
BuildRequires:  YODA-devel >= 1.8.0
BuildRequires:  doxygen
BuildRequires:  fastjet-contrib-devel
BuildRequires:  fastjet-devel
BuildRequires:  fastjet-plugin-siscone-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  rsync
BuildRequires:  texlive-latex-bin
BuildRequires:  yaml-cpp-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(zlib)

%description
The Rivet project (Robust Independent Validation of Experiment and
Theory) is a toolkit for validation of Monte Carlo event generators.
It provides a large (and ever growing) set of experimental analyses
useful for MC generator development, validation, and tuning, as well
as a convenient infrastructure for adding your own analyses. Rivet is
the most widespread way by which analysis code from the LHC and other
high-energy collider experiments is preserved for comparison to and
development of future theory models.

%package -n %{so_name}
Summary:        A toolkit for validation of Monte Carlo event generators
Group:          System/Libraries

%description -n %{so_name}
The Rivet project (Robust Independent Validation of Experiment and
Theory) is a toolkit for validation of Monte Carlo event generators.
It provides a large (and ever growing) set of experimental analyses
useful for MC generator development, validation, and tuning, as well
as a convenient infrastructure for adding your own analyses. Rivet is
the most widespread way by which analysis code from the LHC and other
high-energy collider experiments is preserved for comparison to and
development of future theory models.

This package provides the shared libraries for %{name}.

%package devel
Summary:        A toolkit for validation of Monte Carlo event generators
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}
Requires:       YODA-devel >= 1.8.0

%description devel
The Rivet project (Robust Independent Validation of Experiment and
Theory) is a toolkit for validation of Monte Carlo event generators.
It provides a large (and ever growing) set of experimental analyses
useful for MC generator development, validation, and tuning, as well
as a convenient infrastructure for adding your own analyses. Rivet is
the most widespread way by which analysis code from the LHC and other
high-energy collider experiments is preserved for comparison to and
development of future theory models.

This package provides the source files for development with %{name}.

%package -n python3-%{name}
Summary:        A toolkit for validation of Monte Carlo event generators
Group:          Productivity/Scientific/Physics
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < %{version}

%description -n python3-%{name}
The Rivet project (Robust Independent Validation of Experiment and
Theory) is a toolkit for validation of Monte Carlo event generators.
It provides a large (and ever growing) set of experimental analyses
useful for MC generator development, validation, and tuning, as well
as a convenient infrastructure for adding your own analyses. Rivet is
the most widespread way by which analysis code from the LHC and other
high-energy collider experiments is preserved for comparison to and
development of future theory models.

This package provides the python bindings for %{name}.

%package plugins
Summary:        A collection of analyses plugins for %{name}
Group:          Productivity/Scientific/Physics
Requires:       %{name}-devel = %{version}

%description plugins
The Rivet project (Robust Independent Validation of Experiment and
Theory) is a toolkit for validation of Monte Carlo event generators.
It provides a large (and ever growing) set of experimental analyses
useful for MC generator development, validation, and tuning, as well
as a convenient infrastructure for adding your own analyses. Rivet is
the most widespread way by which analysis code from the LHC and other
high-energy collider experiments is preserved for comparison to and
development of future theory models.

This package provides all the analysis plugins for %{name}.

%prep
%autosetup -p1

# REMOVE EXISTING rivet.pc FILE, ALLOW make TO GENERATE rivet.pc FROM rivet.pc.in
rm -f rivet.pc

# REMOVE INCORRECT LIBDIRS FROM .pc.in FILE (the right libdirs are already present)
sed -i "s| -L@GSLLIBPATH@||g" rivet.pc.in
sed -i "s| -L@GSLINCPATH@||g" rivet.pc.in

%build
autoreconf -fvi
export PYTHON_VERSION=%{py3_ver}
%configure --with-hepmc3 \
           --with-hepmc3-libname=HepMC3 \
           --with-hepmc3-libpath=%{_libdir}/ \
           --with-hepmc3-incpath=%{_includedir}/ \
           --docdir=%{_docdir}/%{name}/
make %{?_smp_mflags}

%install
%make_install

# SECTION Fix env based hashbangs in binaries
sed -Ei "1s:^#!\s*%{_bindir}/env python:#!%{_bindir}/python3:" %{buildroot}%{_bindir}/*
sed -Ei "1s:^#!\s*%{_bindir}/env bash:#!/bin/bash:" %{buildroot}%{_bindir}/*
# /SECTION

# SECTION Remove rpaths from config binaries and pkgconfig file
sed -i "s|-Wl,-rpath,||g" %{buildroot}%{_bindir}/rivet-config
# /SECTION

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-plugins.conf

chmod -x %{buildroot}%{_datadir}/Rivet/ALICE_2012_I1126966.info \
        %{buildroot}%{_datadir}/Rivet/ALICE_2014_I1243865.info \
        %{buildroot}%{_datadir}/Rivet/STAR_2017_I1510593.{info,plot}
sed -E -i '1{/^#!.*env python/d}' %{buildroot}%{python3_sitearch}/rivet/spiresbib.py

%fdupes %{buildroot}%{_datadir}/Rivet/

%post -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%{_libdir}/libRivet-*.so

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_bindir}/rivet-config
%{_bindir}/rivet-buildplugin
%{_includedir}/%{name}/
%{_datadir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/rivet.pc

%files -n python3-%{name}
%license COPYING
%{_bindir}/*
%exclude %{_bindir}/rivet-config
%exclude %{_bindir}/rivet-buildplugin
%{python3_sitearch}/rivet/
%{python3_sitearch}/rivet-*egg-info

%files plugins
%license COPYING
%config %{_sysconfdir}/ld.so.conf.d/%{name}-plugins.conf
%{_libdir}/%{name}/

%changelog
