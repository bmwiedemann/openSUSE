#
# spec file for package python-build
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
# TW defined --without python2
%bcond_without python2
Name:           python-build
Version:        0.1.0
Release:        0
Summary:        Simple PEP517 package builder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/build
Source:         https://github.com/pypa/build/archive/%{version}.tar.gz#/build-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-unused-import.patch -- remove unused import https://github.com/pypa/build/commit/efa3710
Patch0:         remove-unused-import.patch
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pep517 >= 0.9}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python-typing
BuildRequires:  python-virtualenv >= 20.0.35
%endif
BuildRequires:  (python3-importlib_metadata if python3-base < 3.8)
BuildRequires:  (python36-importlib_metadata if python36-base)
Requires:       python-packaging
Requires:       python-pep517 >= 0.9
Requires:       python-toml
Requires:       (python-importlib_metadata if python-base < 3.8)
%ifpython2
Requires:       python-typing
Requires:       python-virtualenv >= 20.0.35
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Simple PEP517 package builder.

%prep
%autosetup -p1 -n build-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyproject-build
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_create_isolated_build_host (x2) fail due to venv/test rig
%pytest -k 'not (test_create_isolated_build_host_with_no_pip or test_create_isolated_build_has_with_pip)'

%post
%python_install_alternative pyproject-build

%postun
%python_uninstall_alternative pyproject-build

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyproject-build
%{python_sitelib}/*

%changelog
