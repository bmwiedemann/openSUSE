#
# spec file for package python-gmpy
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%bcond_without tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-gmpy
Version:        1.17
Release:        1
License:        LGPL-2.1
Summary:        Multiprecision arithmetic for Python
Url:            https://pypi.python.org/pypi/gmpy/
Group:          Development/Libraries/Python
Source0:        https://files.pythonhosted.org/packages/source/g/gmpy/gmpy-%{version}.zip
BuildRequires:  fdupes
BuildRequires:  gmp-devel >= 4.0.1
BuildRequires:  libmpir-devel
BuildRequires:  unzip
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
%if %{with test}
BuildRequires:  %{python_module nose}
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
%{python_expand PYTHONPATH="%{buildroot}%{$python_sitearch}" 
$python gmpy_test.py
}
popd
%endif

%files %{python_files}
%defattr(-,root,root)
%doc README changes.txt lgpl-2.1.txt
%doc doc/*
%{python_sitearch}/gmpy-%{version}-py*.egg-info
%{python_sitearch}/gmpy.*so

%changelog
