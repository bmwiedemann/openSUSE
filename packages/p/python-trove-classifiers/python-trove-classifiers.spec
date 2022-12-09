#
# spec file for package python-trove-classifiers
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
Name:           python-trove-classifiers
Version:        2022.12.1
Release:        0
Summary:        Canonical source for classifiers on PyPI
License:        Apache-2.0
URL:            https://github.com/pypa/trove-classifiers
Source:         https://files.pythonhosted.org/packages/source/t/trove-classifiers/trove-classifiers-%{version}.tar.gz
BuildRequires:  %{python_module calver}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Classifiers categorize projects per PEP 301. Use this package to validate classifiers in packages for PyPI upload or download.

%prep
%setup -q -n trove-classifiers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/trove_classifiers
%{python_sitelib}/trove_classifiers-%{version}*-info

%changelog
