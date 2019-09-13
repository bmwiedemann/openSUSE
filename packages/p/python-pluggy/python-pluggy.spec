#
# spec file for package python-pluggy
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pluggy%{psuffix}
Version:        0.12.0
Release:        0
Summary:        Plugin registration and hook calling mechanisms for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pluggy
Source:         https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata >= 0.12}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata >= 0.12
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
This is the plugin manager as used by pytest but stripped
of pytest specific details.

During the 0.x series this plugin does not have much documentation
except extensive docstrings in the pluggy.py module.

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
%{python_sitelib}/*
%endif

%changelog
