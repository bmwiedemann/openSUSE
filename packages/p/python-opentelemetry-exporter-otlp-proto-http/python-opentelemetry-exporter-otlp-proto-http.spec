#
# spec file for package python-opentelemetry-exporter-otlp-proto-http
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


Name:           python-opentelemetry-exporter-otlp-proto-http
Version:        1.25.0
Release:        0
Summary:        OpenTelemetry Collector Protobuf over HTTP Exporter
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-exporter-otlp-proto-http/opentelemetry_exporter_otlp_proto_http-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Deprecated >= 1.2.6}
BuildRequires:  %{python_module googleapis-common-protos >= 1.52}
BuildRequires:  %{python_module opentelemetry-api >= 1.15}
BuildRequires:  %{python_module opentelemetry-exporter-otlp-proto-common = %{version}}
BuildRequires:  %{python_module opentelemetry-proto = %{version}}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.23.0}
BuildRequires:  %{python_module opentelemetry-test-utils}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.7}
BuildRequires:  %{python_module responses >= 0.22.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Deprecated >= 1.2.6
Requires:       python-googleapis-common-protos >= 1.52
Requires:       python-opentelemetry-api >= 1.15
Requires:       python-opentelemetry-exporter-otlp-proto-common = %{version}
Requires:       python-opentelemetry-proto = %{version}
Requires:       python-opentelemetry-sdk >= 1.23.0
Requires:       python-requests >= 2.7
BuildArch:      noarch
%python_subpackages

%description
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over HTTP.

%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_http-%{version}

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
%dir %{python_sitelib}/opentelemetry/exporter/otlp/
%dir %{python_sitelib}/opentelemetry/exporter/otlp/proto
%{python_sitelib}/opentelemetry/exporter/otlp/proto/http
%{python_sitelib}/opentelemetry_exporter_otlp_proto_http-%{version}.dist-info

%changelog
