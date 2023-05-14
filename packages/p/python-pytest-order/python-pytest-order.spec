#
# spec file for package python-pytest-order
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pytest-order
Version:        1.1.0
Release:        0
Summary:        Pytest plugin to run your tests in a specific order
License:        MIT
URL:            https://github.com/pytest-dev/pytest-order
Source:         https://files.pythonhosted.org/packages/source/p/pytest-order/pytest-order-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module pytest-dependency}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 5.0
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin that allows you to customize the order in which your tests are
run. It uses the marker order that defines when a specific test shall be run
relative to the other tests. pytest-order is a fork of pytest-ordering that
provides some additional features.

%prep
%setup -q -n pytest-order-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/pytest_order
%{python_sitelib}/pytest_order-%{version}*-info

%changelog
