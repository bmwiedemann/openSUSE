#
# spec file for package python-azure-cognitiveservices-inkrecognizer
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
Name:           python-azure-cognitiveservices-inkrecognizer
Version:        1.0.0b1
Release:        0
Summary:        Microsoft Azure Cognitive Services Ink Recognizer Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-cognitiveservices-inkrecognizer/azure-cognitiveservices-inkrecognizer-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-cognitiveservices-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-cognitiveservices-nspkg >= 3.0.0
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-core >= 1.0.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-cognitiveservices-inkrecognizer <= 1.0.0b1
%endif
BuildArch:      noarch
%python_subpackages

%description
Azure Ink Recognizer SDK is an SDK for developers to work with Azure Ink Recognizer Service.
The service recognize a collection of ink strokes and return a tree hierarchy of the recognized units,
such as lines, words, shapes, as well as the handwriting recognition result of the words.

Features:

* Connect to Azure Ink Recognizer Service
* Convert collections of ink strokes into HTTP requests
* Parse HTTP response into ink recognition units

%prep
%setup -q -n azure-cognitiveservices-inkrecognizer-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cognitiveservices-inkrecognizer-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc HISTORY.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/cognitiveservices/inkrecognizer
%{python_sitelib}/azure_cognitiveservices_inkrecognizer-*.dist-info

%changelog
