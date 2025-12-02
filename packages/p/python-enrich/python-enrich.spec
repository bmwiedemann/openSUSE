#
# spec file for package python-enrich
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


%{?sle15_python_module_pythons}
Name:           python-enrich
Version:        1.3.0
Release:        0
Summary:        Extends the python-rich library functionality
License:        MIT
URL:            https://github.com/pycontribs/enrich
Source0:        https://github.com/pycontribs/enrich/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove_setuptools_scm.patch -- remove dependency on setuptools-scm
Patch0:         remove_setuptools_scm.patch
# PATCH-FIX-UPSTREAM remove_rich_constraint.patch -- remove the constraint on rich < 12.5, the tests also succeed with rich 14.0 https://github.com/pycontribs/enrich/issues/40
Patch1:         remove_rich_constraint.patch
# PATCH-FIX-UPSTREAM gh#pycontribs/enrich#74
Patch2:         support-pytest-9.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rich
BuildArch:      noarch
%{?python_enable_dependency_generator}
%python_subpackages

%description
Extends the python-rich library functionality
with a set of changes that were not accepted to rich itself.

%prep
%autosetup -n enrich-%{version} -p1
sed -i 's/__VERSION__/%{version}/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#pycontribs/enrich#40
%pytest -k 'not test_rich_console_ex'

%files %{python_files}
%{python_sitelib}/enrich
%{python_sitelib}/enrich-%{version}*info

%changelog
