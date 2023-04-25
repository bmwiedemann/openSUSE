#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-pluggy%{psuffix}
Version:        1.0.0
Release:        0
Summary:        A minimalist production ready plugin system
License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source:         https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata >= 0.12
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module importlib-metadata >= 0.12 if %python-base < 3.8}
BuildRequires:  %{python_module pytest >= 6.2.5}
%endif
%python_subpackages

%description
This is the core framework used by the pytest, tox, and devpi projects.

%prep
%setup -q -n pluggy-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest testing
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/pluggy
%{python_sitelib}/pluggy-%{version}*-info
%endif

%changelog
