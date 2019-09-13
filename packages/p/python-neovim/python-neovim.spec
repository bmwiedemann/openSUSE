#
# spec file for package python-neovim
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


%define modname pynvim
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-neovim
Version:        0.3.2
Release:        0
Summary:        Python client to Neovim
License:        Apache-2.0
Group:          Productivity/Text/Editors
URL:            https://github.com/neovim/pynvim
Source:         https://github.com/neovim/pynvim/archive/%{version}/pynvim-%{version}.tar.gz
BuildRequires:  fdupes
%if 0%{?rhel} >= 7
BuildRequires:  python34-pytest
BuildRequires:  python34-setuptools
%else
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%endif
BuildRequires:  python-rpm-macros
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
Requires:       neovim >= 0.1.6
Requires:       python-greenlet
Requires:       python-msgpack-python
BuildArch:      noarch
%if "%{python_flavor}" == "python2"
Requires:       python-trollius
%endif
Provides:       python-nvim
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

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/neovim/
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-*.egg-info/

%changelog
