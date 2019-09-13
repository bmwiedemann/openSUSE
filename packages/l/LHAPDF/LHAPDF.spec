#
# spec file for package LHAPDF
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


%define so_name libLHAPDF-6_2_3
%define execname lhapdf

Name:           LHAPDF
Version:        6.2.3
Release:        0
Summary:        A library for unified interface to PDF sets
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            https://lhapdf.hepforge.org/
Source:         http://www.hepforge.org/archive/lhapdf/%{name}-%{version}.tar.gz
Patch1:         sover.diff
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.53.0
%endif
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  texlive-latex-bin
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package devel
Summary:        Development files for LHAPDF, a library for PDF sets
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.53.0
%endif

%description devel
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets.

This package provides the header and source files for development with
%{name}.

%package -n python-%{name}
Summary:        Python bindings for LHAPDF, a library for PDF sets
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}
Requires:       python

%description -n python-%{name}
LHAPDF provides a unified and interface to PDF (probability
distribution function) sets.

This package provides the python wrapper for %{name}.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fi
%configure --disable-static --docdir=%{_docdir}/%{name}/
make %{?_smp_mflags}

%install
%make_install

sed -E -i "s|#! /usr/bin/env python|#! /usr/bin/python%{py_ver}|" %{buildroot}%{_bindir}/lhapdf
sed -E -i "s|#! /usr/bin/env bash|#! /bin/bash|" %{buildroot}%{_bindir}/lhapdf-config

find %{buildroot}%{_libdir}/ -name "*.la" -delete

%post   -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%files -n %{so_name}
%defattr(-, root, root)
%{_libdir}/libLHAPDF-%version.so

%files devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{execname}
%{_bindir}/%{execname}-*
%{_datadir}/%{name}/
%{_includedir}/%{name}
%{_libdir}/libLHAPDF.so
%{_libdir}/pkgconfig/%{execname}.pc

%files -n python-%{name}
%defattr(-, root, root)
%{python_sitearch}/%{name}-*.egg-info
%{python_sitearch}/%{execname}.so

%changelog
