#
# spec file for package python-python-jsonschema-objects
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-python-jsonschema-objects
Version:        0.3.11
Release:        0
Summary:        An object wrapper for JSON Schema definitions
License:        MIT
Group:          Development/Languages/Python
URL:            https://python-jsonschema-objects.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/p/python_jsonschema_objects/python_jsonschema_objects-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 18.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown >= 2.4
Requires:       python-inflection >= 0.2
Requires:       python-jsonschema >= 2.3
Requires:       python-six >= 1.5.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Markdown >= 2.4}
BuildRequires:  %{python_module inflection >= 0.2}
BuildRequires:  %{python_module jsonschema >= 2.3}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.5.2}
# /SECTION
%python_subpackages

%description
An object wrapper for JSON Schema definitions

%prep
%setup -q -n python_jsonschema_objects-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/python_jsonschema_objects/examples/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
