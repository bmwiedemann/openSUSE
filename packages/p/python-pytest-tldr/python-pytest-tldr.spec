#
# spec file for package python-pytest-tldr
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


Name:           python-pytest-tldr
Version:        0.2.5
Release:        0
Summary:        A pytest plugin that limits the output to just the things you need
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/freakboy3742/pytest-tldr
Source:         https://files.pythonhosted.org/packages/source/p/pytest-tldr/pytest-tldr-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.5.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.5.0
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin that limits the output to just the things you need.

%prep
%setup -q -n pytest-tldr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/pytest_tldr.py
%{python_sitelib}/pytest_tldr-%{version}*-info

%changelog
