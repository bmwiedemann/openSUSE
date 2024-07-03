#
# spec file for package apfel
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


%define soname libAPFEL0_0_0
# Need -ffat-lto-objects for the static lib
%define _lto_cflags -flto=auto -ffat-lto-objects
Name:           apfel
Version:        3.1.1
Release:        0
Summary:        A Probability Distribution Function Evolution Library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://apfel.hepforge.org/
Source:         https://github.com/scarrazza/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM apfel-dont-set-default-reltype.patch badshah400@gmail.com -- Don't assume 'RELEASE' as the release type, this should be set by user
Patch1:         apfel-dont-set-default-reltype.patch
BuildRequires:  %{python_module LHAPDF}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  LHAPDF-devel
BuildRequires:  cmake >= 3.15
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libboost_headers-devel
BuildRequires:  python-rpm-macros
BuildRequires:  swig
Requires:       python-LHAPDF
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

%package -n %{soname}
Summary:        A Probability Distribution Function Evolution Library
Group:          System/Libraries
# Problem with older naming scheme
Conflicts:      libAPFEL0 <= 3.0.6

%description -n %{soname}
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

This package provides the shared libraries for %{name}.

%package -n %{name}-devel
Summary:        Development files for Apfel, a PDF Evolution Library
Requires:       %{soname} = %{version}
Requires:       LHAPDF-devel
Recommends:     %{name}-doc = %{version}

%description -n %{name}-devel
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

This package provides the source files required to develop
applications with %{name}.

%package -n %{name}-devel-static
# We need to build and install the static lib as there is no way to
# disable it during configuration stage and it pollutes the cmake files
Summary:        Static development files for Apfel, a PDF Evolution library

%description -n %{name}-devel-static
APFEL is a library to perform the combined QCD+QED DGLAP
evolution of parton distributions.

This package provides the static library required to develop
applications with %{name}.

%package -n %{name}-doc
Summary:        Documentation for APFEL, a PDF evolution library

%description -n %{name}-doc
This package provides documentation for APFEL in PDF (Portable
Document Format), a PDF (Probability Distribution Function) evolution
library.

%prep
%autosetup -p1

%build
%{python_expand # Necessary to run configure with all $python flavors
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%cmake \
  -DCMAKE_RELEASE_TYPE="RelwithDebInfo" \
  -DPython_EXECUTABLE:PATH=${PYTHON} \
  -DAPFEL_DOWNLOAD_PDFS:BOOL=OFF
%cmake_build
popd
}

%install
%{python_expand #  all $python flavors as configured above
export PYTHON=%{_bindir}/$python
pushd ../$python
%cmake_install
%python_clone -a %{buildroot}%{_bindir}/apfel
popd
}

# REMOVE libtool ARCHIVES
find %{buildroot} -type f -name "*.la" -delete -print

# FIX env BASED SCRIPT INTERPRETER
sed -Ei "1{s|#\!\s*%{_bindir}/env bash|#\!/bin/bash|}" %{buildroot}%{_bindir}/apfel-config

# REMOVE INSTALLED README, INSTALL IT USING %%doc INSTEAD
rm -fr %{buildroot}%{_docdir}/%{name}/README
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
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}-config
%{_includedir}/APFEL/
%{_libdir}/*.so

%files -n %{name}-devel-static
%license COPYING
%{_libdir}/*.a
%{_datadir}/APFEL/

%files %{python_files}
%python_alternative %{_bindir}/apfel
%{python_sitearch}/apfel/
%{python_sitearch}/apfel-%{version}-py%{python_version}.egg-info

%files -n %{name}-doc
%doc doc/pdfs/manual.pdf

%changelog
