#
# spec file for package python-jschema_to_python
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-jschema-to-python
Version:        1.2.3
Release:        0
Summary:        Generate source code for Python classes from a JSON schema
License:        MIT
URL:            https://github.com/microsoft/jschema-to-python
Source:         https://files.pythonhosted.org/packages/source/j/jschema-to-python/jschema_to_python-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pbr}
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs
Requires:       python-jsonpickle
Requires:       python-pbr
BuildArch:      noarch
%python_subpackages

%description
Generate source code for Python classes from a JSON schema.

%prep
%setup -q -n jschema_to_python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/

%files %{python_files}
%{python_sitelib}/*

%changelog
