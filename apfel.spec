#
# spec file for package apfel
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


%define soname libAPFEL0
Name:           apfel
Version:        3.0.6
Release:        0
Summary:        A Probability Distribution Function Evolution Library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://apfel.hepforge.org/
Source:         https://github.com/scarrazza/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module LHAPDF}
BuildRequires:  %{python_module devel}
BuildRequires:  LHAPDF-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libboost_headers-devel
BuildRequires:  python-rpm-macros
Requires:       python-LHAPDF
Requires(post): update-alternatives
Requires(postun):update-alternatives

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
%{python_expand # Necessary to run configure with all python flavors
export PYTHON=%{_bindir}/$python
mkdir ../{$python}_build
cp -pr ./ ../{$python}_build
pushd ../{$python}_build
%configure \
  --disable-static
%make_build
popd
}

%install
%{python_expand #  all python flavors as configured above
export PYTHON=%{_bindir}/$python
pushd ../{$python}_build
%make_install
%python_clone -a %{buildroot}%{_bindir}/apfel
popd
}

# REMOVE libtool ARCHIVES
find %{buildroot} -type f -name "*.la" -delete -print

# FIX env BASED SCRIPT INTERPRETER
sed -Ei "1{s|#\!\s*/usr/bin/env bash|#\!/bin/bash|}" %{buildroot}%{_bindir}/apfel-config

# REMOVE INSTALLED README, INSTALL IT USING %%doc INSTEAD
rm -fr %{buildroot}%{_datadir}/doc/apfel/README
rm -fr %{buildroot}%{_datadir}/apfel/README

%post   -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%post
%python_install_alternative apfel

%postun
%python_uninstall_alternative apfel

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

%files %{python_files}
%python_alternative %{_bindir}/apfel
%{python_sitearch}/apfel.py
%{python_sitearch}/*.so
%pycache_only %{python_sitearch}/__pycache__/*.pyc
%python2_only %{python_sitearch}/*.pyc
%{python_sitearch}/APFEL-%{version}-py%{python_version}.egg-info

%files -n %{name}-doc
%doc doc/pdfs/manual.pdf

%changelog
