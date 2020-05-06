#
# spec file for package apfel
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


# PYTHON BINDINGS INCOMPATIBLE WITH PYTHON3
%if 0%{?suse_version} >= 1550
%bcond_with pywrap
%else
%bcond_without pywrap
%endif

%define skip_python3 1

%define soname libAPFEL0
Name:           apfel
Version:        3.0.4
Release:        0
Summary:        A Probability Distribution Function Evolution Library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://apfel.hepforge.org/
Source:         https://github.com/scarrazza/%{name}/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM apfel-allow-disabling-pywrap.patch badshah400@gmail.com -- Allow building with python extension disabled, for example due to lack of python2 support in the system
Patch0:         apfel-allow-disabling-pywrap.patch
BuildRequires:  LHAPDF-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libboost_headers-devel
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
%if %{with pywrap}
BuildRequires:  %{python_module LHAPDF}
BuildRequires:  %{python_module devel}
%endif
Requires:       python-LHAPDF

%python_subpackages

%description
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

%package -n %{soname}
Summary:        A Probability Distribution Function Evolution Library
Group:          System/Libraries

%description -n %{soname}
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

This package provides the shared libraries for %{name}.

%package -n %{name}-devel
Summary:        Development files for Apfel, a PDF Evolution Library
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       LHAPDF-devel
Recommends:     %{name}-doc = %{version}

%description -n %{name}-devel
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

This package provides the source files required to develop
applications with %{name}.

%package -n %{name}-doc
Summary:        Documentation for APFEL, a PDF evolution library
Group:          Documentation/Other

%description -n %{name}-doc
This package provides documentation for APFEL in PDF (Portable
Document Format), a PDF (Probability Distribution Function) evolution
library.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure \
  --disable-static \
  %{!?with_pywrap:--disable-pywrap}
make %{?_smp_mflags}

%install
%make_install

# REMOVE libtool ARCHIVES
find %{buildroot} -type f -name "*.la" -delete -print

# FIX env BASED SCRIPT INTERPRETER
sed -Ei "1{s|#\!\s*/usr/bin/env bash|#\!/bin/bash|}" %{buildroot}%{_bindir}/apfel-config

# REMOVE INSTALLED README, INSTALL IT USING %%doc INSTEAD
rm -fr %{buildroot}%{_datadir}/doc/apfel/README
rm -fr %{buildroot}%{_datadir}/apfel/README

%post   -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%{_libdir}/*.so.*

%files -n %{name}-devel
%{_includedir}/APFEL/
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/CheckAPFEL
%{_bindir}/%{name}-config
%{_bindir}/ListFunctions
%{_libdir}/*.so

%if %{with pywrap}
%files %{python_files}
%{_bindir}/apfel
%{python_sitearch}/*
%endif

%files -n %{name}-doc
%doc doc/pdfs/manual.pdf

%changelog
