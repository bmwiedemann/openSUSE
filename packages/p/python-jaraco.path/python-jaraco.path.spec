#
# spec file for package python-jaraco.path
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-jaraco.path
Version:        3.3.1
Release:        0
Summary:        miscellaneous path functions for jaraco packages
License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.path/jaraco.path-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.base}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module singledispatch}
BuildRequires:  python-rpm-macros
Requires:       python-singledispatch
BuildArch:      noarch
%python_subpackages

%description
jaraco.path provides cross platform hidden file detection
and other miscellaneous path helper functions.

%prep
%setup -q -n jaraco.path-%{version}

%build
%python_build

%install
%python_install

%check
%pytest

%files %{python_files}
%license LICENSE
%dir %{python_sitelib}/jaraco/
%{python_sitelib}/jaraco/path.py
%{python_sitelib}/jaraco.path-%{version}-py%{python_version}.egg-info
%pycache_only %{python_sitelib}/jaraco/__pycache__/path*.py*

%changelog
