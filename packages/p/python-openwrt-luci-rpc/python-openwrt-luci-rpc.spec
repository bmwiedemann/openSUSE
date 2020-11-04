#
# spec file for package python-openwrt-luci-rpc
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
Name:           python-openwrt-luci-rpc
Version:        1.1.3
Release:        0
Summary:        Module for interacting with OpenWrt Luci RPC interface
License:        Apache-2.0
URL:            https://github.com/fbradyirl/openwrt-luci-rpc
Source:         https://files.pythonhosted.org/packages/source/o/openwrt-luci-rpc/openwrt-luci-rpc-%{version}.tar.gz
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module packaging >= 19.1}
BuildRequires:  %{python_module requests >= 2.21}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 6.0
Requires:       python-packaging >= 19.1
Requires:       python-requests >= 2.21
BuildArch:      noarch
%python_subpackages

%description
Module for interacting with OpenWrt Luci RPC interface. You need to have 'luci-mod-rpc'
installed on your openwrt based router.

-  Allows you to use the Luci RPC interface to fetch connected devices
   on your OpenWrt based router.
-  Supports 15.X & 17.X & 18.X or newer releases of OpenWrt.

https://openwrt-luci-rpc.readthedocs.io

%prep
%setup -q -n openwrt-luci-rpc-%{version}
# do not harcode versions
sed -i -e 's:==:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%{python_sitelib}/openwrt_luci_rpc*

%changelog
