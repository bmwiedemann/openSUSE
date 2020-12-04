#
# spec file for package python-python-socketio
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
Name:           python-python-socketio
Version:        4.6.1
Release:        0
Summary:        SocketIO server
License:        MIT
URL:            http://github.com/miguelgrinberg/python-socketio/
Source:         https://github.com/miguelgrinberg/python-socketio/archive/v%{version}.tar.gz#/python-socketio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-engineio >= 3.13.0
Requires:       python-six >= 1.9.0
Suggests:       python-aiohttp >= 3.4
Suggests:       python-requests >= 2.21.0
Suggests:       python-websocket-client >= 0.54.0
Suggests:       python-websockets >= 7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-engineio >= 3.13.0}
BuildRequires:  %{python_module six >= 1.9.0}
# /SECTION
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
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
