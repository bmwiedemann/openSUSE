#
# spec file for package python-moksha-hub
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
Name:           python-moksha-hub
Version:        1.5.17
Release:        0
Summary:        Hub components for Moksha
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://mokshaproject.net
Source:         https://files.pythonhosted.org/packages/source/m/moksha.hub/moksha.hub-%{version}.tar.gz
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module moksha-common >= 1.0.6}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module txWS}
BuildRequires:  %{python_module txZMQ}
BuildRequires:  %{python_module websocket-client}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted
Requires:       python-moksha-common >= 1.0.6
Requires:       python-pyzmq
Requires:       python-txWS
Requires:       python-txZMQ
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Hub components for Moksha.

%prep
%setup -q -n moksha.hub-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/moksha-hub
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative moksha-hub

%postun
%python_uninstall_alternative moksha-hub

%files %{python_files}
%license COPYING
%doc AUTHORS README
%python_alternative %{_bindir}/moksha-hub
%{python_sitelib}/*

%changelog
