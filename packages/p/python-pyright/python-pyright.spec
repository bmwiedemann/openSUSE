#
# spec file for package python-pyright
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pyright
Version:        1.1.376
Release:        0
Summary:        Command line wrapper for pyright
License:        MIT
URL:            https://github.com/RobertCraigie/pyright-python
Source:         https://github.com/RobertCraigie/pyright-python/archive/refs/tags/v%{version}.tar.gz#/pyright-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-subprocess}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nodeenv >= 1.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nodeenv >= 1.6.0}
# /SECTION
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
%python_group_libalternatives pyright pyright-python pyright-langserver pyright-python-langserver
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{_bindir}

%pre
%python_libalternatives_reset_alternative pyright

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
