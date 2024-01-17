#
# spec file for package python-gevent-websocket
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


Name:           python-gevent-websocket
Version:        0.10.1
Release:        0
Summary:        Websocket handler for the gevent pywsgi server, a Python network library
License:        Apache-2.0
URL:            https://www.gitlab.com/noppo/gevent-websocket
Source:         https://files.pythonhosted.org/packages/source/g/gevent-websocket/gevent-websocket-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gevent
BuildArch:      noarch
%python_subpackages

%description
Websocket handler for the gevent pywsgi server, a Python network library

%prep
%setup -q -n gevent-websocket-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/geventwebsocket
%{python_sitelib}/gevent_websocket-%{version}*-info

%changelog
