#
# spec file for package python-pytest-pycodestyle
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


%define skip_python2 1
Name:           python-pytest-pycodestyle
Version:        2.3.1
Release:        0
Summary:        Pytest plugin to run pycodestyle
License:        MIT
URL:            https://github.com/henry0312/pytest-pycodestyle
Source:         https://files.pythonhosted.org/packages/source/p/pytest-pycodestyle/pytest-pycodestyle-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest >= 5.4}
BuildRequires:  %{python_module pytest-isort}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-py
Requires:       python-pycodestyle
Requires:       python-pytest
Requires:       python-setuptools
Provides:       python-pytest-codestyle = %{version}
Obsoletes:      python-pytest-codestyle < %{version}
BuildArch:      noarch
%python_subpackages

%description
pytest plugin to run pycodestyle in python tests

%prep
%setup -q -n pytest-pycodestyle-%{version}
sed -i -e 's:~=:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/pytest_pycodestyle.py
%{python_sitelib}/pytest_pycodestyle-%{version}*-info

%changelog
