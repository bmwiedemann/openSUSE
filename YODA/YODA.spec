#
# spec file for package YODA
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


%define so_name lib%{name}-1_7_7

Name:           YODA
Version:        1.7.7
Release:        0
Summary:        A small set of data analysis classes for MC event generator validation analyses
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Url:            http://yoda.hepforge.org/
Source:         http://www.hepforge.org/archive/yoda/%{name}-%{version}.tar.bz2
Patch1:         sover.diff
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-Cython
BuildRequires:  python-devel
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
YODA is a small set of data analysis (specifically histogramming)
classes being developed by MCnet members as a lightweight common
system for MC event generator validation analyses. 

A few key features of YODA are as follows:
* Storage of all information needed for statistically correct run
  combination and reweighting up to second-order correlations (e.g.
  variances, std devs, etc.) not just in the number of entries in a
  bin, but also the correlations of that with the x and y fill
  values.
* Separation of statistics and data handling from presentation. YODA
  is primarily a library for doing the data part correctly: while we
  love really high quality data presentation, that's a separate goal.
* A sensible class hierarchy for histogramming, recognising that a
  histogram contains details of fill history beyond the pure visual
  height of a bin, and that just counting weights, or binning
  arbitrary types on an axis are valuable operations.
* Flexible data format support, including a new text-based, compact,
  and human-readable YODA format.
* Proper and convenience treatment of "details" like irregular bin
  widths, gaps in contiguous binning, and overflows/underflows/etc.
  (incuding how they impact normalisation and calculation of histo-
  wide stat quantities)
* Carefully designed programming interfaces in C++ and Python. We
  are very welcoming of feedback and design evolution, too!

%package -n %{so_name}
Summary:        A small set of data analysis classes for MC event generator validation analyses
Group:          System/Libraries

%description -n %{so_name}
YODA is a small set of data analysis (specifically histogramming)
classes being developed by MCnet members as a lightweight common
system for MC event generator validation analyses. 

This package provides the source files for development with %{name}.


%package devel
Summary:        A small set of data analysis classes for MC event generator validation analyses
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}

%description devel
YODA is a small set of data analysis (specifically histogramming)
classes being developed by MCnet members as a lightweight common
system for MC event generator validation analyses. 

This package provides the source files for development with %{name}.

%package -n python-%{name}
Summary:        A small set of data analysis classes for MC event generator validation analyses
Group:          Development/Libraries/Python
Requires:       %{so_name} = %{version}
Requires:       python = %{py_ver}

%description -n python-%{name}
YODA is a small set of data analysis (specifically histogramming)
classes being developed by MCnet members as a lightweight common
system for MC event generator validation analyses. 

This package provides the python binidings for %{name}.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

find %{buildroot}%{_libdir}/ -name "*.la" -delete

# Remove traces of BUILDROOT from files
sed -i "s|%{buildroot}||g" %{buildroot}%{python_sitearch}/yoda/*.pyc

# FIX env BASED HASHBANGS
for exe in %{buildroot}%{_bindir}/*
do
  sed -E -i "s|^#! /usr/bin/env python|#! /usr/bin/python|" ${exe}
done
sed -E -i "s|^#! /usr/bin/env bash|#! /bin/bash|" %{buildroot}%{_bindir}/yoda-config

%post   -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%defattr(-,root,root)
%{_libdir}/libYODA-*.so

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/aida2flat
%{_bindir}/aida2yoda
%{_bindir}/flat2yoda
%{_bindir}/yoda2aida
%{_bindir}/yoda2flat
%{_bindir}/yoda2yoda
%{_bindir}/yoda-config
%{_bindir}/yodamerge
%{_bindir}/yodacmp
%{_bindir}/yodacnv
%{_bindir}/yodadiff
%{_bindir}/yodahist
%{_bindir}/yodals
%{_bindir}/yodaplot
%{_bindir}/yodascale
%{_libdir}/libYODA.so
%{_libdir}/pkgconfig/yoda.pc
%{_includedir}/%{name}/
%{_datadir}/%{name}/

%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/yoda/
%{python_sitearch}/yoda1/
%{python_sitearch}/yoda*.egg-info

%changelog
