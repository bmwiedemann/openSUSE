#
# spec file for package python-xai-sdk
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


Name:           python-xai-sdk
Version:        1.17.0
Release:        0
Summary:        The official Python SDK for the xAI API
License:        Apache-2.0
URL:            https://github.com/xai-org/xai-sdk-python
Source0:        https://files.pythonhosted.org/packages/source/x/xai-sdk/xai_sdk-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-proto-dispatch-support-protobuf-7-via-v6-gencode.patch -- route protobuf >= 6 to the v6 gencode (forward-compatible; fixes import on protobuf 7)
Patch0:         0001-proto-dispatch-support-protobuf-7-via-v6-gencode.patch
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.8.6}
BuildRequires:  %{python_module googleapis-common-protos >= 1.65.0}
BuildRequires:  %{python_module grpcio >= 1.72.1}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.36.0}
BuildRequires:  %{python_module packaging >= 25.0}
BuildRequires:  %{python_module portpicker}
BuildRequires:  %{python_module protobuf >= 5.29.4}
BuildRequires:  %{python_module pydantic >= 2.5.3}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.31.0}
# /SECTION
Requires:       python-aiohttp >= 3.8.6
Requires:       python-googleapis-common-protos >= 1.65.0
Requires:       python-grpcio >= 1.72.1
Requires:       python-opentelemetry-sdk >= 1.36.0
Requires:       python-packaging >= 25.0
Requires:       python-protobuf >= 5.29.4
Requires:       python-pydantic >= 2.5.3
Requires:       python-requests >= 2.31.0
Recommends:     python-opentelemetry-exporter-otlp-proto-grpc >= 1.36.0
Recommends:     python-opentelemetry-exporter-otlp-proto-http >= 1.36.0
BuildArch:      noarch
%python_subpackages

%description
The official Python SDK for the xAI API. It provides synchronous and
asynchronous clients for xAI's gRPC API, covering chat completions (including
streaming, tool and function calling, and structured outputs), image
generation, embeddings and tokenization, file and collection management, batch
jobs, and deferred requests. Optional OpenTelemetry exporters allow tracing of
SDK calls.

%prep
%autosetup -p1 -n xai_sdk-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/xai_sdk
%{python_sitelib}/xai_sdk-%{version}.dist-info

%changelog
