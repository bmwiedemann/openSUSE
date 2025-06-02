#
# spec file for package python-moban-ansible
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


# Tests have dependency loop with moban
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define test 1
%define pkg_suffix -test
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
Name:           python-moban-ansible%{pkg_suffix}
Version:        0.0.2
Release:        0
Summary:        Ansible filters, tests and utility functions for moban users
License:        BSD-3-Clause
URL:            https://github.com/moremoban/moban-ansible
Source:         https://files.pythonhosted.org/packages/source/m/moban-ansible/moban-ansible-%{version}.tar.gz
# https://github.com/moremoban/moban-ansible/pull/2
Patch0:         python-moban-ansible-remove-nose.patch
Patch1:         remove-mock.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-moban >= 0.8.1
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module moban >= 0.8.1}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
Ansible filters, tests and utility functions for moban users

%prep
%autosetup -p1 -n moban-ansible-%{version}

%if !%{with test}
%build
%pyproject_wheel
%endif

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/moban[-_]ansible
%{python_sitelib}/moban[-_]ansible-%{version}*-info
%endif

%changelog
