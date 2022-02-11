#
# spec file for package python-gmpy
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


%bcond_without tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-gmpy
Version:        1.17
Release:        0
License:        LGPL-2.1-only
Summary:        Multiprecision arithmetic for Python
URL:            https://pypi.python.org/pypi/gmpy/
Group:          Development/Libraries/Python
Source0:        https://files.pythonhosted.org/packages/source/g/gmpy/gmpy-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gmp-devel >= 4.0.1
BuildRequires:  libmpir-devel
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%python_subpackages

%description
A C-coded Python extension module that wraps the GMP library
to provide to Python code fast multiprecision arithmetic
(integer, rational, and float), random number generation,
advanced number-theoretical functions, and more.

%prep
%setup -q -n gmpy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
pushd test
%pytest
popd
%endif

%files %{python_files}
%defattr(-,root,root)
%doc README changes.txt lgpl-2.1.txt
%doc doc/*
%{python_sitearch}/gmpy-%{version}-py*.egg-info
%{python_sitearch}/gmpy.*so

%changelog
