#
# spec file for package python-compat-patcher-core
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-compat-patcher-core
Version:        2.2
Release:        0
Summary:        Python patcher system
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pakal/compat-patcher-core
Source:         https://github.com/pakal/compat-patcher-core/archive/refs/tags/release-%{version}.tar.gz#/compat-patch-core-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pakal/compat-patcher-core/pull/3 Get rid of the six dependency
Patch:          no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  cookiecutter > 1.6.0
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       cookiecutter > 1.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli}
BuildRequires:  python3-pytest-cookies
# /SECTION
%python_subpackages

%description
Python patcher system to allow easy and lasting API compatibility.

%prep
%autosetup -p1 -n compat-patcher-core-release-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Cookiecutter is only available as python3
%python_expand [ %{_bindir}/$python -ef %{_bindir}/python3 ] ||  $python_ignore="--ignore tests/test_cookiecutter_recipe.py"
# _and_run_tests: use setup.py test
%pytest tests ${$python_ignore} -k 'not _and_run_tests'

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/compat_patcher_core
%{python_sitelib}/compat_patcher_core-%{version}.dist-info

%changelog
