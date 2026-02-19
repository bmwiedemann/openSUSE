#
# spec file for package python-rich-click
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
Name:           python-rich-click
Version:        1.9.7
Release:        0
Summary:        Format click help output nicely with rich
License:        MIT
URL:            https://github.com/ewels/rich-click
Source:         https://github.com/ewels/rich-click/archive/refs/tags/v%{version}.tar.gz#/rich_click-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-click >= 8
Requires:       python-rich >= 12
%if %{python3_version_nodots} < 311
Requires:       python-typing_extensions >= 4
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 8}
BuildRequires:  %{python_module inline-snapshot >= 0.24}
BuildRequires:  %{python_module pytest-cov >= 5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 12}
BuildRequires:  %{python_module typer >= 0.15}
BuildRequires:  %{python_module typing_extensions >= 4}
# /SECTION
%python_subpackages

%description
Format click help output nicely with rich.

%prep
%setup -q -n rich-click-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rich-click
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative rich-click

%check
# Requires specific modifications to sys.path and PYTHONPATH that
# don't behave well with our macros
%pytest -x --ignore tests/test_rich_click_cli.py

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/rich-click
%{python_sitelib}/rich_click
%{python_sitelib}/rich_click-%{version}.dist-info

%changelog
