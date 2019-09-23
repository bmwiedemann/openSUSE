#
# spec file for package python-azure-servicebus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-azure-servicebus
Version:        0.50.0
Release:        0
Summary:        Microsoft Azure Service Bus Runtime Client Library
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-servicebus/azure-servicebus-%{version}.zip
Source1:        LICENSE.txt
Patch1:         as_drop-compatible-releases-operator.patch
Patch2:         as_drop-extras-require.patch
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-common >= 1.1.5
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-requests
Requires:       python-uamqp >= 1.1.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Service Bus Runtime Client Library.

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

%prep
%setup -q -n azure-servicebus-%{version}
%patch1 -p1
%patch2 -p1

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-servicebus-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{python_sitelib}/azure/servicebus
%{python_sitelib}/azure_servicebus-*.egg-info

%changelog
