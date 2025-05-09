#
# spec file for package python-azure-ai-formrecognizer
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-azure-ai-formrecognizer
Version:        3.3.3
Release:        0
Summary:        Microsoft Azure Form Recognizer Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-formrecognizer/azure-ai-formrecognizer-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-msrest >= 0.6.21
Requires:       python-typing_extensions >= 4.0.1
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-core >= 1.23.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-ai-formrecognizer < 3.3.2
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure Cognitive Services Form Recognizer is a cloud service that uses machine learning
to recognize text and table data from form documents. It includes the following main
functionalities:

 * Custom models - Recognize field values and table data from forms. These models are
   trained with your own data, so they're tailored to your forms.
 * Content API - Recognize text and table structures, along with their bounding box coordinates,
   from documents. Corresponds to the REST service's Layout API.
 * Prebuilt receipt model - Recognize data from USA sales receipts using a prebuilt model.

%prep
%setup -q -n azure-ai-formrecognizer-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-formrecognizer-%{version}
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
%license LICENSE.txt
%{python_sitelib}/azure/ai/formrecognizer
%{python_sitelib}/azure_ai_formrecognizer-*.dist-info

%changelog
