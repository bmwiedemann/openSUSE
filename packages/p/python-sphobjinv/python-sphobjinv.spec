#
# spec file for package python-sphobjinv
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
Name:           python-sphobjinv
Version:        2.3.1.2
Release:        0
Summary:        Sphinx objectsinv Inspection/Manipulation Tool
License:        MIT
URL:            https://github.com/bskinn/sphobjinv
Source:         https://github.com/bskinn/sphobjinv/archive/refs/tags/v%{version}.tar.gz#/sphobjinv-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2
Requires:       python-certifi
Requires:       python-jsonschema >= 3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module attrs >= 19.4}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module dictdiffer}
BuildRequires:  %{python_module jsonschema >= 3.0}
BuildRequires:  %{python_module pytest >= 4.4.0}
BuildRequires:  %{python_module pytest-check >= 1.1.2}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module sphinx_rtd_theme}
# /SECTION
%python_subpackages

%description
Sphinx objects.inv Inspection/Manipulation Tool

%prep
%setup -q -n sphobjinv-%{version}
sed -i '1{/^#!/d}' src/sphobjinv/_vendored/fuzzywuzzy/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sphobjinv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we don't have stdio-mgr
ignoretests="--ignore tests/test_cli.py --ignore tests/test_cli_nonlocal.py"
# Errors with invalid inventory source type: we didn't build the docs and don't have the inventory there
sed -i 's/--doctest-glob="README.rst"//' tox.ini
# failing tests with sphinx 8.2, gh#bskinn/sphobjinv#314
donttest="test_name_lead_chars"
%pytest -k "not ($donttest)" $ignoretests

%post
%python_install_alternative sphobjinv

%postun
%python_uninstall_alternative sphobjinv

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%python_alternative %{_bindir}/sphobjinv
%{python_sitelib}/sphobjinv
%{python_sitelib}/sphobjinv-%{version}.dist-info

%changelog
