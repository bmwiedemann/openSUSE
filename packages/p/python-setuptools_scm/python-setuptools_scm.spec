#
# spec file for package python-setuptools_scm
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-setuptools_scm%{psuffix}
Version:        4.1.2
Release:        0
Summary:        Python setuptools handler for SCM tags
License:        MIT
URL:            https://github.com/pypa/setuptools_scm
Source:         https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
Patch0:         add-rpmfail-pytest-markers.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Suggests:       python-toml
BuildArch:      noarch
%if %{with test}
# Testing requirements
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm = %{version}}
BuildRequires:  %{python_module toml}
BuildRequires:  git-core
BuildRequires:  mercurial
%endif
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     git-core
%endif
%python_subpackages

%description
The setuptools_scm package handles managing one's Python package versions
in SCM metadata. It also handles file finders for the supperted SCMs.

%prep
%setup -q -n setuptools_scm-%{version}
%autopatch -p1
sed -i 's/yield_fixture/fixture/' testing/conftest.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# both tests in test_integration.py encounter https://github.com/pypa/setuptools_scm/issues/386 (at least on Python 2)
# ignore unraisable exceptions (basically https://github.com/pypa/setuptools_scm/commit/cf54011725bb5e6ac9911b06e23ffc5c2938a53f)
%pytest -p no:unraisableexception -k 'not test_integration'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/setuptools_scm*
%endif

%changelog
