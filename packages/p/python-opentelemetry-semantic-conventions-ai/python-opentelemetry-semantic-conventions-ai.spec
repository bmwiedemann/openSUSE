#
# spec file for package python-opentelemetry-semantic-conventions-ai
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
# published by the Open Source Initiative.//
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-opentelemetry-semantic-conventions-ai
Version:        0.5.1
Release:        0
Summary:        OpenTelemetry Semantic Conventions Extension for Large Language Models
License:        Apache-2.0
URL:            https://github.com/traceloop/openllmetry
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry_semantic_conventions_ai/opentelemetry_semantic_conventions_ai-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.38.0}
BuildRequires:  %{python_module opentelemetry-semantic-conventions >= 0.59b0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentelemetry-sdk >= 1.38.0
Requires:       python-opentelemetry-semantic-conventions >= 0.59b0
BuildArch:      noarch
%python_subpackages

%description
An extension of the standard OpenTelemetry Semantic Conventions for
generative-AI applications. It defines additional span attributes,
metrics and enums useful for debugging and monitoring prompts,
completions and token usage of large language models.

%prep
%autosetup -p1 -n opentelemetry_semantic_conventions_ai-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/opentelemetry/semconv_ai
%{python_sitelib}/opentelemetry_semantic_conventions_ai-%{version}.dist-info

%changelog
