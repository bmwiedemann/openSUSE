#
# spec file for package python-napalm-ansible
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-napalm-ansible
Version:        1.1.0
Release:        0
Summary:        Ansible module for device access using NAPALM
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/napalm-automation/napalm-ansible
Source:         https://github.com/napalm-automation/napalm-ansible/archive/%{version}.tar.gz#/napalm-ansible-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-napalm
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module napalm}
BuildRequires:  %{python_module pytest}
BuildRequires:  ansible
# /SECTION
%python_subpackages

%description
Collection of ansible modules that use napalm to retrieve data or modify
configuration on networking devices.

%prep
%setup -q -n napalm-ansible-%{version}
# Drop shebang
sed -i -e '/^#!\//, 1d' \
  napalm_ansible/modules/napalm_translate_yang.py \
  napalm_ansible/modules/napalm_diff_yang.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/napalm-ansible
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative napalm-ansible

%postun
%python_uninstall_alternative napalm-ansible

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.rst
%python_alternative %{_bindir}/napalm-ansible
%{python_sitelib}/*

%changelog
