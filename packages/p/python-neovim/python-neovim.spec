#
# spec file for package python-neovim
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


%define modname pynvim
%{?sle15_python_module_pythons}
Name:           python-neovim
Version:        0.5.2
Release:        0
Summary:        Python client to Neovim
License:        Apache-2.0
Group:          Productivity/Text/Editors
URL:            https://github.com/neovim/pynvim
Source:         https://github.com/neovim/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  neovim >= 0.9.0
BuildRequires:  python-rpm-macros
Requires:       neovim
Requires:       python-greenlet
Requires:       python-msgpack
Requires:       python-typing_extensions
Provides:       python-nvim
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module msgpack}
# /SECTION
%python_subpackages

%description
Library for scripting Nvim processes through its msgpack-rpc API.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/neovim
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
