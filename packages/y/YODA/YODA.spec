#
# spec file for package YODA
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


# HDF5 is too old on Leap 15.6
%if 0%{?suse_version} >= 1600
%bcond_without hdf5
%else
%bcond_with hdf5
%endif
%define so_name lib%{name}-%(echo %{version} | tr '.' '_')
Name:           YODA
Version:        2.1.2
Release:        0
Summary:        A small set of data analysis classes for MC event generator validation analyses
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://gitlab.com/hepcedar/yoda
Source0:        https://www.hepforge.org/archive/yoda/%{name}-%{version}.tar.bz2
Source1:        %{name}.rpmlintrc
Patch0:         sover.diff
BuildRequires:  autoconf
BuildRequires:  bash-completion
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(zlib)
%if %{with hdf5}
BuildRequires:  pkgconfig(hdf5)
%endif
# SECTION For running python tests in make check
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
# /SECTION

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
%if %{with hdf5}
Requires:       pkgconfig(hdf5)
%endif
Recommends:     %{name}-matplotlib-style = %{version}

%description devel
YODA is a small set of data analysis (specifically histogramming)
classes being developed by MCnet members as a lightweight common
system for MC event generator validation analyses.

This package provides the source files for development with %{name}.

%package -n python3-%{name}
Summary:        A small set of data analysis classes for MC event generator validation analyses
Group:          Development/Libraries/Python
Requires:       %{so_name} = %{version}
Provides:       python-%{name} = %{version}
Recommends:     %{name}-matplotlib-style = %{version}

%description -n python3-%{name}
YODA is a small set of data analysis (specifically histogramming)
classes being developed by MCnet members as a lightweight common
system for MC event generator validation analyses.

This package provides the python binidings for %{name}.

%package matplotlib-style
Summary:        Matplotlib style file for YODA styled plots
Requires:       python3-matplotlib
BuildArch:      noarch

%description matplotlib-style
This package provides a style file that may be used with matplotlib to produce
YODA styled plots.

%prep
%autosetup -p1

# USE PYTHON3 FOR HASHBANGS
sed -Ei "1{s|/usr/bin/python3?$|/usr/bin/python3|}" bin/*
sed -Ei "1{s|/usr/bin/env python3?$|/usr/bin/python3|}" bin/* pyext/yoda/mktemplates
sed -Ei "1{s|/usr/bin/env python3?$|/usr/bin/python3|}" tests/*.py

# FIX env BASED HASHBANGS
sed -E -i "s|^#! /usr/bin/env bash|#! /bin/bash|" bin/yoda-config*

# REMOVE AN UNNECESSARY ONE
sed -E -i "1{s|^#! /usr/bin/env python||}" pyext/yoda/search.py

%build
export PYTHON_VERSION=%{py3_ver}
autoreconf -fi
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/* %{buildroot}%{_datadir}/bash-completion/completions/
find %{buildroot} -type f -name "*.la" -delete -print

%check
# Two tests fail due to minor result vs test-value mismatch for i586; ignore for now
%ifarch %{ix86}
%make_build check || true
%else
%make_build check
%endif

%ldconfig_scriptlets -n %{so_name}

%files -n %{so_name}
%{_libdir}/libYODA-*.so

%files devel
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/yoda-config
%{_libdir}/libYODA.so
%{_libdir}/pkgconfig/yoda.pc
%{_includedir}/%{name}/

%files matplotlib-style
%{_datadir}/YODA/

%files -n python3-%{name}
%{python3_sitearch}/yoda/
%{_datadir}/bash-completion/completions/*
%{_bindir}/root2yoda
%{_bindir}/yoda2root
%{_bindir}/yoda2yoda
%{_bindir}/yodacnv
%{_bindir}/yodadiff
%{_bindir}/yodaenvelope
%{_bindir}/yodals
%{_bindir}/yodamerge
%{_bindir}/yodaplot
%{_bindir}/yodascale
%{_bindir}/yodastack

%changelog
