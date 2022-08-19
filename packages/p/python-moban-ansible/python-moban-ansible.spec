#
# spec file
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
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
BuildRequires:  %{python_module setuptools}
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
%python_build
%endif

%if !%{with test}
%install
%python_install
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
%{python_sitelib}/*
%endif

%changelog
