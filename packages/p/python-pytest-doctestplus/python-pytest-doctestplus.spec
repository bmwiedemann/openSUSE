#
# spec file for package python-pytest-doctestplus-test
#
# Copyright (c) 2021 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-doctestplus%{psuffix}
Version:        0.9.0
Release:        0
Summary:        Pytest plugin with advanced doctest features
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-doctestplus
Source:         https://files.pythonhosted.org/packages/source/p/pytest-doctestplus/pytest-doctestplus-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 4.6
Requires:       python-setuptools >= 30.3.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pip >= 19.3.1}
BuildRequires:  %{python_module pytest-doctestplus = %{version}}
%endif
%python_subpackages

%description
This package contains a plugin for the pytest framework that provides
advanced doctest support and enables the testing of reStructuredText
(".rst") files.

%prep
%setup -q -n pytest-doctestplus-%{version}
# https://build.opensuse.org/request/show/889802
sed -i '/filterwarnings/,/\s+/ { /error/ a \        ignore:.*unclosed file.*:ResourceWarning
}' setup.cfg

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export LANG=en_US.UTF8
export PY_IGNORE_IMPORTMISMATCH=1
# -k: inline pytest calls with -We, https://build.opensuse.org/request/show/889802
%pytest tests/ --doctest-plus --doctest-rst -k "not (test_doctestplus and warnings)"
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_doctestplus
%{python_sitelib}/pytest_doctestplus-%{version}*-info
%endif

%changelog
