#
# spec file for package python-opentelemetry-exporter-gcp-monitoring
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
Name:           python-opentelemetry-exporter-gcp-monitoring
Version:        1.11.0~a0
Release:        0
Summary:        Google Cloud Monitoring exporter for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-python/tree/main/opentelemetry-exporter-gcp-monitoring
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-exporter-gcp-monitoring/opentelemetry_exporter_gcp_monitoring-1.11.0a0.tar.gz
# PATCH-FIX-UPSTREAM fix-syrupy-api.patch - Fix compatibility with syrupy 5.x API
Patch0:         fix-syrupy-api.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module syrupy}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Core dependencies
BuildRequires:  %{python_module google-cloud-monitoring >= 2.0}
BuildRequires:  %{python_module opentelemetry-api >= 1.30}
BuildRequires:  %{python_module opentelemetry-resourcedetector-gcp >= 1.5.0~dev0}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.30}
BuildRequires:  fdupes
BuildArch:      noarch
# Runtime dependencies
Requires:       python-google-cloud-monitoring >= 2.0
Requires:       python-opentelemetry-api >= 1.30
Requires:       python-opentelemetry-resourcedetector-gcp >= 1.5.0~dev0
Requires:       python-opentelemetry-sdk >= 1.30

%python_subpackages

%description
This library provides support for exporting metrics to Google Cloud Monitoring.

%prep
%autosetup -p1 -n opentelemetry_exporter_gcp_monitoring-1.11.0a0

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm %{buildroot}%{$python_sitelib}/opentelemetry/py.typed

%check
%pytest

%files %{python_files}
%dir %{python_sitelib}/opentelemetry/exporter
%{python_sitelib}/opentelemetry/exporter/cloud_monitoring
%{python_sitelib}/opentelemetry_exporter_gcp_monitoring-1.11.0a0.dist-info

%changelog
