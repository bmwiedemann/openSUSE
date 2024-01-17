#
# spec file for package splinter
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define shlib lib%{name}-3-0
Name:           splinter
Version:        3.0
Release:        0
Summary:        A library for multivariate function approximation implemented in C++
License:        MPL-2.0
Group:          Productivity/Scientific/Math
Url:            https://github.com/bgrimstad/splinter
Source:         https://github.com/bgrimstad/%{name}/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM: upstream_add_armv8.patch -- add support to aarch64 (armv8)
Patch0:         upstream_add_armv8.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64 aarch64

%description
SPLINTER (SPLine INTERpolation) is a library for multivariate function
approximation implemented in C++. The library can be used for function
approximation, regression and data smoothing.

%package -n %{shlib}
Summary:        A library for multivariate function approximation implemented in C++
Group:          System/Libraries

%description -n %{shlib}
SPLINTER (SPLine INTERpolation) is a library for multivariate function
approximation implemented in C++. The library can be used for function
approximation, regression and data smoothing. Currently,
the library contains the following implementations:

1. tensor product B-splines,
2. radial basis functions, including the thin plate spline, and
3. polynomial regression.

The coefficients in these models are computed using ordinary least
squares (OLS). The name of the library, SPLINTER, originates from the
tensor product B-spline implementation, which was the first of the
methods to be implemented.

%package devel
Summary:        Development files for splinter, a multivariate function approximation library
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

%description devel
SPLINTER (SPLine INTERpolation) is a library for multivariate function
approximation implemented in C++. The library can be used for function
approximation, regression and data smoothing.

This package provides the header files and sources required for
developing applications with %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
Group:          Development/Languages/Python

%description -n python3-%{name}
SPLINTER (SPLine INTERpolation) is a library for multivariate function
approximation implemented in C++. The library can be used for function
approximation, regression and data smoothing.

This package provides the python bindings for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
  -DLIBRARY_INSTALL_DIRECTORY="%{_lib}" \
%ifarch x86_64
  -DARCH="x86-64"
%else
%ifarch aarch64
  -DARCH="armv8"
%else
  -DARCH="x86"
%endif
%endif

%make_jobs all doc

%install
%cmake_install

pushd python
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd

#FIXME: Need to fix crazy install dir of python libraries instead of them being installed in builddir
dirname=`pwd`
rm -r %{buildroot}/${dirname}/

find %{buildroot}/%{_libdir} -name "*.a" -delete -print

%fdupes %{buildroot}%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info/

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/lib%{name}*.so

%files devel
%defattr(-,root,root)
%doc CHANGELOG.md README.md CREDITS.md LICENSE
%{_includedir}/SPLINTER/

%files -n python3-%{name}
%defattr(-,root,root)
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info/

%changelog
