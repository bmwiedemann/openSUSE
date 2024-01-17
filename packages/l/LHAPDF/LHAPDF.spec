#
# spec file for package LHAPDF
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


# Not needed for actual use, but quilt does not work without this
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
#
%define so_name libLHAPDF-6_5_4
%define execname lhapdf
Name:           LHAPDF
Version:        6.5.4
Release:        0
Summary:        A library for unified interface to PDF sets
License:        GPL-3.0-only
URL:            https://lhapdf.hepforge.org/
Source:         http://www.hepforge.org/archive/lhapdf/%{name}-%{version}.tar.gz
Patch1:         sover.diff
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-latex-bin
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets. It also works with the more recent
multiple "error" sets, and incorporates many of the older sets found
in PDFLIB, including pion and photon PDFs. In LHAPDF, the computer
code and input parameters/grids are separated, thus allowing updating
and no limit to the expansion possibilities.

%package -n %{so_name}
Summary:        A library for unified and interface to PDF sets
Obsoletes:      libLHAPDF < %{version}-%{release}
Provides:       libLHAPDF = %{version}-%{release}

%description -n %{so_name}
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets. It also works with the more recent
multiple "error" sets, and incorporates many of the older sets found
in PDFLIB, including pion and photon PDFs. In LHAPDF, the computer
code and input parameters/grids are separated, thus allowing updating
and no limit to the expansion possibilities.

This package provides the shared library for %{name}.

%package -n %{name}-devel
Summary:        Development files for LHAPDF, a library for PDF sets
BuildRequires:  libboost_headers-devel
Requires:       %{so_name} = %{version}
Recommends:     %{name}-doc = %{version}

%description -n %{name}-devel
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets.

This package provides the header and source files for development with
%{name}.

%package -n %{name}-doc
Summary:        API documentation for LHAPDF, a library for PDF sets
BuildArch:      noarch

%description -n %{name}-doc
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets.

This package provides the API documentation for LHAPDF in HTML format.

%prep
%autosetup -p1
# Drop timestamps from doxygen doc files
sed -i "s/HTML_TIMESTAMP\s*=\s*YES/HTML_TIMESTAMP = NO/" doc/Doxyfile.in

%build
autoreconf -fvi
%{python_expand # Necessary to run configure for multiple py3 flavours
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%configure --disable-static --docdir=%{_docdir}/%{name}/
%make_build
# Build doc only for one flavour, viz., which provides the default python3
if [ "$python_" = "python3_" -o "%{$python_provides}" = "python3" ]; then
%make_build doxy
fi
popd
}

%install
%{python_expand # multiple py3 flavour make_install
export PYTHON=%{_bindir}/$python
pushd ../$python
%make_install
if [ "$python_" = "python3_" -o "%{$python_provides}" = "python3" ]; then
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pr doc/doxygen %{buildroot}%{_docdir}/%{name}/

# Drop a bunch of execs that report libtool-wrapper-in-package errors via rpmlint
for f in analyticpdf compatibility hessian2replicas reweight testpdf testpdfunc testpdfset
do
rm %{buildroot}%{_docdir}/%{name}/examples/${f}
done

%fdupes %{buildroot}%{_docdir}/%{name}/

fi
popd
}

sed -E -i "s|#! /usr/bin/env python|#! %{_bindir}/python3|" %{buildroot}%{_bindir}/lhapdf
sed -E -i "s|#! /usr/bin/env bash|#! /bin/bash|" %{buildroot}%{_bindir}/lhapdf-config

find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%license COPYING
%{_libdir}/libLHAPDF-%{version}.so

%files -n %{name}-devel
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/lhapdf
%{_bindir}/%{execname}-config
%{_datadir}/%{name}/
%{_includedir}/%{name}
%{_libdir}/libLHAPDF.so
%{_libdir}/pkgconfig/%{execname}.pc

%files %{python_files}
%{python_sitearch}/lhapdf/

%files -n %{name}-doc
%doc %{_docdir}/%{name}/

%changelog
