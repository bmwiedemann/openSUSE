#
# spec file for package python-sphinx-jsonschema
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


Name:           python-sphinx-jsonschema
Version:        1.19.2
Release:        0
Summary:        Sphinx extension to display JSON Schema
License:        GPL-3.0-only
URL:            https://github.com/lnoor/sphinx-jsonschema
# Tarballs from pypi.org are missing license files
Source:         https://github.com/lnoor/sphinx-jsonschema/archive/refs/tags/v.%{version}.tar.gz#/sphinx-jsonschema-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-docutils
Requires:       python-jsonpointer
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module jsonpointer}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Sphinx extension to display JSON Schema.

%prep
%autosetup -p1 -n sphinx-jsonschema-v.%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The tests don't actually properly execute
# see upstream https://github.com/lnoor/sphinx-jsonschema/issues/56
#%%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sphinx[-_]jsonschema
%{python_sitelib}/sphinx[-_]jsonschema-%{version}.dist-info

%changelog
