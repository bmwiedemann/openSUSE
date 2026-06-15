#
# spec file for package python-google-adk
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
Name:           python-google-adk
Version:        1.29.0
Release:        0
Summary:        An open-source, code-first Python toolkit for building AI agents
License:        Apache-2.0
URL:            https://github.com/google/adk-python
Source:         https://github.com/google/adk-python/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Core dependencies
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module Authlib}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module google-api-python-client}
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module google-cloud-aiplatform}
BuildRequires:  %{python_module google-cloud-bigquery-storage}
BuildRequires:  %{python_module google-cloud-bigquery}
BuildRequires:  %{python_module google-cloud-bigtable}
BuildRequires:  %{python_module google-cloud-dataplex}
BuildRequires:  %{python_module google-cloud-discoveryengine}
BuildRequires:  %{python_module google-cloud-pubsub}
BuildRequires:  %{python_module google-cloud-secret-manager}
BuildRequires:  %{python_module google-cloud-spanner}
BuildRequires:  %{python_module google-cloud-speech}
BuildRequires:  %{python_module google-cloud-storage}
BuildRequires:  %{python_module google-genai}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mcp}
BuildRequires:  %{python_module opentelemetry-api}
BuildRequires:  %{python_module opentelemetry-exporter-gcp-logging}
BuildRequires:  %{python_module opentelemetry-exporter-gcp-monitoring}
BuildRequires:  %{python_module opentelemetry-exporter-gcp-trace}
BuildRequires:  %{python_module opentelemetry-exporter-otlp-proto-http}
BuildRequires:  %{python_module opentelemetry-resourcedetector-gcp}
BuildRequires:  %{python_module opentelemetry-sdk}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sqlalchemy-spanner}
BuildRequires:  %{python_module sqlalchemy}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module tenacity}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module watchdog}
BuildRequires:  %{python_module websockets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# Runtime dependencies
Requires:       python-PyYAML
Requires:       python-aiosqlite
Requires:       python-anyio
Requires:       python-click
Requires:       python-fastapi
Requires:       python-google-api-python-client
Requires:       python-google-auth
Requires:       python-google-cloud-aiplatform
Requires:       python-google-cloud-bigquery
Requires:       python-google-cloud-bigquery-storage
Requires:       python-google-cloud-bigtable
Requires:       python-google-cloud-dataplex
Requires:       python-google-cloud-discoveryengine
Requires:       python-google-cloud-pubsub
Requires:       python-google-cloud-secret-manager
Requires:       python-google-cloud-spanner
Requires:       python-google-cloud-speech
Requires:       python-google-cloud-storage
Requires:       python-google-genai
Requires:       python-graphviz
Requires:       python-httpx
Requires:       python-jsonschema
Requires:       python-mcp
Requires:       python-opentelemetry-api
Requires:       python-opentelemetry-exporter-gcp-logging
Requires:       python-opentelemetry-exporter-gcp-monitoring
Requires:       python-opentelemetry-exporter-gcp-trace
Requires:       python-opentelemetry-exporter-otlp-proto-http
Requires:       python-opentelemetry-resourcedetector-gcp
Requires:       python-opentelemetry-sdk
Requires:       python-arrow
Requires:       python-pydantic
Requires:       python-python-dateutil
Requires:       python-python-dotenv
Requires:       python-requests
Requires:       python-sqlalchemy
Requires:       python-sqlalchemy-spanner
Requires:       python-starlette
Requires:       python-tenacity
Requires:       python-typing-extensions
Requires:       python-tzlocal
Requires:       python-uvicorn
Requires:       python-watchdog
Requires:       python-websockets

%python_subpackages

%description
An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

%prep
%autosetup -p1 -n adk-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/adk
%python_expand echo 'import os; os.environ.setdefault("ADK_SUPPRESS_EXPERIMENTAL_FEATURE_WARNINGS", "1")' > %{buildroot}%{$python_sitelib}/adk-suppress-warnings.pth
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative adk

%postun
%python_uninstall_alternative adk

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/adk
%{python_sitelib}/google/adk
%{python_sitelib}/google_adk-%{version}.dist-info
%{python_sitelib}/adk-suppress-warnings.pth

%changelog
