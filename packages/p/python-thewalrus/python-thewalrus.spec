#
# spec file for package python-thewalrus
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


%define packagename thewalrus
%define skip_python2 1
%{?!python_module:%define python_module() python3-%{**}}
Name:           python-thewalrus
Version:        0.18.0
Release:        0
Summary:        An open-source software architecture for photonic quantum computing
License:        Apache-2.0
URL:            https://github.com/XanaduAI/thewalrus
Source:         https://github.com/XanaduAI/thewalrus/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module dask-delayed}
BuildRequires:  %{python_module flaky >= 3.7.0}
BuildRequires:  %{python_module numba >= 0.49.1}
BuildRequires:  %{python_module numpy >= 1.19.2}
BuildRequires:  %{python_module pytest >= 5.4.1}
BuildRequires:  %{python_module scipy >= 1.2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy >= 1.5.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dask-delayed
Requires:       python-numba >= 0.49.1
Requires:       python-numpy >= 1.19.2
Requires:       python-scipy >= 1.2.1
Requires:       python-sympy >= 1.5.1
BuildArch:      noarch
# Tests fail on 32-bit: 64bit-types expected
ExcludeArch:    i586
%python_subpackages

%description
A library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{packagename}-%{version}*-info
%{python_sitelib}/%{packagename}

%changelog
