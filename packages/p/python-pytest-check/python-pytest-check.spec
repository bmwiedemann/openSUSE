#
# spec file for package python-pytest-check
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
Name:           python-pytest-check
Version:        2.8.0
Release:        0
Summary:        A pytest plugin that allows multiple failures per test
License:        MIT
URL:            https://github.com/okken/pytest-check
Source:         https://files.pythonhosted.org/packages/source/p/pytest-check/pytest_check-%{version}.tar.gz
# Only include this patch for 15.6 and 16.0 builds
Patch0:         pytest-check-no-new-classifiers.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module typing-extensions >= 4.12.2 if %python-base < 3.11}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 7.0.0
%if %{python_version_nodots} < 311
Requires:       python-typing-extensions >= 4.12.2
%endif
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin that allows multiple failures per test. A rewrite of pytest-expect

%prep
%setup -q -n pytest_check-%{version}

# Only include this patch for 15.6 and 16.0 builds
%if 0%{?sle_version} == 150600 || 0%{?sle_version} == 160000
%autopatch -p1
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md changelog.md
%{python_sitelib}/pytest_check
%{python_sitelib}/pytest_check-%{version}*-info

%changelog
