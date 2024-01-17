#
# spec file for package python-magic-wormhole-transit-relay
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-magic-wormhole-transit-relay
Version:        0.2.1
Release:        0
Summary:        Transit Relay server for Magic-Wormhole
License:        MIT
URL:            https://github.com/warner/magic-wormhole-transit-relay
Source:         https://files.pythonhosted.org/packages/source/m/magic-wormhole-transit-relay/magic-wormhole-transit-relay-%{version}.tar.gz
# https://github.com/magic-wormhole/magic-wormhole/issues/439
Patch0:         python-magic-wormhole-transit-relay-no-mock.patch
BuildRequires:  %{python_module Twisted >= 17.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 17.5.0
BuildArch:      noarch
%python_subpackages

%description
Transit Relay server for Magic-Wormhole

%prep
%autosetup -p1 -n magic-wormhole-transit-relay-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src/wormhole_transit_relay/test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/wormhole_transit_relay
%{python_sitelib}/magic_wormhole_transit_relay-%{version}*-info
%{python_sitelib}/twisted/plugins/magic_wormhole_transit_relay.py
%pycache_only %{python_sitelib}/twisted/plugins/__pycache__/magic_wormhole_transit_relay*.pyc

%changelog
