#
# spec file for package LHAPDF
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


%define so_name libLHAPDF-6_2_3
%define execname lhapdf

Name:           LHAPDF
Version:        6.2.3
Release:        0
Summary:        A library for unified interface to PDF sets
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://lhapdf.hepforge.org/
Source:         http://www.hepforge.org/archive/lhapdf/%{name}-%{version}.tar.gz
Patch1:         sover.diff
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.53.0
%endif
BuildRequires:  %{python_module devel}
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-latex-bin
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Group:          System/Libraries
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
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.53.0
%endif

%description -n %{name}-devel
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets.

This package provides the header and source files for development with
%{name}.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fi
%{python_expand # Necessary to run %%configure with both py2 and py3
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%configure --disable-static --docdir=%{_docdir}/%{name}/
make %{?_smp_mflags}
popd
}

%install
%{python_expand # py2 and py3 make_install
export PYTHON=%{_bindir}/$python
pushd ../$python
%make_install
popd
}

sed -E -i "s|#! /usr/bin/env python|#! /usr/bin/python3|" %{buildroot}%{_bindir}/lhapdf
sed -E -i "s|#! /usr/bin/env bash|#! /bin/bash|" %{buildroot}%{_bindir}/lhapdf-config

find %{buildroot}%{_libdir}/ -name "*.la" -delete

%post   -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%defattr(-, root, root)
%{_libdir}/libLHAPDF-%version.so

%files -n %{name}-devel
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{execname}-*
%{_datadir}/%{name}/
%{_includedir}/%{name}
%{_libdir}/libLHAPDF.so
%{_libdir}/pkgconfig/%{execname}.pc

%files %{python_files}
%python3_only %{_bindir}/%{execname}
%{python_sitearch}/*.egg-info
%{python_sitearch}/*.so

%changelog
