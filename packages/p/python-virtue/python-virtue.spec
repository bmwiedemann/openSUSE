#
# spec file for package python-virtue
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


%{?sle15_python_module_pythons}
Name:           python-virtue
Version:        2025.2.1
Release:        0
Summary:        After trial comes virtue. A test runner for good
License:        MIT
URL:            https://github.com/Julian/Virtue
Source:         https://files.pythonhosted.org/packages/source/v/virtue/virtue-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Twisted >= 23.10.0rc1}
BuildRequires:  %{python_module attrs >= 19}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pyrsistent}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-Twisted >= 23.10.0rc1
Requires:       python-attrs >= 19
Requires:       python-click
Requires:       python-colorama
Requires:       python-pyrsistent
Suggests:       python-importlib_metadata
BuildArch:      noarch
%python_subpackages

%description
After trial comes virtue. A test runner for good.

%prep
%setup -q -n virtue-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/virtue
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_IGNORE="test_foo"
%pytest -k "not (${PYTEST_IGNORE})"

%post
%python_install_alternative virtue

%postun
%python_uninstall_alternative virtue

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/virtue
%{python_sitelib}/virtue
%{python_sitelib}/virtue-%{version}.dist-info/

%changelog
