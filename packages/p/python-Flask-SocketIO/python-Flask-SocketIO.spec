#
# spec file for package python-Flask-SocketIO
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-Flask-SocketIO
Version:        5.1.1
Release:        0
License:        MIT
Summary:        SocketIO integration for Flask applications
URL:            http://github.com/miguelgrinberg/Flask-SocketIO/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/F/Flask-SocketIO/Flask-SocketIO-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/miguelgrinberg/Flask-SocketIO/v%{version}/test_socketio.py
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module python-socketio >= 5.0.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Flask >= 0.9
Requires:       python-python-socketio >= 5.0.2

BuildArch:      noarch
%python_subpackages

%description
Socket.IO integration for Flask applications.

%prep
%setup -q -n Flask-SocketIO-%{version}
cp %{S:1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v test_socketio.py

%files  %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
