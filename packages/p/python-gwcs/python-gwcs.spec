#
# spec file for package python-gwcs
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


Name:           python-gwcs
Version:        0.24.0
Release:        0
Summary:        Generalized World Coordinate System
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://gwcs.readthedocs.io/en/latest/
# SourceRepository: https://github.com/spacetelescope/gwcs
Source:         https://files.pythonhosted.org/packages/source/g/gwcs/gwcs-%{version}.tar.gz
BuildRequires:  %{python_module asdf >= 3.3.0}
BuildRequires:  %{python_module asdf-astropy >= 0.5.0}
BuildRequires:  %{python_module asdf_wcs_schemas >= 0.4.0}
BuildRequires:  %{python_module astropy >= 6}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module numpy >= 1.24}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 1.14.1}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf >= 3.3.0
Requires:       python-asdf-astropy >= 0.5.0
Requires:       python-asdf_wcs_schemas >= 0.4.0
Requires:       python-astropy >= 6
Requires:       python-numpy >= 1.24
Requires:       python-scipy >= 1.14.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-astropy >= 0.11.0}
BuildRequires:  %{python_module pytest >= 8}
# /SECTION
%python_subpackages

%description
An Astropy affiliated package providing tools for managing the
World Coordinate System of astronomical data.

%prep
%setup -q -n gwcs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -ra

%files %{python_files}
%doc README.rst
%license licenses/LICENSE.rst licenses/README.rst
%{python_sitelib}/gwcs
%{python_sitelib}/gwcs-%{version}*-info

%changelog
