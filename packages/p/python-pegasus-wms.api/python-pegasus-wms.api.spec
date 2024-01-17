#
# spec file for package python-pegasus-wms.api
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pegasus-wms.api
Version:        5.0.3
Release:        0
Summary:        Pegasus Workflow Management System Python API
License:        Apache-2.0
URL:            http://pegasus.isi.edu
Source0:        pegasus-wms.api-gh-%{version}.tar.xz
Source1:        pegasus-schema-yaml-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pegasus-wms.common < 5.1}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pegasus-wms.common < 5.1
BuildArch:      noarch
%python_subpackages

%description
This package contains the Python APIs for Pegasus WMS, including:

The DAX API (Versions 2 and 3)
The PDAX API (Version 2)
The monitoring API
The Stampede database API
The Pegasus statistics API
The Pegasus plots API
Misc. Pegasus utilities
The pegasus service, including the ensemble manager and dashboard

%prep
%setup -q -n pegasus-wms.api-gh-%{version} -b1
# replace ties to global git repository with our limited package subset
sed -i 's|version=read_version(),|version="%{version}",|' setup.py
# replaces paths in two lines
sed -i test/api/conftest.py \
  -e 's|"packages/pegasus-api/test/api"|"pegasus-wms.api-gh-%{version}/test/api"|' \
  -e 's|"share/pegasus/schema/yaml"|"pegasus-schema-yaml-%{version}"|'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# same output but different order in 'uses' field
donttest="test_workflow_to_subworkflow_conversion_in_write"
%pytest -v -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/Pegasus
%{python_sitelib}/Pegasus/api
%{python_sitelib}/pegasus_wms.api-%{version}*-info

%changelog
