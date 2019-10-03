#
# spec file for package python-semver
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
%bcond_without test
Name:           python-semver
Version:        2.8.1
Release:        0
Summary:        Python helper for Semantic Versioning
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/k-bx/python-semver
# https://github.com/k-bx/python-semver/issues/136
Source:         https://github.com/k-bx/python-semver/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# See https://github.com/k-bx/python-semver/issues/67 for why conflicts is needed
Conflicts:      python-node-semver
BuildArch:      noarch
%python_subpackages

%description
A Python module for semantic versioning. Simplifies comparing versions.
See also http://semver.org/

%prep
%setup -q -n python-semver-%{version}

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/semver*
%pycache_only %{python_sitelib}/__pycache__/semver*

%changelog
