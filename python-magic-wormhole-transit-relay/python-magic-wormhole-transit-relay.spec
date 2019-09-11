#
# spec file for package python-magic-wormhole-transit-relay
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-magic-wormhole-transit-relay
Version:        0.1.2
Release:        0
License:        MIT
Summary:        Transit Relay server for Magic-Wormhole
Url:            https://github.com/warner/magic-wormhole-transit-relay
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/magic-wormhole-transit-relay/magic-wormhole-transit-relay-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  %{python_module Twisted >= 17.5.0}
BuildRequires:  %{python_module mock}
Requires:       python-Twisted >= 17.5.0
BuildArch:      noarch

%python_subpackages

%description
Transit Relay server for Magic-Wormhole

%prep
%setup -q -n magic-wormhole-transit-relay-%{version}

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
%{python_sitelib}/*

%changelog
