#
# spec file for package python-envier
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


%{?sle15_python_module_pythons}
Name:           python-envier
Version:        0.6.1
Release:        0
Summary:        Python application configuration via the environment
License:        BSD-3-Clause
URL:            https://github.com/DataDog/envier
Source:         https://files.pythonhosted.org/packages/source/e/envier/envier-%{version}.tar.gz
Source1:        https://github.com/DataDog/envier/archive/refs/tags/v%{version}.tar.gz#/envier-%{version}-source1.tar.gz
Patch0:         envier-test_types_assert.patch
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       mypy
Suggests:       python-mypy
BuildArch:      noarch
%python_subpackages

%description
Envier is a Python library for extracting configuration from environment
variables in a declarative and (eventually) 12-factor-app-compliant way.

%prep
%setup -q -n envier-%{version}
mkdir -p envier-%{version}-source1
tar -xzf %{SOURCE1} -C envier-%{version}-source1 --strip-components=1
# Apply the patch to the files from Source1
pushd envier-%{version}-source1
%patch -P0 -p1
popd

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd envier-%{version}-source1
%pytest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/envier
%{python_sitelib}/envier-%{version}.dist-info

%changelog
