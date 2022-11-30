#
# spec file for package python-pytest-sugar
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


Name:           python-pytest-sugar
Version:        0.9.6
Release:        0
Summary:        Pretty printer for pytest progress
License:        BSD-3-Clause
URL:            https://github.com/Frozenball/pytest-sugar
Source:         https://files.pythonhosted.org/packages/source/p/pytest-sugar/pytest-sugar-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module termcolor}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-termcolor
BuildArch:      noarch
%python_subpackages

%description
pytest-sugar is a plugin for py.test that shows failures and errors instantly and shows a progress bar.

%prep
%setup -q -n pytest-sugar-%{version}

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
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/pytest_sugar.py
%{python_sitelib}/pytest_sugar-%{version}*-info

%changelog
