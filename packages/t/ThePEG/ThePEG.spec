#
# spec file for package ThePEG
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


# DISABLE JAVA BINDINGS UNTIL COMPATIBLE WITH openjdk >= 1.9
%bcond_with java

Name:           ThePEG
Version:        2.2.2
Release:        0
Summary:        Toolkit providing a common platform for event generators in C++
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://home.thep.lu.se/~leif/ThePEG/
Source:         http://www.hepforge.org/archive/thepeg/%{name}-%{version}.tar.bz2
Patch1:         ThePEG_gcc6_failed.patch
BuildRequires:  HepMC-devel
BuildRequires:  LHAPDF-devel
BuildRequires:  Rivet-devel
BuildRequires:  YODA-devel
BuildRequires:  fastjet-devel
BuildRequires:  fastjet-plugin-siscone-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  libboost_test-devel
%if %{with java}
BuildRequires:  java-devel
%endif
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# 32-BIT BUILDS ARE NOT SUPPORTED BY UPSTREAM
ExcludeArch:    i586

%description
ThePEG project is a toolkit for providing a common platform for using and
building event generators in C++.

%package -n ThePEG-libs
Summary:        Toolkit providing a common platform for event generators in C++
Group:          System/Libraries
Obsoletes:      libThePEG24 < %{version}-%{release}
Provides:       libThePEG24 = %{version}-%{release}

%description -n ThePEG-libs
ThePEG project is a toolkit for providing a common platform for using and
building event generators in C++.

This package provides the shared libraries for ThePEG.

%package devel
Summary:        Toolkit providing a common platform for event generators in C++
Group:          Development/Libraries/C and C++
Requires:       ThePEG-libs = %{version}

%description devel
ThePEG project is a toolkit for providing a common platform for using and
building event generators in C++.

This package provides the header and source files needed for development with
ThePEG.

%prep
%setup -q
%patch1 -p1

# FIX AN env BASED HASHBANG
sed -i "1{s|#! /usr/bin/env bash|#!/bin/bash|}" ./src/thepeg-config.in

%build
%configure \
  --with-hepmcversion=3 \
  --with-rivet=%{_prefix}
%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
cat << EOF > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%{_libdir}/%{name}
EOF

find %{buildroot}%{_libdir}/%{name} -name "*.la" -delete
%fdupes -s %{buildroot}%{_libdir}/%{name}/

%post   -n ThePEG-libs -p /sbin/ldconfig
%postun -n ThePEG-libs -p /sbin/ldconfig

%files -n ThePEG-libs
%defattr(-,root,root)
%doc AUTHORS GUIDELINES ChangeLog NEWS README
%license COPYING
%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/runThePEG
%{_bindir}/setupThePEG
%{_bindir}/thepeg-config
%{_includedir}/%{name}/
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/Makefile
%{_libdir}/%{name}/Makefile.common
%{_libdir}/%{name}/ThePEGDefaults-%{version}.rpo
%{_libdir}/%{name}/ThePEGDefaults.rpo
%{_libdir}/%{name}/runThePEG-%{version}
%{_libdir}/%{name}/setupThePEG-%{version}
%{_datadir}/%{name}/
%if %{with java}
%{_bindir}/thepeg
%{_libdir}/%{name}/ThePEG.jar
%endif

%changelog
