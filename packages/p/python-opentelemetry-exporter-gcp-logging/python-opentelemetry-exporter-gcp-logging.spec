#
# spec file for package python-opentelemetry-exporter-gcp-logging
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
Name:           python-opentelemetry-exporter-gcp-logging
Version:        1.12.0
Release:        0
Summary:        Google Cloud Logging exporter for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-python
# using the source for multiple python packages, weeding out the different package like cloud_logging 
# for different python version would make the spec file look garbage
Source:         https://github.com/GoogleCloudPlatform/opentelemetry-operations-python/archive/refs/tags/v%{version}.tar.gz#/opentelemetry_exporter_gcp_logging-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Core dependencies
BuildRequires:  %{python_module google-cloud-logging >= 3.0}
BuildRequires:  %{python_module opentelemetry-api >= 1.35.0}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.35.0}
BuildRequires:  %{python_module opentelemetry-resourcedetector-gcp >= 1.5.0~dev0}
BuildRequires:  fdupes
BuildArch:      noarch
# Runtime dependencies
Requires:       python-google-cloud-logging >= 3.0
Requires:       python-opentelemetry-api >= 1.35.0
Requires:       python-opentelemetry-resourcedetector-gcp >= 1.5.0~dev0
Requires:       python-opentelemetry-sdk >= 1.35.0

%python_subpackages

%description
Google Cloud Logging exporter for OpenTelemetry.

%prep
%autosetup -p1 -n opentelemetry-operations-python-%{version}/opentelemetry-exporter-gcp-logging

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%dir %{python_sitelib}/opentelemetry
%dir %{python_sitelib}/opentelemetry/exporter
%{python_sitelib}/opentelemetry/exporter/cloud_logging
%{python_sitelib}/opentelemetry_exporter_gcp_logging-*.dist-info

%changelog
