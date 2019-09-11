#
# spec file for package python-delegator.py
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
Name:           python-delegator.py
Version:        0.1.1
Release:        0
Summary:        Python library for dealing with subprocesses
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/kennethreitz/delegator.py
Source:         https://files.pythonhosted.org/packages/source/d/delegator.py/delegator.py-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/kennethreitz/delegator.py/master/tests/test_chain.py
Patch0:         exclude-eof-from-result.patch
BuildRequires:  %{python_module pexpect >= 4.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%setup -q -n delegator.py-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests from master are not compatible.  Likely fixed in next release.
# https://github.com/kennethreitz/delegator.py/pull/71
#%%check
#export PYTHONPATH=${PWD}
#%%python_exec -m pytest test_chain.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
