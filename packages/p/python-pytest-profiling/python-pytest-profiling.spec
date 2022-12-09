#
# spec file for package python-pytest-profiling
#
# Copyright (c) 2022 SUSE LLC
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
%bcond_without python2
Name:           python-pytest-profiling
Version:        1.7.0
Release:        0
Summary:        Profiling plugin for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-profiling/pytest-profiling-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM pytest-fixtures-pr171-remove-mock.patch -- gh#man-group#pytest-plugins#171
Patch0:         pytest-fixtures-pr171-remove-mock.patch
# https://github.com/man-group/pytest-plugins/issues/209
Patch1:         python-pytest-profiling-no-six.patch
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gprof2dot
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gprof2dot}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python2-mock
%endif
# /SECTION
%python_subpackages

%description
Profiling plugin for py.test

%prep
%autosetup -p1 -n pytest-profiling-%{version}
# Unpin
sed -i 's/more-itertools==5.0.0/more-itertools/' tests/integration/test_profile_integration.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# integration tests omit as they try to use the system image instead of buildroot
%pytest -k 'not test_profile_integration'

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_profiling.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_profiling*.pyc
%{python_sitelib}/pytest_profiling-%{version}*-info

%changelog
