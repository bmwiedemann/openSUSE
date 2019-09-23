#
# spec file for package python-pytest-remotedata
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-remotedata
Version:        0.3.2
Release:        0
Summary:        Pytest plugin for controlling remote data access
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/astropy/pytest-remotedata
Source:         https://files.pythonhosted.org/packages/source/p/pytest-remotedata/pytest-remotedata-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.1
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This package provides a plugin for the pytest framework that allows
developers to control unit tests that require access to data from the internet.

%prep
%setup -q -n pytest-remotedata-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_internet_access (test_default_behavior, test_strict_with_decorator) - needs network
%pytest -k 'not (test_default_behavior or test_strict_with_decorator)'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
