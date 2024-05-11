#
# spec file for package python-azure-messaging-nspkg
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
Name:           python-azure-messaging-nspkg
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Messaging Namespace Package
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-messaging-nspkg/azure-messaging-nspkg-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-nspkg >= 3.0.0
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-messaging-nspkg <= 1.0.0
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Messaging namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure.messaging namespace.

%prep
%setup -q -n azure-messaging-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-messaging-nspkg-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand mkdir -p %{buildroot}%{$python_sitelib}/azure/messaging

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/messaging
%{python_sitelib}/azure_messaging_nspkg-*.dist-info

%changelog
