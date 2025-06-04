#
# spec file for package python-stone
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


%bcond_without libalternatives
Name:           python-stone
Version:        3.3.9
Release:        0
Summary:        Stone is an interface description language (IDL) for APIs
License:        MIT
URL:            https://github.com/dropbox/stone
Source:         https://github.com/dropbox/stone/archive/refs/tags/v%{version}.tar.gz#/stone-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/dropbox/stone/pull/318 remove dependency on six
Patch:          remove-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 3.0.3}
BuildRequires:  %{python_module packaging >= 21.0}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  alts
Requires:       alts
Requires:       python-Jinja2 >= 3.0.3
Requires:       python-packaging >= 21.0
Requires:       python-ply >= 3.4
BuildArch:      noarch
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
