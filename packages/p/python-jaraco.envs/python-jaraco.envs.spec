#
# spec file for package python-jaraco.envs
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


%{?sle15_python_module_pythons}
Name:           python-jaraco.envs
Version:        2.4.0
Release:        0
Summary:        Classes for Python Virtual Environments
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.envs
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.envs/jaraco.envs-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-path
Requires:       python-virtualenv
Recommends:     python-tox
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module path}
BuildRequires:  %{python_module virtualenv}
# /SECTION
%python_subpackages

%description
Classes for orchestrating Python (virtual) environments.

%prep
%setup -q -n jaraco.envs-%{version}
# Avoid tox in openSUSE:Factory:Rings:1-MinimalX
sed -i '/tox/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.envs-%{version}*info
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/envs.py*
%pycache_only %dir %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/envs*.py*

%changelog
