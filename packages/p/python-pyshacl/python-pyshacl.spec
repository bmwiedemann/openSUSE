#
# spec file for package python-pyshacl
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications or additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, or modifications or additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-pyshacl
Version:        0.30.1
Release:        0
Summary:        Python SHACL Validator
License:        Apache-2.0
URL:            https://www.pyshacl.app/
Source0:        pyshacl-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module owlrl}
BuildRequires:  %{python_module pyduktape2}
BuildRequires:  %{python_module prettytable}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rdflib}
BuildRequires:  fdupes
Requires:       python-owlrl
Requires:       python-pyduktape2
Requires:       python-prettytable
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is a pure Python module which allows for the validation of RDF graphs against
Shapes Constraint Language (SHACL) graphs. This module uses the rdflib Python
library for working with RDF or is dependent on the OWL-RL Python
module for OWL2 RL Profile based expansion of data graphs.

%prep
%autosetup -p1 -n pyshacl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/pyshacl_server
%python_clone -a %{buildroot}%{_bindir}/pyshacl_validate
%python_clone -a %{buildroot}%{_bindir}/pyshacl_rules
%python_clone -a %{buildroot}%{_bindir}/pyshacl
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyshacl
%python_install_alternative pyshacl_rules
%python_install_alternative pyshacl_validate
%python_install_alternative pyshacl_server

%postun
%python_uninstall_alternative pyshacl
%python_uninstall_alternative pyshacl_rules
%python_uninstall_alternative pyshacl_validate
%python_uninstall_alternative pyshacl_server

%check
# As there is no web access these fail
dontcheck="test_154 or test_cmdline_web or test_cmdline_jsonld or test_web_retrieve or test_web_retrieve_fail or test_owl_imports or test_owl_imports_fail"

# Somehow files are missing
dontcheck+=" or test_cmdline or test_cmdline_fail or test_cmdline_table or test_cmdline_rules"

%pytest -k "not ($dontcheck)"

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/pyshacl
%{python_sitelib}/pyshacl-%{version}*info
%python_alternative %{_bindir}/pyshacl
%python_alternative %{_bindir}/pyshacl_rules
%python_alternative %{_bindir}/pyshacl_validate
%python_alternative %{_bindir}/pyshacl_server

%changelog
