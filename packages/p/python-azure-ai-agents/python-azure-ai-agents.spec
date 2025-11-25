#
# spec file for package python-azure-ai-agents
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-azure-ai-agents
Version:        1.1.0
Release:        0
Summary:        Microsoft Corporation Azure AI Agents Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_ai_agents/azure_ai_agents-%{version}.tar.gz
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Requires:       python-typing-extensions >= 4.6.0
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Use the AI Agents client library to:

 * Develop Agents using the Azure AI Agents Service, leveraging an extensive ecosystem
   of models, tools, and capabilities from OpenAI, Microsoft, and other LLM providers.
   The Azure AI Agents Service enables the building of Agents for a wide range of
   generative AI use cases.
 * Note: While this package can be used independently, we recommend using the Azure AI
   Projects client library (azure-ai-projects) for an enhanced experience. The Projects
   library provides simplified access to advanced functionality, such as creating and
   managing agents, enumerating AI models, working with datasets and managing search
   indexes, evaluating generative AI performance, and enabling OpenTelemetry tracing.

%prep
%setup -q -n azure_ai_agents-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/ai/agents
%{python_sitelib}/azure_ai_agents-*.dist-info

%changelog
