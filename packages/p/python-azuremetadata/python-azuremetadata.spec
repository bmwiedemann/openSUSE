#
# spec file for package python-azuremetadata
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
%define upstream_name azuremetadata
Name:           python-azuremetadata
Version:        5.1.5
Release:        0
Summary:        Python module for collecting instance metadata from Azure
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/SUSE-Enceladus/azuremetadata
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     util-linux
Conflicts:      regionServiceClientConfigAzure <= 0.0.4
Conflicts:      regionServiceClientConfigSAPAzure <= 1.0.1
# Packaged renamed in SLE15
Provides:       azuremetadata = %{version}
Obsoletes:      azuremetadata < 5.0.0
Provides:       python-azuremetadata = %{version}
Obsoletes:      python3-azuremetadata < %{version}
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
A module for collecting instance metadata from Microsoft Azure.

%prep
%autosetup -p1 -n python3-%{upstream_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/azuremetadata.1 %{buildroot}/%{_mandir}/man1
%python_clone -a %{buildroot}%{_bindir}/%{upstream_name}
%python_clone -a %{buildroot}%{_mandir}/man1/azuremetadata.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative azuremetadata azuremetadata.1%{?ext_man}

%postun
%python_uninstall_alternative azuremetadata

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/%{upstream_name}
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}*-info
%python_alternative %{_mandir}/man1/%{upstream_name}.1%{?ext_man}

%changelog
