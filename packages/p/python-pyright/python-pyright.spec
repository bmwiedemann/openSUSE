#
# spec file for package python-pyright
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
Name:           python-pyright
Version:        1.1.376
Release:        0
Summary:        Command line wrapper for pyright
License:        MIT
URL:            https://github.com/RobertCraigie/pyright-python
Source:		https://github.com/RobertCraigie/pyright-python/archive/refs/tags/v%{version}.tar.gz#/pyright-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-subprocess}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module nodeenv >= 1.6.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-nodeenv >= 1.6.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Command line wrapper for pyright

%prep
%autosetup -p1 -n pyright-python-%{version}

%build
%pyproject_wheel

%check
# NOTE: disable test_main.py, test_node.py, and test_langserver.py as the tests
# required internet access, by attempting to download the version
# file from the main server at
# https://raw.githubusercontent.com/microsoft/pylance-release/main/releases/{pylance_version}.json
%pytest --ignore tests/test_main.py --ignore tests/test_langserver.py --ignore tests/test_node.py

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyright
%python_clone -a %{buildroot}%{_bindir}/pyright-python
%python_clone -a %{buildroot}%{_bindir}/pyright-langserver
%python_clone -a %{buildroot}%{_bindir}/pyright-python-langserver
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{_bindir}

%post
%python_install_alternative pyright pyright-python pyright-langserver pyright-python-langserver

%postun
%python_uninstall_alternative pyright

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyright
%python_alternative %{_bindir}/pyright-python
%python_alternative %{_bindir}/pyright-langserver
%python_alternative %{_bindir}/pyright-python-langserver
%{python_sitelib}/pyright
%{python_sitelib}/pyright-%{version}.dist-info

%changelog
