#
# spec file for package python-voluptuous-serialize
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


Name:           python-voluptuous-serialize
Version:        2.7.0
Release:        0
Summary:        Python module to convert voluptuous schemas to dictionaries
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/balloob/voluptuous-serialize
Source:         https://files.pythonhosted.org/packages/source/v/voluptuous-serialize/voluptuous_serialize-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-voluptuous
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module voluptuous}
# /SECTION
%python_subpackages

%description
A Python module to convert voluptuous schemas to dictionaries.

%prep
%setup -q -n voluptuous_serialize-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/voluptuous[-_]serialize
%{python_sitelib}/voluptuous[-_]serialize-%{version}*-info

%changelog
