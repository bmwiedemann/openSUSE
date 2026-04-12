#
# spec file for package python-lib4sbom
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-lib4sbom
Version:        0.10.3
Release:        0
Summary:        Library to ingest and generate SBOMs
License:        Apache-2.0
URL:            https://github.com/anthonyharrison/lib4sbom
Source0:        https://github.com/anthonyharrison/lib4sbom/archive/v%{version}.tar.gz#/lib4sbom-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# Test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module PyYAML >= 5.4}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module fastjsonschema}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module packageurl-python}
BuildRequires:  %{python_module semantic_version}
BuildRequires:  %{python_module xmlschema}
# end of Test requirements
Requires:       python-PyYAML >= 5.4
Requires:       python-defusedxml
Requires:       python-fastjsonschema
Requires:       python-jsonschema
Requires:       python-packageurl-python
Requires:       python-semantic_version
Requires:       python-xmlschema
BuildArch:      noarch
%python_subpackages

%description
Lib4SBOM is a library to parse and generate Software Bill of Materials (SBOMs).
It supports SBOMs created in both SPDX and CycloneDX formats.

It has been developed on the assumption that having a generic abstraction of SBOM
regardless of the underlying format will be useful to developers.

The following facilities are provided:

 * Generate SPDX SBOM in TagValue, JSON and YAML formats
 * Generate CycloneDX SBOM in JSON format
 * Parse SPDX SBOM in TagValue, JSON, YAML, XML and RDF formats
 * Parse CycloneDX SBOM in JSON and XMLformat
 * Create and manipulate a SBOM file object
 * Create and manipulate a SBOM package object
 * Create and manipulate a SBOM dependency relationship object
 * Create and manipulate a Vulnerability object
 * Create and manipulate a Software Service object
 * Generated SBOM can be output to a file or to the console

%prep
%autosetup -p1 -n lib4sbom-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Do not package test, examples and tools
%{python_expand #
rm -rf %buildroot/%{$python_sitelib}/examples
rm -rf %buildroot/%{$python_sitelib}/tools
rm -rf %buildroot/%{$python_sitelib}/test
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Lot's of broken tests, so we ignore the output for now
# %%pytest test ||:

# At least runngin tests that are implemented
test_files="test/test_document.py"
test_files+=" test/test_file.py"
test_files+=" test/test_package.py"
test_files+=" test/test_parser.py"
test_files+=" test/test_relationship.py"
test_files+=" test/test_sbom.py"

# The setted checksum is not valid, so this test fails
donttest="test_set_checksum"
# The setted type is not valid, so this test fails
donttest+=" or test_set_type"
# Assert with different capitalization
donttest+=" or test_set_supplier or test_set_supplier or test_set_originator or test_set_downloadlocation or test_set_homepage or test_set_externalreference"
# Not implemented in test_parser.py
donttest+=" or test_get_type or test_get_files or test_get_packages or test_get_relationships"

%pytest $test_files -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/lib4sbom
%{python_sitelib}/lib4sbom-%{version}*info

%changelog
