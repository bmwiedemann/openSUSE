#
# spec file for package fastjet-contrib
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


%define shlib libfastjetcontribfragile
Name:           fastjet-contrib
Version:        1.049
Release:        0
Summary:        A library of 3rd-party add-ons to FastJet
License:        GPL-2.0-only
URL:            https://fastjet.hepforge.org/contrib/
Source:         https://fastjet.hepforge.org/contrib/downloads/fjcontrib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - https://github.com/alisw/fastjet/pull/6
Patch0:         reproducible.patch
BuildRequires:  fastjet-devel
BuildRequires:  gcc-c++

%description
%{name} provides a library of 3rd-party add-ons to FastJet.

%package -n %{shlib}
Summary:        Shared library for fastjet-contrib

%description -n %{shlib}
This package provides the shared library for fastjet-contrib.

%package devel
Summary:        Headers for fastjet-contrib
Requires:       %{shlib} = %{version}

%description devel
This package provides the headers for writing code using fastjet-contrib.

%package devel-static
Summary:        Static libraries and headers for fastjet-contrib
Requires:       %{name}-devel = %{version}

%description devel-static
This package provides the static libraries for fastjet-contrib to link against.

%prep
%setup -q -n fjcontrib-%{version}
%patch0 -p1

%build
# %%configure does not work as a few of the args passed to it isn't recognised by the configure script
./configure --fastjet-config=%{_bindir}/fastjet-config --prefix=%{buildroot}%{_prefix}

%make_build fragile-shared

%install
%make_install
make fragile-shared-install

# Thanks to definciencies in configure script, need to move the libraries to the correct loc manually
mkdir -p %{buildroot}%{_libdir}
%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}/
%endif

%files -n %{shlib}
%{_libdir}/*.so

%files devel-static
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_libdir}/*.a

%files devel
%license COPYING
%{_includedir}/fastjet/contrib/

%changelog
