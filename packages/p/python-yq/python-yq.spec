#
# spec file for package python-yq
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-yq
Version:        3.1.1
Release:        0
Summary:        Command-line YAML processor - jq wrapper for YAML documents
License:        Apache-2.0
URL:            https://github.com/kislyuk/yq
Source:         https://files.pythonhosted.org/packages/source/y/yq/yq-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jq
Requires:       python-PyYAML >= 5.3.1
Requires:       python-argcomplete >= 1.8.1
Requires:       python-setuptools
Requires:       python-toml >= 0.10.0
Requires:       python-xmltodict >= 0.11.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module argcomplete >= 1.8.1}
BuildRequires:  %{python_module toml >= 0.10.0}
BuildRequires:  %{python_module xmltodict >= 0.11.0}
BuildRequires:  jq
# /SECTION
%python_subpackages

%description
yq: Command-line YAML processor - jq wrapper for YAML documents

%prep
%autosetup -p1 -n yq-%{version}
sed -i "/setup_requires/d" setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/yq
%python_clone -a %{buildroot}%{_bindir}/xq
%python_clone -a %{buildroot}%{_bindir}/tomlq
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative yq
%python_install_alternative xq
%python_install_alternative tomlq

%postun
%python_uninstall_alternative yq
%python_uninstall_alternative xq
%python_uninstall_alternative tomlq

%check
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/test.py -v

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/yq
%python_alternative %{_bindir}/xq
%python_alternative %{_bindir}/tomlq
%{python_sitelib}/*

%changelog
