#
# spec file for package python-SPARQLWrapper
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
Name:           python-SPARQLWrapper
Version:        2.0.0
Release:        0
Summary:        SPARQL Endpoint interface to Python
License:        W3C
URL:            https://rdflib.dev/sparqlwrapper/
Source:         https://files.pythonhosted.org/packages/source/S/SPARQLWrapper/SPARQLWrapper-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rdflib >= 4.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%prep
%setup -q -n SPARQLWrapper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rqw
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#%%pytest test

%post
%python_install_alternative rqw

%postun
%python_uninstall_alternative rqw

%files %{python_files}
%license LICENSE.txt
%doc README.rst AUTHORS.md
%python_alternative %{_bindir}/rqw
%{python_sitelib}/SPARQLWrapper
%{python_sitelib}/SPARQLWrapper-%{version}.dist-info

%changelog
