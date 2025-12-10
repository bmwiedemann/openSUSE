#
# spec file for package python-python-socketio
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


%{?sle15_python_module_pythons}
Name:           python-python-socketio
Version:        5.15.0
Release:        0
Summary:        SocketIO server
License:        MIT
URL:            http://github.com/miguelgrinberg/python-socketio/
Source:         https://github.com/miguelgrinberg/python-socketio/archive/v%{version}.tar.gz#/python_socketio-%{version}.tar.gz
BuildRequires:  %{python_module bidict >= 0.21.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-engineio >= 4.11.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bidict >= 0.21.0
Requires:       python-python-engineio >= 4.11.0
Suggests:       python-aiohttp >= 3.4
Suggests:       python-requests >= 2.21.0
Suggests:       python-websocket-client >= 0.54.0
#Tests:
BuildRequires:  %{python_module aiohttp >= 3.4}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.21.0}
BuildRequires:  %{python_module simple-websocket}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module websocket-client >= 0.54.0}
BuildArch:      noarch
%python_subpackages

%description
Python implementation of the Socket.IO realtime server.

%prep
%setup -q -n python-socketio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires python-valkey, not packaged
ignore="--ignore tests/async/test_redis_manager.py "
ignore+="--ignore tests/common/test_redis_manager.py"
%pytest -rs $ignore -k 'not test_logger' --timeout=60

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/socketio
%{python_sitelib}/python_socketio-%{version}.dist-info

%changelog
