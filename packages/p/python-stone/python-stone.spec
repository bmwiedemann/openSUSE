#
# spec file for package python-stone
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
%{?sle15_python_module_pythons}
Name:           python-stone
Version:        3.5.5
Release:        0
Summary:        Stone is an interface description language (IDL) for APIs
License:        MIT
URL:            https://github.com/dropbox/stone
Source:         https://github.com/dropbox/stone/archive/refs/tags/v%{version}.tar.gz#/stone-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Jinja2 >= 3.1.6
Requires:       python-packaging >= 26.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 3.1.6}
BuildRequires:  %{python_module packaging >= 26.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
# /SECTION
%python_subpackages

%description
Stone is an interface description language (IDL) for APIs.

%prep
%autosetup -p1 -n stone-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/stone
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative stone

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE
%python_alternative %{_bindir}/stone
%{python_sitelib}/stone
%{python_sitelib}/stone-%{version}.dist-info

%changelog
