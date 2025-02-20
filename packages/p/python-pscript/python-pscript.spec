#
# spec file for package python-pscript
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


%define modname pscript
Name:           python-pscript
Version:        0.8.0
Release:        0
Summary:        Python to JavaScript compiler
License:        BSD-2-Clause
URL:            https://github.com/flexxui/pscript
Source:         https://github.com/flexxui/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  nodejs
# /SECTION
%python_subpackages

%description
PScript is a Python to JavaScript compiler, and is also the name of the subset
of Python that this compiler supports.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/flexxui/pscript/issues/69
%pytest -k 'not test_async_and_await' tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pscript
%{python_sitelib}/pscript-%{version}.dist-info

%changelog
