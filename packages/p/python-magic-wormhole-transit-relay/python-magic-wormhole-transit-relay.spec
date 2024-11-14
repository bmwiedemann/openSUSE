#
# spec file for package python-magic-wormhole-transit-relay
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


Name:           python-magic-wormhole-transit-relay
Version:        0.4.0
Release:        0
Summary:        Transit Relay server for Magic-Wormhole
License:        MIT
URL:            https://github.com/warner/magic-wormhole-transit-relay
Source:         https://files.pythonhosted.org/packages/source/m/magic-wormhole-transit-relay/magic-wormhole-transit-relay-%{version}.tar.gz
BuildRequires:  %{python_module Twisted >= 21.2.0}
BuildRequires:  %{python_module autobahn >= 21.3.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 21.2.0
Requires:       python-autobahn >= 21.3.1
BuildArch:      noarch
%python_subpackages

%description
Transit Relay server for Magic-Wormhole

%prep
%autosetup -p1 -n magic-wormhole-transit-relay-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_backpressure.py: tests here need internet connection
rm src/wormhole_transit_relay/test/test_backpressure.py
%pytest src/wormhole_transit_relay/test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/wormhole_transit_relay
%{python_sitelib}/magic_wormhole_transit_relay-%{version}.dist-info
%{python_sitelib}/twisted/plugins/magic_wormhole_transit_relay.py
%pycache_only %{python_sitelib}/twisted/plugins/__pycache__/magic_wormhole_transit_relay*.pyc

%changelog
