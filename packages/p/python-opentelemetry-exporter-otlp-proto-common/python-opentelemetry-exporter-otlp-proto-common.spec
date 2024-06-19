#
# spec file for package python-opentelemetry-exporter-otlp-proto-common
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
Name:           python-opentelemetry-exporter-otlp-proto-common
Version:        1.25.0
Release:        0
Summary:        OpenTelemetry Protobuf encoding
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-exporter-otlp-proto-common/opentelemetry_exporter_otlp_proto_common-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module opentelemetry-proto = %{version}}
BuildRequires:  %{python_module opentelemetry-sdk = %{version}}
BuildRequires:  %{python_module opentelemetry-test-utils}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-opentelemetry-proto = %{version}
BuildArch:      noarch
%python_subpackages

%description
This library is provided as a convenience to encode to Protobuf. Currently used by:

* opentelemetry-exporter-otlp-proto-grpc
* opentelemetry-exporter-otlp-proto-http

%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_common-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%dir %{python_sitelib}/opentelemetry
%dir %{python_sitelib}/opentelemetry/exporter
%dir %{python_sitelib}/opentelemetry/exporter/otlp
%dir %{python_sitelib}/opentelemetry/exporter/otlp/proto
%{python_sitelib}/opentelemetry/exporter/otlp/proto/common
%{python_sitelib}/opentelemetry_exporter_otlp_proto_common-%{version}.dist-info

%changelog
