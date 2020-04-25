#
# spec file for package python-jaraco.envs
#
# Copyright (c) 2020 SUSE LLC
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
# requires python-path
%define skip_python2 1
Name:           python-jaraco.envs
Version:        2.0.0
Release:        0
Summary:        Classes for Python Virtual Environments
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.envs
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.envs/jaraco.envs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-path
Requires:       python-virtualenv
BuildArch:      noarch
%python_subpackages

%description
Classes for orchestrating Python (virtual) environments.

%prep
%setup -q -n jaraco.envs-%{version}
sed -i 's/--flake8 --black --cov//' pytest.ini

%build
%python_build

%install
%python_install
%{python_expand rm -f %{buildroot}%{$python_sitelib}/jaraco/__init__.py* \
  %{buildroot}%{$python_sitelib}/jaraco/__pycache__/__init__.*
  %fdupes %{buildroot}%{$python_sitelib}
}

%check
# no upstream tests

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.envs-*-py*.egg-info
%{python_sitelib}/jaraco*

%changelog
