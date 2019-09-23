#
# spec file for package python-futures
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-futures
Version:        3.3.0
Release:        0
Summary:        Backport of the concurrent.futures package from Python 3.2
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/agronholm/pythonfutures
Source:         https://files.pythonhosted.org/packages/source/f/futures/futures-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
# This packages contain module test from stdlib, nothing to with
# BuildArch field
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  python-test
%endif
BuildRequires:  python2-devel
BuildArch:      noarch
%python_subpackages

%description
A Java-style futures package for Python

This package is described in PEP-3148 and is included in Python 3.2.

See the Python documentation for a full description.

%prep
%setup -q -n futures-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_futures.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/concurrent/
%{python_sitelib}/futures-%{version}-py*.egg-info

%changelog
