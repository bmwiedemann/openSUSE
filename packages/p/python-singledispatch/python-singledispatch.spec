#
# spec file for package python-singledispatch
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
Name:           python-singledispatch
Version:        3.6.1
Release:        0
Summary:        Provides functools.singledispatch for Python 2.x
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ambv/singledispatch
Source:         https://pypi.python.org/packages/source/s/singledispatch/singledispatch-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toml}
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
PEP 443 proposed to expose a mechanism in the functools standard library module
in Python 3.4 that provides a simple form of generic programming known as
single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%prep
%setup -q -n singledispatch-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec test_singledispatch.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/singledispatch
%{python_sitelib}/singledispatch-%{version}-py%{python_version}.egg-info

%changelog
