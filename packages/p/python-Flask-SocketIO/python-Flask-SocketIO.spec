#
# spec file for package python-Flask-SocketIO
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-Flask-SocketIO
Version:        5.4.1
Release:        0
Summary:        SocketIO integration for Flask applications
License:        MIT
URL:            https://github.com/miguelgrinberg/Flask-SocketIO/
Source:         https://files.pythonhosted.org/packages/source/f/flask-socketio/flask_socketio-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-socketio >= 5.0.2}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-Flask >= 0.9
Requires:       python-python-socketio >= 5.0.2
BuildArch:      noarch
%python_subpackages

%description
Socket.IO integration for Flask applications.

%prep
%autosetup -n flask_socketio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v test_socketio.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/flask_socketio
%{python_sitelib}/Flask_SocketIO-%{version}.dist-info

%changelog
