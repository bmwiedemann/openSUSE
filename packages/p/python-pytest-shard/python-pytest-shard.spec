#
# spec file for package python-pytest-shard
#
# Copyright (c) 2025 SUSE LLC
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

%define short_name pytest-shard
%{?sle15_python_module_pythons}
Name:           python-pytest-shard
Version:        0.1.2
Release:        0
Summary:        Shard tests to support parallelism across multiple machines
License:        MIT 
URL:            https://github.com/AdamGleave/pytest-shard 
Source:         %{short_name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Shards tests based on a hash of their test name enabling easy parallelism across machines, suitable for a wide variety
of continuous integration services. Tests are split at the finest level of granularity, individual test cases, enabling
parallelism even if all of your tests are in a single file (or even single parameterized test method).

%prep
%autosetup -p1 -n %{short_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/pytest_shard

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_shard
%{python_sitelib}/pytest_shard-%{version}.*info

%changelog

