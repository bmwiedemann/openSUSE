#
# spec file for package python-testtools
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-testtools%{psuffix}
Version:        2.4.0
Release:        0
Summary:        Extensions to the Python Standard Library Unit Testing Framework
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/testing-cabal/testtools
Source:         https://files.pythonhosted.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# unittest2 is not neccessary to run testsuite
# removing unittest2 entirely:
# https://github.com/testing-cabal/testtools/pull/277
Patch0:         python-testtools-no-unittest2.patch
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-extras >= 1.0.0
Requires:       python-pbr >= 0.11
Requires:       python-python-mimeparse
Requires:       python-six >= 1.4.0
Requires:       python-traceback2
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module extras >= 1.0.0}
BuildRequires:  %{python_module python-mimeparse}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module traceback2}
%endif
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Recommends:     python-fixtures >= 1.3.0
%endif
%python_subpackages

%description
testtools is a set of extensions to the Python standard library's unit tests
framework. These extensions have been derived from many years of experience
with unit tests in Python and come from many different sources. testtools
also ports recent unittest changes all the way back to Python 2.4.

%prep
%setup -q -n testtools-%{version}
%patch0 -p1
sed -i '/unittest2/d' requirements.txt setup.cfg

%if !%{with test}
%build
%python_build
%endif

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_exec -m testtools.run testtools.tests.test_suite
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc NEWS README.rst
%{python_sitelib}/testtools
%{python_sitelib}/testtools-%{version}-py*.egg-info
%endif

%changelog
