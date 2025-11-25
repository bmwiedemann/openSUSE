#
# spec file for package python-azure-ai-projects
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
Name:           python-azure-ai-projects
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure AI Projects Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_ai_projects/azure_ai_projects-%{version}.tar.gz
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Requires:       python-azure-ai-agents >= 1.0.0
Requires:       python-azure-storage-blob >= 12.15.0
Requires:       python-typing-extensions >= 4.12.2
Conflicts:      python-azure-sdk <= 2.0.0
Suggests:       python-mldesigner
BuildArch:      noarch
%python_subpackages

%description
The AI Projects client library (in preview) is part of the Azure AI Foundry
SDK, and provides easy access to resources in your Azure AI Foundry Project.

Use it to:

 * Create and run Agents using methods on the .agents client property.
 * Get an AzureOpenAI client using the .get_openai_client() client method.
 * Enumerate AI Models deployed to your Foundry Project using methods
   on the .deployments client property.
 * Enumerate connected Azure resources in your Foundry project using methods
   on the .connections client property.
 * Upload documents and create Datasets to reference them using methods on
   the .datasets client property.
 * Create and enumerate Search Indexes using methods on the .indexes client property.

The client library uses version v1 of the AI Foundry data plane REST APIs.

%prep
%setup -q -n azure_ai_projects-%{version}

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
%{python_sitelib}/azure/ai/projects
%{python_sitelib}/azure_ai_projects-*.dist-info

%changelog
