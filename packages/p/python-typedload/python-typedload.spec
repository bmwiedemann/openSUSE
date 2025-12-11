#
# spec file for package python-typedload
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


Name:           python-typedload
Version:        2.39
Release:        0
Summary:        Load and dump data from json-like format into typed data structures
License:        GPL-3.0-only
URL:            https://ltworf.codeberg.page/typedload/
Source0:        https://codeberg.org/ltworf/typedload/releases/download/%{version}/typedload_%{version}.orig.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Load and dump data from json-like format into typed data structures

%prep
%setup -q -n typedload

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/__main__.py has a version specific test collection and calls unittest.main()
%python_exec -B -m tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/typedload
%{python_sitelib}/typedload-%{version}.dist-info

%changelog
