#
# spec file for package Rivet
#
# Copyright (c) 2023 SUSE LLC
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


%define ver 3.1.7
%define so_name lib%{name}-%(echo %{ver} | tr '.' '_')
Name:           Rivet
Version:        %{ver}
Release:        0
Summary:        A toolkit for validation of Monte Carlo event generators
License:        GPL-2.0-only
URL:            https://rivet.hepforge.org/
Source:         http://www.hepforge.org/archive/rivet/%{name}-%{version}.tar.gz
Patch0:         sover.diff
# PATCH-FEATURE-OPENSUSE Rivet-correct-python-platlib.patch badshah400@gmail.com -- Use consistent platlib across multiple python versions
Patch1:         Rivet-correct-python-platlib.patch
BuildRequires:  HepMC-devel >= 3.0
BuildRequires:  YODA-devel >= 1.8.0
BuildRequires:  bash-completion
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

%package data
Summary:        Data files for Rivet
BuildArch:      noarch

%description data
The Rivet project (Robust Independent Validation of Experiment and
Theory) is a toolkit for validation of Monte Carlo event generators.

This package provides common data files for Rivet used by both C++
and Python bindings.

%package devel
Summary:        A toolkit for validation of Monte Carlo event generators
Requires:       %{name}-data = %{version}
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
Requires:       %{name}-data = %{version}
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
rm rivet.pc

# SECTION Fix/drop env based hashbangs in binaries as appropriate
# Need to do this here rather than post-install in buildroot for tests in %%check to succeed
sed -Ei "1s:^#!\s*%{_bindir}/env bash:#!/bin/bash:" ./bin/*
sed -Ei "1s:^#!\s*%{_bindir}/env python:#!%{_bindir}/python3:" \
  ./bin/* \
  ./pyext/build.py.in
sed -E -i '1{/^#!.*env python/d}' \
          ./pyext/rivet/spiresbib.py \
          ./analyses/pluginLHCb/LHCB_201*_ratios.py
# /SECTION

%build
autoreconf -fvi
export PYTHON_VERSION=%{py3_ver}
%configure --with-hepmc3 \
           --with-hepmc3-libname=HepMC3 \
           --with-hepmc3-libpath=%{_libdir}/ \
           --with-hepmc3-incpath=%{_includedir}/ \
           --docdir=%{_docdir}/%{name}/
%make_build

%install
export PYTHONPATH+=':%{buildroot}%{_libdir}/python%{py3_ver}/site-packages'
%make_install

# SECTION Remove rpaths from config binaries and pkgconfig file
sed -i "s|-Wl,-rpath,[^ ]\+||g" %{buildroot}%{_bindir}/rivet-config
# /SECTION

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-plugins.conf

chmod -x %{buildroot}%{_datadir}/Rivet/ALICE_2012_I1126966.info \
         %{buildroot}%{_datadir}/Rivet/ALICE_2014_I1243865.info \
         %{buildroot}%{_datadir}/Rivet/STAR_2017_I1510593.{info,plot} \
         %{buildroot}%{_datadir}/Rivet/ATLAS_2019_I1772071.{cc,plot}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}/etc/bash_completion.d/rivet-completion %{buildroot}%{_datadir}/bash-completion/completions/

%fdupes %{buildroot}%{_datadir}/Rivet/

%check
export PYTHONPATH+=':%{buildroot}%{_libdir}/python%{py3_ver}/site-packages'
%make_build check

%post -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%{_libdir}/libRivet-*.so

%files data
%license COPYING
%{_datadir}/%{name}/

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_bindir}/rivet-config
%{_bindir}/rivet-buildplugin
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/rivet.pc

%files -n python3-%{name}
%license COPYING
%{_bindir}/*
%exclude %{_bindir}/rivet-config
%exclude %{_bindir}/rivet-buildplugin
%{python3_sitearch}/rivet/
%{_datadir}/bash-completion/completions/*

%files plugins
%license COPYING
%config %{_sysconfdir}/ld.so.conf.d/%{name}-plugins.conf
%{_libdir}/%{name}/

%changelog
