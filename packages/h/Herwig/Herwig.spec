#
# spec file for package Herwig
#
# Copyright (c) 2024 SUSE LLC
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


%define so_name Herwig-libs
Name:           Herwig
Version:        7.3.0
Release:        0
Summary:        Multi-purpose event generator for high-energy physics
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://herwig.hepforge.org/
Source0:        http://www.hepforge.org/archive/herwig/%{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE Herwig-disable-repo-install.patch badshah400@gmail.com -- Disable post-install hooks intended to set up the Herwig repo, this doesn't work inside the build script because of missing LHAPDF data that needs to be installed by the user; the install-hook doesn't serve any purpose while building the rpm and users can easily set this up on their own
Patch0:         Herwig-disable-repo-install.patch
# PATCH-FIX-UPSTREAM Herwig-type-mismatch-fix.patch badshah400@gmail.com -- Fix a type mismatch error in fortran flagged by GCC 10
Patch1:         Herwig-type-mismatch-fix.patch
BuildRequires:  HepMC-devel
BuildRequires:  LHAPDF-devel
BuildRequires:  Rivet-devel
BuildRequires:  ThePEG-devel >= 2.3.0
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  fastjet-devel
BuildRequires:  fastjet-plugin-siscone-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gsl)
ExcludeArch:    %{ix86} %{arm}

%description
Herwig is a multi-purpose particle physics event generator.
Herwig 7.0 (Herwig++ 3.0) replaces any prior HERWIG or Herwig++ versions.

Herwig features coherent parton showers (including angular-ordered
and dipole-based evolution), the cluster hadronization model, an
eikonal multiple-interaction model, highly flexible BSM capabilities
and improved perturbative input using next-to-leading order QCD.

Herwig is based on ThePEG.

%package -n %{so_name}
Summary:        Multi purpose event generator for high energy physics
Group:          System/Libraries
Obsoletes:      libHerWig1 < %{version}-%{release}

%description -n %{so_name}
Herwig is a multi-purpose particle physics event generator.

Herwig features coherent parton showers (including angular-ordered
and dipole-based evolution), the cluster hadronization model, an
eikonal multiple-interaction model, highly flexible BSM capabilities
and improved perturbative input using next-to-leading order QCD.

Herwig is based on ThePEG.

This package provides the shared libraries for %{name}.

%package devel
Summary:        Multi purpose event generator for high energy physics
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}
Requires:       ThePEG-devel
Provides:       Herwig++-devel = %{version}
Obsoletes:      Herwig++-devel < %{version}

%description devel
Herwig is a multi-purpose particle physics event generator.
Herwig 7.0 (Herwig++ 3.0) replaces any prior HERWIG or Herwig++ versions.

Herwig features coherent parton showers (including angular-ordered
and dipole-based evolution), the cluster hadronization model, an
eikonal multiple-interaction model, highly flexible BSM capabilities
and improved perturbative input using next-to-leading order QCD.

Herwig is based on ThePEG.

This package provides the header and source libraries for development
with %{name}.

%prep
%autosetup -p1
# autoconf macros assume x86_64 is the only 64 bit arch
sed -i -e 's/"${host_cpu}" == "x86_64"/%{__isa_bits} == 64/' m4/{fastjet,herwig}.m4

# FIX ENV BASED HASHBANG
sed -i "1{s|/usr/bin/env bash|/bin/bash|}" src/herwig-config.in

%build
# default-integer-8 only set for x86_64 by upstream
export FCFLAGS="%{?build_fflags} -fdefault-integer-8"
autoreconf -fvi
%configure --disable-static
%make_build

%install
%make_install

mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf

find %{buildroot} -type f -name "*.la" -delete -print

# Remove unnecessary hashbangs
sed -i "1{/\/usr\/bin\/env/d;}" %{buildroot}%{_libdir}/%{name}/python/slha2herwig
sed -i "1{/\/usr\/bin\/env/d;}" %{buildroot}%{_libdir}/%{name}/python/ufo2herwig

# Fix hashbangs to directly point to python
for exe in gosam2herwig herwig-mergegrids mg2herwig slha2herwig ufo2herwig
do
 sed -i "1{s/\/usr\/bin\/env python/\/usr\/bin\/python3/;}" %{buildroot}%{_bindir}/${exe}
done

%fdupes -s %{buildroot}%{_libdir}/%{name}/
%fdupes -s %{buildroot}%{_datadir}/%{name}/

%post -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%doc AUTHORS GUIDELINES ChangeLog README
%license COPYING
%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.*

%files devel
%{_bindir}/Herwig
%{_bindir}/herwig-combinedistributions
%{_bindir}/herwig-combineruns
%{_bindir}/herwig-makedistributions
%{_bindir}/herwig-mergegrids
%{_bindir}/herwig-config
%{_bindir}/ufo2herwig
%{_bindir}/slha2herwig
%{_bindir}/gosam2herwig
%{_bindir}/mg2herwig
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/python/
%{_includedir}/%{name}/
%{_datadir}/%{name}/

%changelog
