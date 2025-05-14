#
# spec file for package python-pyprimes
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without  test
# Alpha releases also contain a digit, assuming 0 if not provided
%define wheel_version %{version}0
Name:           python-pyprimes
Version:        0.2.2a
Release:        0
Summary:        Generate and test for prime numbers
License:        MIT
URL:            http://code.google.com/p/pyprimes/
Source:         https://files.pythonhosted.org/packages/source/p/pyprimes/pyprimes-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
The pyprimes package offers a variety of algorithms for generating prime
numbers and fast primality tests, written in pure Python.

Prime numbers are those positive integers which are not divisible exactly
by any number other than itself or one. Generating primes and testing for
primality has been a favourite mathematical pastime for centuries, as well
as of great practical importance for encrypting data.

``pyprimes`` includes the following features:

    - Produce prime numbers lazily, on demand.
    - Effective algorithms including Sieve of Eratosthenes, Croft Spiral,
      and Wheel Factorisation.
    - Efficiently test whether numbers are prime, using both deterministic
      (exact) and probabilistic primality tests.
    - Examples of what *not* to do are provided, including naive trial
      division, Turner's algorithm, and primality testing using a
      regular expression.
    - Factorise small numbers into the product of prime factors.
    - Suitable for Python 2.4 through 3.x from one code base.

%prep
%setup -q -n pyprimes-%{version}
sed -i 's/\r$//' CHANGES.txt
sed -i 's/\r$//' README.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec src/pyprimes/tests.py
%endif

%files %{python_files}
%doc CHANGES.txt README.txt
%license LICENCE.txt
%{python_sitelib}/pyprimes
%{python_sitelib}/pyprimes-%{wheel_version}.dist-info

%changelog
