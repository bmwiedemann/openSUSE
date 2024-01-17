#
# spec file for package python-asdf_coordinates_schemas
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-asdf-coordinates-schemas
Version:        0.1.0
Release:        0
Summary:        ASDF coordinates schemas
License:        BSD-3-Clause
URL:            https://github.com/asdf-format/asdf-coordinates-schemas
Source:         https://files.pythonhosted.org/packages/source/a/asdf-coordinates-schemas/asdf_coordinates_schemas-0.1.0.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires:       python-asdf >= 2.8.0
BuildArch:      noarch
%python_subpackages

%description
ASDF coordinates schemas

%prep
%setup -q -n asdf_coordinates_schemas-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/asdf_coordinates_schemas
%{python_sitelib}/asdf_coordinates_schemas-%{version}*-info
%changelog
