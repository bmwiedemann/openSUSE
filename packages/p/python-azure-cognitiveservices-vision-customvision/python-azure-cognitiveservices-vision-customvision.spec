#
# spec file for package python-azure-cognitiveservices-vision-customvision
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
Name:           python-azure-cognitiveservices-vision-customvision
Version:        3.1.1
Release:        0
Summary:        Microsoft Azure Custom Vision Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_cognitiveservices_vision_customvision/azure_cognitiveservices_vision_customvision-%{version}.tar.gz
BuildRequires:  %{python_module azure-cognitiveservices-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-cognitiveservices-vision-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-cognitiveservices-nspkg >= 3.0.0
Requires:       python-azure-cognitiveservices-vision-nspkg >= 3.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.21
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-mgmt-core >= 1.1 with python-azure-mgmt-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-cognitiveservices-vision-customvision <= 3.1.0
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Custom Vision Client Library.

This package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.

%prep
%setup -q -n azure_cognitiveservices_vision_customvision-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/vision/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/vision/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/cognitiveservices/vision/customvision
%{python_sitelib}/azure_cognitiveservices_vision_customvision-*.dist-info

%changelog
