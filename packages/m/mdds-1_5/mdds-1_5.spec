#
# spec file for package mdds-1_5
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


# redefined as we put there just devel docs
%define _docdir %{_defaultdocdir}/%{name}-devel
%define _apiver 1.5
%define _oname mdds
Name:           %{_oname}-1_5
Version:        1.6.0
Release:        0
Summary:        A collection of multi-dimensional data structure and indexing algorithm
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.com/mdds/mdds
Source:         http://kohei.us/files/%{_oname}/src/%{_oname}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
This library provides a collection of multi-dimensional data structure and indexing
algorithm.  All data structures are available as C++ templates, hence this is a
header-only library, with no shared library to link against.

%package        devel
Summary:        A collection of multi-dimensional data structure and indexing algorithm
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1500
Requires:       libboost_headers-devel
%else
Requires:       boost-devel >= 1.39
%endif

%description    devel
This library provides a collection of multi-dimensional data structure and indexing
algorithms.  All data structures are available as C++ templates, hence this is a
header-only library, with no shared library to link against.

%prep
%setup -q -n %{_oname}-%{version}

%build
%configure \
    --disable-silent-rules \
    --docdir=%{_docdir}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install

%files devel
%doc %{_docdir}
%{_includedir}/%{_oname}-%{_apiver}
%{_datadir}/pkgconfig/*.pc

%changelog
