#
# spec file for package python-neovim
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.6.0
Release:        0
Summary:        Python client to Neovim
License:        Apache-2.0
Group:          Productivity/Text/Editors
URL:            https://github.com/neovim/pynvim
Source:         %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module msgpack}
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
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-nvim
BuildArch:      noarch

%python_subpackages

%description
Library for scripting Nvim processes through its msgpack-rpc API.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{modname}-python
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative %{modname}-python

%postun
%python_uninstall_alternative %{modname}-python

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/%{modname}-python
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info
%{python_sitelib}/neovim

%changelog
