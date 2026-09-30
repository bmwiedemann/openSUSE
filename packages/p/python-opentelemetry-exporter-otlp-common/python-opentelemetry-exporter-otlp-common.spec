#
# spec file for package python-opentelemetry-exporter-otlp-common
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-opentelemetry-exporter-otlp-common
Version:        0.66b0
Release:        0
Summary:        OpenTelemetry OTLP HTTP export utilities
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-common
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-exporter-otlp-common/opentelemetry_exporter_otlp_common-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module opentelemetry-sdk = 1.45.0}
BuildRequires:  %{python_module opentelemetry-exporter-http-transport}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module iniconfig}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module mocket}
# /SECTION
BuildRequires:  fdupes
Requires:       python-opentelemetry-sdk = 1.45.0
Recommends:     python-opentelemetry-exporter-http-transport
BuildArch:      noarch
%python_subpackages

%description
OpenTelemetry OTLP export utilities.

This package is intended to be used by OpenTelemetry signal exporters (traces, metrics,
logs) that send telemetry with OTLP. Currently, all functionality in this package
is marked as internal and is not intended for use directly by application developers.

%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_common-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/opentelemetry/exporter
%dir %{python_sitelib}/opentelemetry/exporter/otlp
%{python_sitelib}/opentelemetry/exporter/otlp/common
%{python_sitelib}/opentelemetry_exporter_otlp_common-%{version}.dist-info

%changelog
