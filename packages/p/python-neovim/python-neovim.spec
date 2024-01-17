#
# spec file for package python-neovim
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


%define modname pynvim
Name:           python-neovim
Version:        0.5.0
Release:        0
Summary:        Python client to Neovim
License:        Apache-2.0
Group:          Productivity/Text/Editors
URL:            https://github.com/neovim/pynvim
Source:         https://github.com/neovim/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module greenlet}
BuildRequires:  neovim
# /SECTION
Requires:       neovim >= 0.9.0
Requires:       %{python_module greenlet}
Requires:       %{python_module msgpack}
Provides:       python-nvim
BuildArch:      noarch
%python_subpackages

%description
Library for scripting Nvim processes through its msgpack-rpc API.

%prep
%autosetup -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/neovim/
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-*.egg-info/

%changelog
