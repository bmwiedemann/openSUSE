#
# spec file for package python-opentelemetry-test-utils
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
Name:           python-opentelemetry-test-utils
Version:        0.50b0
Release:        0
Summary:        Test utilities for OpenTelemetry unit tests
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-test-utils/opentelemetry_test_utils-%{version}.tar.gz
BuildRequires:  %{python_module asgiref >= 3.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-api == 1.29.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asgiref
Requires:       python-opentelemetry-api == 1.29.0
BuildArch:      noarch
%python_subpackages

%description
OpenTelemetry Test Utilities

This package provides internal testing utilities for the OpenTelemetry Python
project and provides no stability or quality guarantees.  Please do not use it
for anything other than writing or running tests for the OpenTelemetry Python
project (github.com/open-telemetry/opentelemetry-python).

%prep
%autosetup -p1 -n opentelemetry_test_utils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%dir %{python_sitelib}/opentelemetry
%{python_sitelib}/opentelemetry/test
%{python_sitelib}/opentelemetry_test_utils-%{version}.dist-info

%changelog
