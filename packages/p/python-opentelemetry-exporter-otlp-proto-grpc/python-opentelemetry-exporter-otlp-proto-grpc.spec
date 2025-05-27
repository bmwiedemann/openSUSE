#
# spec file for package python-opentelemetry-exporter-otlp-proto-grpc
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
Name:           python-opentelemetry-exporter-otlp-proto-grpc
Version:        1.33.1
Release:        0
Summary:        OpenTelemetry Collector Protobuf over gRPC Exporter
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-exporter-otlp-proto-grpc/opentelemetry_exporter_otlp_proto_grpc-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Deprecated >= 1.2.6}
BuildRequires:  %{python_module googleapis-common-protos >= 1.52}
BuildRequires:  %{python_module grpcio >= 1.0.0}
BuildRequires:  %{python_module opentelemetry-api >= 1.15}
BuildRequires:  %{python_module opentelemetry-exporter-otlp-proto-common = %{version}}
BuildRequires:  %{python_module opentelemetry-proto = %{version}}
BuildRequires:  %{python_module opentelemetry-sdk >= %{version}}
BuildRequires:  %{python_module opentelemetry-test-utils}
BuildRequires:  %{python_module pytest-grpc}
BuildRequires:  %{python_module requests}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Deprecated >= 1.2.6
Requires:       python-googleapis-common-protos
Requires:       python-grpcio >= 1.0.0
Requires:       python-opentelemetry-api
Requires:       python-opentelemetry-exporter-otlp-proto-common = %{version}
Requires:       python-opentelemetry-proto = %{version}
Requires:       python-opentelemetry-sdk
BuildArch:      noarch
%python_subpackages

%description
OpenTelemetry Collector Protobuf over gRPC Exporter

This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over gRPC.

%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_grpc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rvf tests/performance
%pytest

%files %{python_files}
%dir %{python_sitelib}/opentelemetry
%dir %{python_sitelib}/opentelemetry/exporter
%dir %{python_sitelib}/opentelemetry/exporter/otlp
%dir %{python_sitelib}/opentelemetry/exporter/otlp/proto
%{python_sitelib}/opentelemetry/exporter/otlp/proto/grpc
%{python_sitelib}/opentelemetry_exporter_otlp_proto_grpc-%{version}.dist-info

%changelog
