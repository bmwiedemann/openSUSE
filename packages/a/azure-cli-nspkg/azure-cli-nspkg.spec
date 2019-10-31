#
# spec file for package azure-cli-nspkg
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


Name:           azure-cli-nspkg
Version:        3.0.4
Release:        0
Summary:        Microsoft Azure CLI Namespace Package
License:        MIT
Group:          System/Management
Url:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-nspkg/azure-cli-nspkg-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  fdupes
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       python3-azure-nspkg >= 3.0.0
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI Namespace Package

This is the Microsoft Azure CLI namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure cli namespaces.

%prep
%setup -q -n azure-cli-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-nspkg-%{version}
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib}
%fdupes %{buildroot}%{python3_sitelib}

%files
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/azure/cli
%{python3_sitelib}/azure_cli_nspkg-*.egg-info

%changelog
