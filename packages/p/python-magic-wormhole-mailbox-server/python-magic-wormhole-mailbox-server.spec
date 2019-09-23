#
# spec file for package python-magic-wormhole-mailbox-server
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-magic-wormhole-mailbox-server
Version:        0.3.1
Release:        0
Summary:        Key exchange and control message server for Magic-Wormhole
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/warner/magic-wormhole-mailbox-server
Source:         https://files.pythonhosted.org/packages/source/m/magic-wormhole-mailbox-server/magic-wormhole-mailbox-server-%{version}.tar.gz
BuildRequires:  %{python_module Twisted >= 17.5.0}
BuildRequires:  %{python_module attrs >= 16.3.0}
BuildRequires:  %{python_module autobahn >= 0.14.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module treq}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 17.5.0
Requires:       python-attrs >= 16.3.0
Requires:       python-autobahn >= 0.14.1
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
The main server for Magic-Wormhole. This server performs
store-and-forward delivery for small key-exchange and control
messages. Bulk data is sent over a direct TCP connection, or through
a transit-relay.

%prep
%setup -q -n magic-wormhole-mailbox-server-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src/wormhole_mailbox_server/test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
