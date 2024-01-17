#
# spec file for package python-cov-core
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
Name:           python-cov-core
Version:        1.15.0
Release:        0
Summary:        Plugin core for use by pytest-cov, nose-cov and nose2-cov
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/schlamar/cov-core
Source:         https://files.pythonhosted.org/packages/source/c/cov-core/cov-core-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage
BuildArch:      noarch
%python_subpackages

%description
This is a lib package for use by pytest-cov, nose-cov and nose2-cov.  Unless your developing a
coverage plugin for a test framework then you probably want one of those.

%prep
%setup -q -n cov-core-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/cov_core.py*
%{python_sitelib}/cov_core_init.py*
%{python_sitelib}/cov_core-%{version}-py%{python_version}.egg-info

%changelog
