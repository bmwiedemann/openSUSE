#
# spec file for package python-mistralai
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


Name:           python-mistralai
Version:        1.10.1
Release:        0
Summary:        Python Client SDK for the Mistral AI API
License:        Apache-2.0
URL:            https://github.com/mistralai/client-python
Source0:        https://files.pythonhosted.org/packages/source/m/mistralai/mistralai-%{version}.tar.gz
Source99:       python-mistralai.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module hatchling}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentelemetry-api
Requires:       python-opentelemetry-exporter-otlp-proto-http
Requires:       python-opentelemetry-sdk
Requires:       python-opentelemetry-semantic-conventions
Requires:       python-PyYAML >= 6.0.2
Requires:       python-eval-type-backport >= 0.2.0
Requires:       python-httpx >= 0.28.1
Requires:       python-invoke >= 2.2.0
Requires:       python-pydantic >= 2.10.3
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-typing-inspection >= 0.4.0
Suggests:       python-authlib >= 1.5.2
Suggests:       python-google-auth >= 2.27.0
Suggests:       python-griffe >= 1.7.3
Suggests:       python-mcp >= 1.0
Suggests:       python-requests >= 2.32.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module eval-type-backport >= 0.2.0}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module invoke >= 2.2.0}
BuildRequires:  %{python_module opentelemetry-api >= 1.33.1}
BuildRequires:  %{python_module opentelemetry-exporter-otlp-proto-http >= 1.37.0}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.33.1}
BuildRequires:  %{python_module opentelemetry-semantic-conventions >= 0.59b0}
BuildRequires:  %{python_module pydantic >= 2.10.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.2}
BuildRequires:  %{python_module typing-inspection >= 0.4.0}
# /SECTION
%python_subpackages

%description
# Mistral Python Client

Before you begin, you will need a Mistral AI API key.

Mistral AI API: Our Chat Completion and Embeddings APIs specification.
Create your account on [La Plateforme](https://console.mistral.ai) to
get access and read the [docs](https://docs.mistral.ai) to learn how to
use it.

%prep
%autosetup -p1 -n mistralai-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/mistralai
%{python_sitelib}/mistralai_gcp
%{python_sitelib}/mistralai_azure
%{python_sitelib}/mistralai-%{version}*-info

%changelog
