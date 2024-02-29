#
# spec file for package python-delegator.py
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-delegator.py
Version:        0.1.1
Release:        0
Summary:        Python library for dealing with subprocesses
License:        MIT
URL:            https://github.com/kennethreitz/delegator.py
Source:         https://files.pythonhosted.org/packages/source/d/delegator.py/delegator.py-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/kennethreitz/delegator.py/master/tests/test_chain.py
Patch0:         merged_pr_62.patch
BuildRequires:  %{python_module pexpect >= 4.1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pexpect >= 4.1.0
BuildArch:      noarch
Conflicts:      python-delegator

%python_subpackages

%description
Delegator.py is a library for dealing with subprocesses, inspired
by both "envoy" and "pexpect" (in fact, it depends on it).

%prep
%autosetup -p1 -n delegator.py-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests from master are not compatible.  Likely fixed in next release.
# https://github.com/kennethreitz/delegator.py/pull/71
#%%check
#export PYTHONPATH=${PWD}
#%%python_exec -m pytest test_chain.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/delegator.py
%pycache_only %{python_sitelib}/__pycache__/delegator.*.py*
%{python_sitelib}/delegator.py-%{version}.dist-info

%changelog
