#
# spec file for package python-pytest-isort
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
Name:           python-pytest-isort
Version:        0.3.1
Release:        0
Summary:        Plugin for pytest to perform isort checks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/moccu/pytest-isort/
Source:         https://files.pythonhosted.org/packages/source/p/pytest-isort/pytest-isort-%{version}.tar.gz
BuildRequires:  %{python_module isort >= 4.0}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-isort >= 4.0
Requires:       python-pytest >= 3.5
BuildArch:      noarch
%python_subpackages

%description
This is a py.test plugin to check import ordering using isort.

%prep
%setup -q -n pytest-isort-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
