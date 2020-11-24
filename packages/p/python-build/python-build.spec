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
Name:           python-build
Version:        0.1.0
Release:        0
Summary:        Simple PEP517 package builder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/build
Source:         https://github.com/pypa/build/archive/%{version}.tar.gz#/build-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-pep517 >= 0.9
Requires:       python-toml
Requires:       python-typing
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pep517 >= 0.9}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module virtualenv}
# /SECTION
%python_subpackages

%description
Simple PEP517 package builder.

%prep
%setup -q -n build-%{version}

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
