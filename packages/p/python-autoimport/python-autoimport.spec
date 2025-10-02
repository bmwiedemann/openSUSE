#
# spec file for package python-autoimport
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


# Tests are broken currently (version 1.6.1)
%bcond_with tests
%bcond_without libalternatives

Name:           python-autoimport
Version:        1.6.1
Release:        0
Summary:        Autoimport missing python libraries
License:        GPL-3.0-only
URL:            https://github.com/lyz-code/autoimport
Source:         https://files.pythonhosted.org/packages/source/a/autoimport/autoimport-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-autoimport-maison_2_0-support.patch
Patch0:         https://patch-diff.githubusercontent.com/raw/lyz-code/autoimport/pull/259.patch#/python-autoimport-maison_2_0-support.patch
# PATCH-FIX-UPSTREAM python-autoimport-use-pyxdg-module-for-xdg.patch badshah400@gmail.com -- Adapt to upstream renaming of xdg module to xdg_base_dirs
Patch1:         python-autoimport-use-pyxdg-module-for-xdg.patch
BuildRequires:  alts
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
# SECTION test requirements
%if %{with tests}
BuildRequires:  %{python_module autoflake >= 1.4}
BuildRequires:  %{python_module click >= 8.1.3}
BuildRequires:  %{python_module maison >= 2.0.0}
BuildRequires:  %{python_module pyprojroot >= 0.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module sh >= 1.14.2}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       alts
Requires:       python-autoflake >= 1.4
Requires:       python-click >= 8.1.3
Requires:       python-maison >= 2.0.0
Requires:       python-pyprojroot >= 0.2.0
Requires:       python-sh >= 1.14.2
Requires:       python-pyxdg
BuildArch:      noarch
%python_subpackages

%description
Module to help automatically import missing python libraries when developing
code.

%prep
%autosetup -p1 -n autoimport-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/autoimport
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%pytest
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/autoimport
%{python_sitelib}/autoimport
%{python_sitelib}/autoimport-%{version}.dist-info

%changelog
