#
# spec file for package python-magic-wormhole-mailbox-server
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


%define skip_python36 1
Name:           python-magic-wormhole-mailbox-server
Version:        0.4.1
Release:        0
Summary:        Key exchange and control message server for Magic-Wormhole
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/warner/magic-wormhole-mailbox-server
Source:         https://files.pythonhosted.org/packages/source/m/magic-wormhole-mailbox-server/magic-wormhole-mailbox-server-%{version}.tar.gz
# https://github.com/magic-wormhole/magic-wormhole/issues/439
Patch0:         python-magic-wormhole-mailbox-server-no-mock.patch
BuildRequires:  %{python_module Twisted-tls >= 17.5.0}
BuildRequires:  %{python_module attrs >= 16.3.0}
BuildRequires:  %{python_module autobahn >= 0.14.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module treq}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted-tls >= 17.5.0
Requires:       python-attrs >= 16.3.0
Requires:       python-autobahn >= 0.14.1
BuildArch:      noarch
%python_subpackages

%description
The main server for Magic-Wormhole. This server performs
store-and-forward delivery for small key-exchange and control
messages. Bulk data is sent over a direct TCP connection, or through
a transit-relay.

%prep
%autosetup -p1 -n magic-wormhole-mailbox-server-%{version}
# https://github.com/magic-wormhole/magic-wormhole-mailbox-server/issues/35
sed '/six/d' setup.py src/magic_wormhole_mailbox_server.egg-info/requires.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src/wormhole_mailbox_server/test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/magic_wormhole_mailbox_server-%{version}*-info
%{python_sitelib}/twisted/plugins/magic_wormhole_mailbox.py
%{python_sitelib}/wormhole_mailbox_server
%pycache_only %{python_sitelib}/twisted/plugins/__pycache__/magic_wormhole_mailbox*.pyc

%changelog
