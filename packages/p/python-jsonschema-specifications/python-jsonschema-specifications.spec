#
# spec file for package python-jsonschema-specifications
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-jsonschema-specifications
Version:        2024.10.1
Release:        0
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema-specifications
Source:         https://files.pythonhosted.org/packages/source/j/jsonschema-specifications/jsonschema_specifications-%{version}.tar.gz#/jsonschema_specifications-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module importlib_resources}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module referencing >= 0.31.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-referencing >= 0.31.0
BuildArch:      noarch
%python_subpackages

%description
The JSON Schema meta-schemas and vocabularies, exposed as a Registry

%prep
%setup -q -n jsonschema_specifications-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/jsonschema_specifications
%{python_sitelib}/jsonschema_specifications-%{version}.dist-info/

%changelog
