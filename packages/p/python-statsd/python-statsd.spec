#
# spec file for package python-statsd
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-statsd
Version:        4.0.1
Release:        0
Summary:        A simple statsd client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jsocol/pystatsd
Source:         https://files.pythonhosted.org/packages/source/s/statsd/statsd-%{version}.tar.gz
Patch0:         remove-nose.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
statsd is a front-end to Graphite. This is a Python client
for the statsd daemon.

%prep
%autosetup -p1 -n statsd-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/jsocol/pystatsd/pull/150
sed -i 's:import mock:from unittest import mock:' statsd/tests.py
%pytest statsd/tests.py

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/statsd
%{python_sitelib}/statsd-%{version}.dist-info

%changelog
