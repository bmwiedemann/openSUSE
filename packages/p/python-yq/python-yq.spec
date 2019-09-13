#
# spec file for package python-yq
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
Name:           python-yq
Version:        2.7.2
Release:        0
Summary:        Command-line YAML processor - jq wrapper for YAML documents
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kislyuk/yq
Source:         https://files.pythonhosted.org/packages/source/y/yq/yq-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jq
Requires:       python-PyYAML >= 3.11
Requires:       python-setuptools
Requires:       python-toml >= 0.9.4
Requires:       python-xmltodict >= 0.11.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module toml >= 0.9.4}
BuildRequires:  %{python_module xmltodict >= 0.11.0}
BuildRequires:  jq
# /SECTION
%python_subpackages

%description
yq: Command-line YAML processor - jq wrapper for YAML documents

%prep
%setup -q -n yq-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/yq
%python_clone -a %{buildroot}%{_bindir}/xq
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative yq
%python_install_alternative xq

%postun
%python_uninstall_alternative yq
%python_uninstall_alternative xq

%check
export LANG=en_US.UTF-8
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 test/test.py -v

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/yq
%python_alternative %{_bindir}/xq
%{python_sitelib}/*

%changelog
