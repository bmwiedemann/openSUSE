#
# spec file for package SHERPA-MC
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


%define soname lib%{name}0

Name:           SHERPA-MC
Version:        2.2.6
Release:        0
Summary:        MC event generator for Simulation of High-Energy Reactions of PArticles
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            https://sherpa.hepforge.org/
Source:         http://www.hepforge.org/archive/sherpa/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM SHERPA-MC-no-return-in-non-void-function.patch badshah400@gmail.com -- Fix a non-void (bool) function that was not returning any data to return "true"
Patch0:         SHERPA-MC-no-return-in-non-void-function.patch
BuildRequires:  HepMC2-devel
BuildRequires:  LHAPDF-devel
BuildRequires:  Rivet-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  fastjet-devel
BuildRequires:  fastjet-plugin-siscone-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 6
BuildRequires:  gcc-fortran >= 6
BuildRequires:  openmpi-devel
BuildRequires:  pkg-config
BuildRequires:  pythia-devel
BuildRequires:  python-devel
BuildRequires:  scons
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zlib)
Requires(post):  info
Requires(preun): info

%description
Sherpa is a Monte Carlo event generator for the Simulation of
High-Energy Reactions of PArticles in lepton-lepton, lepton-photon,
photon-photon, lepton-hadron and hadron-hadron collisions. It provides
complete hadronic final states in simulations of high-energy particle
collisions. The produced events may be passed into detector
simulations used by the various experiments. The entire code has been
written in C++.

Sherpa simulations can be achieved for the following types of
collisions:
 - For lepton–lepton collisions, as explored by the CERN LEP
   experiments,
 - for lepton–photon collisions,
 - for photon–photon collisions with both photons either resolved or
   unresolved,
 - for deep-inelastic lepton-hadron scattering, as investigated by
   the HERA experiments at DESY, and,
 - in particular, for hadronic interactions as studied at the
   Fermilab Tevatron or the CERN LHC.

%package -n %soname
Summary:        MC event generator for Simulation of High-Energy Reactions of PArticles
Group:          System/Libraries
Obsoletes:      libSHERPA-MC < %version-%release
Provides:       libSHERPA-MC = %version-%release
Requires:       libSHERPA-MC-config

%description -n %soname
Sherpa is a Monte Carlo event generator for the Simulation of
High-Energy Reactions of PArticles in lepton-lepton, lepton-photon,
photon-photon, lepton-hadron and hadron-hadron collisions. It provides
complete hadronic final states in simulations of high-energy particle
collisions. The produced events may be passed into detector
simulations used by the various experiments. The entire code has been
written in C++.

This package provides the shared libraries for Sherpa.

%package -n %{soname}-config
Summary:        Dynamic linker configuration for the SHERPA-MC libraries
Group:          System/Base
BuildArch:      noarch
Provides:       libSHERPA-MC-config < %{version}-release
Obsoletes:      libSHERPA-MC-config = %{version}-release

%description -n %{soname}-config
Contains the ld.so.conf.d file for the SHERPA-MC libraries.

%package devel
Summary:        MC event generator for Simulation of High-Energy Reactions of PArticles
Group:          Development/Libraries/C and C++
Requires:       %soname = %{version}

%description devel
Sherpa is a Monte Carlo event generator for the Simulation of
High-Energy Reactions of PArticles in lepton-lepton, lepton-photon,
photon-photon, lepton-hadron and hadron-hadron collisions. It provides
complete hadronic final states in simulations of high-energy particle
collisions. The produced events may be passed into detector
simulations used by the various experiments. The entire code has been
written in C++.

This package provides the source and header files for development with
Sherpa.

%package -n python-%{name}
Summary:        Python extensions for SHERPA-MC
Group:          Development/Languages/Python

%description -n python-%{name}
Sherpa is a Monte Carlo event generator for the Simulation of
High-Energy Reactions of PArticles in lepton-lepton, lepton-photon,
photon-photon, lepton-hadron and hadron-hadron collisions. It provides
complete hadronic final states in simulations of high-energy particle
collisions. The produced events may be passed into detector
simulations used by the various experiments. The entire code has been
written in C++.

This package provides the python extensions for Sherpa.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --docdir=%{_docdir}/%{name}  \
  --enable-ufo \
  --enable-pyext       \
  --enable-analysis    \
  --enable-multithread \
  --enable-gzip        \
  --enable-hepmc2=%{_prefix}      \
  --enable-fastjet=%{_prefix}     \
  --enable-lhapdf=%{_prefix}      \
  --enable-pythia=%{_prefix}

# FIXME: Disable rivet bindings until SHERPA-MC builds with latest Rivet >= 2.1.2
#  --enable-rivet=%%{_prefix}       \

make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{soname}.conf

find %{buildroot}%{_libdir}/%{name}/ -name *.la -delete

%fdupes %{buildroot}%{_datadir}/%{name}/
%fdupes %{buildroot}%{python_sitelib}/

%post -n %soname -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/Sherpa.*.gz

%postun -n %soname -p /sbin/ldconfig

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/Sherpa.*.gz

%files -n %soname
# Even though the dir itself isn't versioned, the shared libs inside it are, so this works
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so.*
#

%files -n %{soname}-config
%config %{_sysconfdir}/ld.so.conf.d/%{soname}.conf

%files devel
%license COPYING
%doc ChangeLog README
%{_bindir}/get_bibtex
%{_bindir}/Combine_Analysis
%{_bindir}/Sherpa
%{_bindir}/Sherpa-config
%{_bindir}/init_nlo.sh
%{_bindir}/make2scons
%{_bindir}/plot_graphs.sh
%{_bindir}/plot_stats.sh
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.jpg
%{_libdir}/%{name}/*.so
%{_includedir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/Sherpa.*.gz
%{_infodir}/Sherpa.*.gz

%files -n python-%{name}
%{_bindir}/Sherpa-generate-model
%{python_sitelib}/Sherpa.py*
%{python_sitelib}/ufo_interface/
%{python_sitelib}/_Sherpa.*

%changelog
