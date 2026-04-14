#
# spec file for package python-langfuse
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
Name:           python-langfuse
Version:        4.2.0
Release:        0
Summary:        A client library for accessing langfuse
License:        MIT
URL:            https://github.com/langfuse/langfuse-python
Source:         https://files.pythonhosted.org/packages/source/l/langfuse/langfuse-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build >= 0.11.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backoff >= 1.10.0
Requires:       python-httpx >= 0.15.4
Requires:       python-opentelemetry-api >= 1.33.1
Requires:       python-opentelemetry-exporter-otlp-proto-http >= 1.33.1
Requires:       python-opentelemetry-sdk >= 1.33.1
Requires:       python-packaging >= 23.2
Requires:       python-pydantic >= 2
Requires:       python-wrapt >= 1.14
BuildArch:      noarch
%python_subpackages

%description
A client library for accessing langfuse, an open-source LLM engineering
platform that helps teams collaboratively debug, analyze, and iterate on their
LLM applications.

%prep
%autosetup -p1 -n langfuse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/langfuse
%{python_sitelib}/langfuse-%{version}.dist-info

%changelog
