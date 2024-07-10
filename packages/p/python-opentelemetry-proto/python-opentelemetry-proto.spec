#
# spec file for package python-opentelemetry-proto
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
Name:           python-opentelemetry-proto
Version:        1.25.0
Release:        0
Summary:        OpenTelemetry Python Proto
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-proto/opentelemetry_proto-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module protobuf >= 3.19}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-protobuf >= 3.19
BuildArch:      noarch
%python_subpackages

%description
This library contains the generated code for OpenTelemetry protobuf data model.
The code in the current package was generated using the v0.17.0 release_ of
opentelemetry-proto.

%prep
%autosetup -p1 -n opentelemetry_proto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%dir %{python_sitelib}/opentelemetry
%{python_sitelib}/opentelemetry/proto
%{python_sitelib}/opentelemetry_proto-%{version}.dist-info

%changelog
