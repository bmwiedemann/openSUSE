#
# spec file for package python-padaos
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


%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-padaos
Version:        0.1.10
Release:        0
Summary:        An intent parser
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/MatthewScholefield/padaos
Source0:        https://files.pythonhosted.org/packages/source/p/padaos/padaos-%{version}.tar.gz
# https://github.com/MycroftAI/padaos/issues/7
Source1:        https://raw.githubusercontent.com/MycroftAI/padaos/master/LICENSE
Source2:        https://raw.githubusercontent.com/MycroftAI/padaos/master/test_padaos.py
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A intent parser Python module.

Padaos converts a series of example sentences into one big chunk of
regex. Each intent is a single compiled regex matcher.

%prep
%setup -q -n padaos-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/padaos.*
%{python_sitelib}/__pycache__/padaos.*
%{python_sitelib}/padaos-%{version}-py%{python_version}.egg-info

%changelog
