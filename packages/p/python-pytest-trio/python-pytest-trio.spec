#
# spec file for package python-pytest-trio
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pytest-trio
Version:        0.8.0
Release:        0
Summary:        Pytest plugin for trio
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/pytest-trio
Source:         https://github.com/python-trio/pytest-trio/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-contextvars >= 2.1
Requires:       python-outcome >= 1.1.0
Requires:       python-pytest >= 7.2.0
Requires:       python-trio >= 0.22.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module contextvars >= 2.1}
BuildRequires:  %{python_module hypothesis >= 3.64}
BuildRequires:  %{python_module outcome >= 1.1.0}
# we really need newer pytest in tests than is required by the package
BuildRequires:  %{python_module pytest >= 7.2.0}
BuildRequires:  %{python_module trio >= 0.22.0}
# /SECTION
%python_subpackages

%description
This is a pytest plugin to help you test projects that use Trio,
a friendly library for concurrency and async I/O in Python.

%prep
%setup -q -n pytest-trio-%{version}

rm pytest.ini
rm pytest_trio/_tests/test_hypothesis_interaction.py
mv pytest_trio/_tests/ tests

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/*

%changelog
