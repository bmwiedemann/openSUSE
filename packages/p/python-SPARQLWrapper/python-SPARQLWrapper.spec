#
# spec file for package python-SPARQLWrapper
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-SPARQLWrapper
Version:        1.8.5
Release:        0
Summary:        SPARQL Endpoint interface to Python
License:        W3C
URL:            http://sparql-wrapper.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/S/SPARQLWrapper/SPARQLWrapper-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rdflib >= 4.0
BuildArch:      noarch
%python_subpackages

%description
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%prep
%setup -q -n SPARQLWrapper-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#%%pytest test

%files %{python_files}
%license LICENSE.txt
%doc README.rst AUTHORS.md
%{python_sitelib}/SPARQLWrapper/
%{python_sitelib}/SPARQLWrapper-%{version}-py*.egg-info

%changelog
