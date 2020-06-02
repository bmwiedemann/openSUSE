#
# spec file for package python-PubChemPy
#
# Copyright (c) 2020 SUSE LLC
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


%define packagename PubChemPy
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-PubChemPy
Version:        1.0.4
Release:        0
Summary:        A simple Python wrapper around the PubChem PUG REST API
License:        MIT
URL:            https://github.com/mcs07/PubChemPy
Source:         https://github.com/mcs07/PubChemPy/archive/v%{version}.tar.gz#/PubChemPy-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# All the tests connct to the webserver
#%%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python_sitelib}/*

%changelog
