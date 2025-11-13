#
# spec file for package python-PubChemPy
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

%{?sle15_python_module_pythons}
%define packagename PubChemPy
Name:           python-PubChemPy
Version:        1.0.5
Release:        0
Summary:        A simple Python wrapper around the PubChem PUG REST API
License:        MIT
URL:            https://github.com/mcs07/PubChemPy
Source:         https://github.com/mcs07/PubChemPy/archive/v%{version}.tar.gz#/PubChemPy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PubChemPy provides a way to interact with PubChem in Python. It allows chemical
searches by name, substructure and similarity, chemical standardization,
conversion between chemical file formats, depiction and retrieval of chemical
properties.

%prep
%setup -q -n %{packagename}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# All the tests connct to the webserver
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pubchempy.py
%pycache_only %{python_sitelib}/__pycache__/pubchempy.*.pyc
%{python_sitelib}/[Pp]ub[Cc]hem[Pp]y-%{version}.dist-info

%changelog
