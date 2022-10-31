#
# spec file for package python-python-socketio
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-python-socketio
Version:        5.7.2
Release:        0
Summary:        SocketIO server
License:        MIT
URL:            http://github.com/miguelgrinberg/python-socketio/
Source:         https://github.com/miguelgrinberg/python-socketio/archive/v%{version}.tar.gz#/python-socketio-%{version}.tar.gz
BuildRequires:  %{python_module bidict >= 0.21.0}
BuildRequires:  %{python_module python-engineio >= 4.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#Tests:
BuildRequires:  %{python_module msgpack}
Requires:       python-bidict >= 0.21.0
Requires:       python-python-engineio >= 4.1.0
Suggests:       python-aiohttp >= 3.4
Suggests:       python-requests >= 2.21.0
Suggests:       python-websocket-client >= 0.54.0
Suggests:       python-websockets >= 7.0
BuildArch:      noarch
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
Python implementation of the Socket.IO realtime server.

%prep
%setup -q -n python-socketio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs -k 'not test_logger'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/socketio
%{python_sitelib}/python_socketio-%{version}*-info

%changelog
