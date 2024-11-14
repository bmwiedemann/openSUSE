#
# spec file for package python-azure-servicebus
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
Name:           python-azure-servicebus
Version:        7.13.0
Release:        0
Summary:        Microsoft Azure Service Bus Runtime Client Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_servicebus/azure_servicebus-%{version}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.0
Requires:       python-typing_extensions >= 4.6.0
Requires:       (python-azure-core >= 1.28.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-servicebus < 7.11.4
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Service Bus Client Library.
This package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.

Microsoft Azure Service Bus supports a set of cloud-based, message-oriented
middleware technologies including reliable message queuing and durable
publish/subscribe messaging.

%prep
%setup -q -n azure_servicebus-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/servicebus
%{python_sitelib}/azure_servicebus-*.dist-info

%changelog
