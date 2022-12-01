#
# spec file for package python-azure-ai-ml
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-ai-ml
Version:        1.1.2
Release:        0
Summary:        Microsoft Azure Machine Learning Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-ml/azure-ai-ml-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module PyYAML >= 5.1.0}
BuildRequires:  %{python_module applicationinsights}
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-common >= 1.1}
BuildRequires:  %{python_module azure-core >= 1.8.0}
BuildRequires:  %{python_module azure-identity}
BuildRequires:  %{python_module azure-mgmt-core >= 1.3.0}
BuildRequires:  %{python_module azure-storage-blob >= 12.10.0}
BuildRequires:  %{python_module azure-storage-file-datalake}
BuildRequires:  %{python_module azure-storage-file-share}
BuildRequires:  %{python_module colorama < 0.5.0}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module jsonschema >= 4.0.0}
BuildRequires:  %{python_module marshmallow >= 3.5}
BuildRequires:  %{python_module msrest >= 0.6.18}
BuildRequires:  %{python_module opencensus-ext-azure < 2.0.0}
BuildRequires:  %{python_module pathspec >= 0.9.0}
BuildRequires:  %{python_module pydash}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module strictyaml < 2.0.0}
BuildRequires:  %{python_module tqdm < 5.0.0}
BuildRequires:  %{python_module typing-extensions >= 4.0.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-PyJWT < 3.0.0
Requires:       python-PyYAML >= 5.1.0
Requires:       python-applicationinsights <= 0.11.10
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-azure-common >= 1.1
Requires:       python-azure-core >= 1.8.0
Requires:       python-azure-identity
Requires:       python-azure-mgmt-core >= 1.3.0
Requires:       python-azure-storage-blob >= 12.10.0
Requires:       python-azure-storage-file-datalake
Requires:       python-azure-storage-file-share
Requires:       python-colorama
Requires:       python-docker
Requires:       python-isodate
Requires:       python-jsonschema >= 4.0.0
Requires:       python-marshmallow >= 3.5
Requires:       python-msrest >= 0.6.18
Requires:       python-pathspec >= 0.9.0
Requires:       python-pydash
Requires:       python-strictyaml
Requires:       python-tqdm
Requires:       python-typing-extensions >= 4.0.1
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Conflicts:      python-azure-sdk <= 2.0.0
Suggests:       python-mldesigner
BuildArch:      noarch
%python_subpackages

%description
We are excited to introduce the public preview of Azure Machine Learning Python
SDK v2. The Python SDK v2 introduces new SDK capabilities like standalone local
jobs, reusable components for pipelines and managed online/batch inferencing.
Python SDK v2 allows you to move from simple to complex tasks easily and
incrementally. This is enabled by using a common object model which brings
concept reuse and consistency of actions across various tasks. The SDK v2 shares
its foundation with the CLI v2 which is currently in also in public preview.

This package has been tested with Python 3.6, 3.7, 3.8, 3.9 and 3.10.

%prep
%setup -q -n azure-ai-ml-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-ml-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/ai/ml
%{python_sitelib}/azure_ai_ml-*.egg-info

%changelog
