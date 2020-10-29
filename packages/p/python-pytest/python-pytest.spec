#
# spec file for package python
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-pytest%{psuffix}
Version:        6.1.1
Release:        0
Summary:        Python testing tool with autodiscovery and detailed asserts
License:        MIT
URL:            https://github.com/pytest-dev/pytest
Source:         https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 40.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.4.0
Requires:       python-importlib-metadata >= 0.12
Requires:       python-iniconfig
Requires:       python-more-itertools >= 4.0.0
Requires:       python-packaging
Requires:       python-pluggy >= 0.12
Requires:       python-py >= 1.8.2
Requires:       python-setuptools
Requires:       python-toml
Requires:       python-wcwidth
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python-pytest-doc
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module hypothesis >= 3.56}
BuildRequires:  %{python_module importlib-metadata >= 0.12}
BuildRequires:  %{python_module iniconfig}
BuildRequires:  %{python_module mock}
# nose is really not REQUIRED, the test suite skips over particular
# tests, when the package is not available.
# BuildRequires:  %%{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pygments-pytest}
BuildRequires:  %{python_module pytest >= %{version}}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module xmlschema}
BuildRequires:  lsof
%endif
%if %{python3_version_nodots} < 36
Requires:       python-pathlib2 >= 2.2.0
%endif
%python_subpackages

%description
pytest is a cross-project Python testing tool. It provides:

* auto-discovery of test modules and functions,
* detailed info on failing assert statements (no need to remember
  self.assert* names),
* modular fixtures for managing small or parametrized long-lived test resources.
* multi-paradigm support: you can use py.test to run test suites based on
  unittest (or trial), nose,
* single-source compatibility to Python2.4 all the way up to Python3.3,
  PyPy-1.9 and Jython-2.5.1, and
* many external plugins.

%prep
%setup -q -n pytest-%{version}

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/py.test
%python_clone -a %{buildroot}%{_bindir}/pytest

if [ -x %{buildroot}%{_bindir}/py.test-%{python2_bin_suffix} ]; then
    ln -s py.test-%{python2_bin_suffix} %{buildroot}%{_bindir}/py.test2
fi
if [ -x %{buildroot}%{_bindir}/py.test-%{python3_bin_suffix} ]; then
    ln -s py.test-%{python3_bin_suffix} %{buildroot}%{_bindir}/py.test3
fi

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if ! %{with test}
%post
%{python_install_alternative py.test} \
   --slave %{_bindir}/pytest pytest %{_bindir}/pytest-%{python_version}

%postun
%python_uninstall_alternative py.test

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/py.test
%python_alternative %{_bindir}/pytest
%python2_only %{_bindir}/py.test2
%python3_only %{_bindir}/py.test3
%{python_sitelib}/*
%endif

%changelog
