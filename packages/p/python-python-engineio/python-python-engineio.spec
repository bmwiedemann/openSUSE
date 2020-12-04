#
# spec file for package python-python-engineio
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
Name:           python-python-engineio
Version:        3.14.1
Release:        0
Summary:        EngineIO server
License:        MIT
URL:            http://github.com/miguelgrinberg/python-engineio/
Source:         https://github.com/miguelgrinberg/python-engineio/archive/v%{version}.tar.gz#/python-engineio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
Recommends:     python-eventlet
Suggests:       python-aiohttp >= 3.4
Suggests:       python-requests >= 2.21.0
Suggests:       python-websocket-client >= 0.54.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.4}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.21.0}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module websocket-client >= 0.54.0}
# /SECTION
%python_subpackages

%description
Python implementation of the Engine.IO realtime server.

%prep
%setup -q -n python-engineio-%{version}

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
