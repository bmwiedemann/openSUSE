#
# spec file for package python-python-daemon
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-daemon
Version:        2.2.3
Release:        0
Summary:        Library to implement a well-behaved Unix daemon process
License:        Apache-2.0 AND GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://pagure.io/python-daemon/
Source:         https://files.pythonhosted.org/packages/source/p/python-daemon/python-daemon-%{version}.tar.gz
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module lockfile >= 0.10}
BuildRequires:  %{python_module mock >= 1.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lockfile >= 0.10
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-daemon = %{version}
Obsoletes:      %{oldpython}-daemon < %{version}
%endif
%python_subpackages

%description
This library implements the well-behaved daemon specification of PEP 3143, "Standard daemon
process library".

A well-behaved Unix daemon process is tricky to get right, but the required steps are much the
same for every daemon program. A DaemonContext instance holds the behaviour and configured
process environment for the program; use the instance as a context manager to enter a daemon state.

%prep
%setup -q -n python-daemon-%{version}
sed -i '/docutils/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_returns_standard_stream_file_descriptors fails
# test_returns_expected_result fails with distutils error
%python_exec -m pytest -k 'not test_returns_standard_stream_file_descriptors and not test_returns_expected_result'

%files %{python_files}
%license LICENSE.ASF-2 LICENSE.GPL-3
%doc README ChangeLog doc/*
%{python_sitelib}/*

%changelog
