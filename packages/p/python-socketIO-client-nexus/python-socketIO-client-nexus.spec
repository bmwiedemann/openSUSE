#
# spec file for package python-socketIO-client-nexus
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
%define         skip_python2 1
Name:           python-socketIO-client-nexus
Version:        0.7.6
Release:        0
Summary:        A socketio client library
License:        MIT
URL:            https://github.com/nexus-devs/socketIO-client
Source:         https://files.pythonhosted.org/packages/source/s/socketIO-client-nexus/socketIO-client-nexus-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.7.0
Requires:       python-six
Requires:       python-websocket-client
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module websocket-client}
BuildRequires:  nodejs
# /SECTION
%python_subpackages

%description
This is a socket.io client library for Python.
You can use it to write test code for your socket.io server.

%prep
%setup -q -n socketIO-client-nexus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Test files missing and no tag to download
# See: https://github.com/nexus-devs/socketIO-client-2.0.3/pulls
# %%check
# DEBUG=* node tests/serve.js  # Start socket.io server in terminal one
# DEBUG=* node tests/proxy.js   # Start proxy server in terminal two
# %%python_exec -m nose

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
