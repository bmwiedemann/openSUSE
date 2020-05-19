#
# spec file for package python-pytest-doctestplus
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.6.1
Release:        0
Summary:        Pytest plugin with advanced doctest features
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-doctestplus
Source:         https://files.pythonhosted.org/packages/source/p/pytest-doctestplus/pytest-doctestplus-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 4.0
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-doctestplus >= %{version}}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
This package contains a plugin for the pytest framework that provides
advanced doctest support and enables the testing of reStructuredText
(".rst") files.

%prep
%setup -q -n pytest-doctestplus-%{version}
# do not change the pytest behaviour for us
rm -f setup.cfg

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
# README.rst contains Python 3 only imports
%pytest --doctest-plus --doctest-rst -k 'not README.rst'
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/*
%endif

%changelog
