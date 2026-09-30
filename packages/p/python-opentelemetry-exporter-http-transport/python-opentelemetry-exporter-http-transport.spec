#
# spec file for package python-opentelemetry-exporter-http-transport
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


Name:           python-opentelemetry-exporter-http-transport
Version:        0.66b0
Release:        0
Summary:        OpenTelemetry Exporters HTTP transport
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-http-transport
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-exporter-http-transport/opentelemetry_exporter_http_transport-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module opentelemetry-api >= 1.15}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module mocket}
BuildRequires:  %{python_module iniconfig}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module urllib3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-opentelemetry-api >= 1.15
Suggests:       python-urllib3 >= 1.26
Suggests:       python-requests >= 2.25
BuildArch:      noarch
%python_subpackages

%description
This package provides shared HTTP transport abstractions used by OpenTelemetry exporters.

%prep
%autosetup -p1 -n opentelemetry_exporter_http_transport-%{version}

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
%dir %{python_sitelib}/opentelemetry/exporter/http
%{python_sitelib}/opentelemetry/exporter/http/transport
%{python_sitelib}/opentelemetry_exporter_http_transport-%{version}.dist-info

%changelog
